from datetime import datetime, timezone
from fastapi import APIRouter, Depends
from app.config import Settings, get_settings
from app.deps import get_store
router = APIRouter(prefix="/api/console", tags=["console"])
@router.get("/main")
def get_main(settings: Settings = Depends(get_settings), store=Depends(get_store)):
    counts = {}
    for table in ["contacts", "step_output", "optout", "conversions"]:
        try: counts[table] = store.count(table)
        except Exception: counts[table] = 0
    processed = counts.get("step_output", 0)
    contacts = counts.get("contacts", 0)
    return {"campaign": {"id": settings.campaign_id, "name": settings.campaign_name, "slug": settings.slug, "objective": "Contactar agricultores y ganaderos para iniciar relación Waka/IFAD y convertir hacia la creación de agentes virtuales.", "status": "draft", "go_live_at": None, "duration_planned_seconds": 2592000, "duration_elapsed_seconds": 0}, "kpi_ops": {"volume_target": {"value": max(contacts, 10000), "label": "Volume cible"}, "volume_processed": {"value": processed, "label": "Volume traité"}, "volume_open": {"value": max(contacts - processed, 0), "label": "Touchés non clôturés"}, "file_closure_rate": {"value": processed / contacts if contacts else 0, "target": 1.0, "label": "Taux de clôture", "viz": "gauge"}, "campaign_duration": {"elapsed_seconds": 0, "planned_seconds": 2592000, "label": "Temps écoulé", "viz": "progress"}, "kpi_business_primary": {"id": "interactions_started", "label": "Interacciones iniciadas", "value": processed, "target": 10000, "format": "absolute", "viz": "progress"}}, "audiences": [{"id": "aud_sl", "name": "Sierra Leona", "count_current": 0}, {"id": "aud_ci", "name": "Costa de Marfil", "count_current": 0}, {"id": "aud_br", "name": "Brasil", "count_current": 0}, {"id": "aud_mx", "name": "México", "count_current": 0}], "volume_by_channel": [], "azure_resources": {"resource_group": settings.resource_group, "container_app": settings.container_app, "container_app_url": settings.container_app_url, "key_vault": settings.key_vault_name, "storage_account": settings.storage_account, "managed_identity": settings.managed_identity, "github_repo": settings.github_repo}}
