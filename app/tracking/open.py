from fastapi import APIRouter, Depends, Response, Request
from app.deps import get_store
from app.storage.tables import utcnow
router=APIRouter(tags=["tracking"])
PIXEL=bytes.fromhex("47494638396101000100800000ffffff00000021f90401000000002c00000000010001000002024401003b")
@router.get("/track/open/{step_id}")
def open_track(step_id: str, request: Request, store=Depends(get_store)):
    store.upsert("events", {"event_id": f"open-{step_id}-{utcnow()}", "provider":"tracking", "channel":"email", "event_type":"opened", "step_id":step_id, "created_at":utcnow(), "payload":{"ua": request.headers.get("user-agent", "")}})
    return Response(PIXEL, media_type="image/gif")
