from fastapi import APIRouter, Depends
from app.config import Settings, get_settings
router = APIRouter()
@router.get("/health")
def health(settings: Settings = Depends(get_settings)):
    return {"ok": True, "service": settings.service_name, "campaign_id": settings.campaign_id}
