from fastapi import APIRouter, Depends, Query
from fastapi.responses import RedirectResponse
from app.deps import get_store
from app.storage.tables import utcnow
router=APIRouter(tags=["tracking"])
@router.get("/track/click/{step_id}")
def click(step_id: str, url: str = Query(...), store=Depends(get_store)):
    store.upsert("events", {"event_id": f"click-{step_id}-{utcnow()}", "provider":"tracking", "channel":"link", "event_type":"clicked", "step_id":step_id, "created_at":utcnow(), "payload":{"url":url}})
    return RedirectResponse(url)
