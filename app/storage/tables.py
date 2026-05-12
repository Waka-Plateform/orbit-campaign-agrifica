import json
from datetime import datetime, timezone
from typing import Any
from azure.core.exceptions import ResourceExistsError
from azure.data.tables import TableServiceClient
from azure.identity import DefaultAzureCredential
from app.config import Settings
from app.storage.schemas import TABLES

TABLE_MAP = {name: name.replace("_", "").title().replace(" ", "") for name in TABLES}
TABLE_MAP.update({"contacts": "Contacts", "step_output": "StepOutput", "audit_log": "AuditLog"})

def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()

class TableStore:
    def __init__(self, settings: Settings):
        self.settings = settings
        if settings.azure_storage_connection_string:
            self.service = TableServiceClient.from_connection_string(settings.azure_storage_connection_string)
        else:
            self.service = TableServiceClient(endpoint=settings.storage_table_endpoint, credential=DefaultAzureCredential())

    def table_name(self, logical: str) -> str:
        if logical not in TABLE_MAP:
            raise ValueError(f"Unsupported table: {logical}")
        return TABLE_MAP[logical]

    def ensure(self) -> None:
        for logical in TABLE_MAP:
            try:
                self.service.create_table(self.table_name(logical))
            except ResourceExistsError:
                continue

    def client(self, logical: str):
        return self.service.get_table_client(self.table_name(logical))

    def upsert(self, logical: str, entity: dict[str, Any]) -> dict[str, Any]:
        item = dict(entity)
        item.setdefault("PartitionKey", item.get("contact_id") or item.get("channel") or logical)
        item.setdefault("RowKey", item.get("id") or item.get("event_id") or item.get("msg_id") or item.get("contact_id") or f"{utcnow()}-{logical}")
        for key, value in list(item.items()):
            if isinstance(value, (dict, list)):
                item[key] = json.dumps(value, ensure_ascii=False)
        self.client(logical).upsert_entity(item)
        return item

    def query(self, logical: str, top: int = 100) -> list[dict[str, Any]]:
        return [dict(e) for e in self.client(logical).list_entities(results_per_page=top).by_page().__next__()]

    def count(self, logical: str) -> int:
        return sum(1 for _ in self.client(logical).list_entities(select=["PartitionKey"]))
