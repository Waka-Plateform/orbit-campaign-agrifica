from fastapi import APIRouter, Depends, Request
from app.deps import get_store
from app.storage.tables import utcnow
router=APIRouter(tags=["webhooks"])
@router.post("/webhooks/sms/event")
async def sms_event(request: Request, store=Depends(get_store)):
    payload=await request.json()
    store.upsert("events", {"event_id": f"sms-{utcnow()}", "provider":"acs_sms", "channel":"sms", "event_type": payload.get("eventType", "sms_event"), "created_at":utcnow(), "payload":payload})
    return {"ok": True}
