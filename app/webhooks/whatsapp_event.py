from fastapi import APIRouter, Depends, Request
from app.deps import get_store
from app.storage.tables import utcnow
router=APIRouter(tags=["webhooks"])
@router.post("/webhooks/whatsapp/event")
async def whatsapp_event(request: Request, store=Depends(get_store)):
    payload=await request.json()
    store.upsert("events", {"event_id": f"whatsapp-{utcnow()}", "provider":"whatsapp", "channel":"whatsapp", "event_type": payload.get("type", "message"), "created_at":utcnow(), "payload":payload})
    if payload.get("message"):
        store.upsert("inbox", {"msg_id": payload.get("id", f"wa-{utcnow()}"), "channel":"whatsapp", "body":payload.get("message"), "received_at":utcnow(), "status":"new"})
    return {"ok": True}
