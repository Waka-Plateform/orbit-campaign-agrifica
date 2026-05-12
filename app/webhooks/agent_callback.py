from fastapi import APIRouter, Depends, Request
from app.deps import get_store
from app.storage.tables import utcnow
router=APIRouter(tags=["webhooks"])
@router.post("/webhooks/agent/{agent_id}")
async def agent_callback(agent_id: str, request: Request, store=Depends(get_store)):
    payload=await request.json()
    store.upsert("events", {"event_id": f"agent-{agent_id}-{utcnow()}", "provider":"waka_agent", "channel":"agent", "event_type": payload.get("type", "callback"), "created_at":utcnow(), "payload":payload})
    return {"ok": True, "agent_id": agent_id}
