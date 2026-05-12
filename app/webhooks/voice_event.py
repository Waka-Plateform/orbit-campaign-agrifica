from fastapi import APIRouter, Depends, Request
from app.deps import get_store
from app.storage.tables import utcnow
router=APIRouter(tags=["webhooks"])
@router.post("/webhooks/voice/event")
async def voice_event(request: Request, store=Depends(get_store)):
    payload=await request.json()
    store.upsert("events", {"event_id": f"voice-{utcnow()}", "provider":"compeak", "channel":"voice", "event_type": payload.get("status", "voice_event"), "created_at":utcnow(), "payload":payload})
    return {"ok": True}
