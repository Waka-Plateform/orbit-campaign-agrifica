from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from app.deps import get_store
from app.storage.tables import utcnow
router=APIRouter(tags=["tracking"])
@router.get("/unsubscribe/{contact_id}", response_class=HTMLResponse)
def unsubscribe(contact_id: str, channel: str = "all", store=Depends(get_store)):
    store.upsert("optout", {"contact_id":contact_id, "channel":channel, "reason":"user_unsubscribe", "created_at":utcnow()})
    return "<html><body><h1>Baja registrada</h1><p>No volveremos a contactar este destinatario para esta campaña.</p></body></html>"
