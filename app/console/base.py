import json
from fastapi import APIRouter, Depends, HTTPException, Query
from app.deps import get_store
from app.storage.schemas import TABLES, schema_for
router = APIRouter(prefix="/api/console/base", tags=["console"])
def apply_filters(rows, q, filters, sort):
    data = rows
    if q:
        data = [r for r in data if any(q.lower() in str(v).lower() for v in r.values() if isinstance(v, str))]
    if filters:
        for f in json.loads(filters):
            field, op, value = f.get("field"), f.get("op"), f.get("value")
            if op == "contains": data = [r for r in data if value.lower() in str(r.get(field, "")).lower()]
            elif op == "equals": data = [r for r in data if str(r.get(field, "")) == str(value)]
            elif op == "not_equals": data = [r for r in data if str(r.get(field, "")) != str(value)]
    if sort:
        for spec in reversed(sort.split(",")):
            field, _, direction = spec.partition(":")
            data = sorted(data, key=lambda r: str(r.get(field, "")), reverse=direction == "desc")
    return data
@router.get("/{table}")
def table_rows(table: str, page: int = 1, per_page: int = 50, q: str | None = None, sort: str | None = None, filter: str | None = None, store=Depends(get_store)):
    if table not in TABLES: raise HTTPException(status_code=404, detail="Unsupported table")
    per_page = min(max(per_page, 1), 100)
    rows = apply_filters(store.query(table, top=5000), q, filter, sort)
    start = (page - 1) * per_page
    return {"table": table, "total": len(rows), "page": page, "per_page": per_page, "rows": rows[start:start+per_page]}
@router.get("/{table}/schema")
def table_schema(table: str, store=Depends(get_store)):
    if table not in TABLES: raise HTTPException(status_code=404, detail="Unsupported table")
    return schema_for(table, store.query(table, top=100))
