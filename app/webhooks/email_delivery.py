from fastapi import APIRouter, Depends, Request
from app.deps import get_store
from app.storage.tables import utcnow
router=APIRouter(tags=["webhooks"])
@router.post("/webhooks/email/delivery")
async def email_delivery(request: Request, store=Depends(get_store)):
    payload=await request.json()
    store.upsert("events", {"event_id": f"email-{utcnow()}", "provider":"acs_email", "channel":"email", "event_type": payload.get("eventType", "delivery"), "created_at":utcnow(), "payload":payload})
    return {"ok": True}
