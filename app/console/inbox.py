from fastapi import APIRouter, Depends
from app.deps import get_store
from app.storage.tables import utcnow
router = APIRouter(prefix="/api/console/inbox", tags=["console"])
@router.get("/{channel}")
def list_inbox(channel: str, store=Depends(get_store)):
    rows=[r for r in store.query("inbox", top=500) if r.get("channel")==channel]
    return {"channel": channel, "messages": rows}
@router.post("/{msg_id}/reply")
def reply(msg_id: str, payload: dict, store=Depends(get_store)):
    store.upsert("audit_log", {"audit_id": f"reply-{msg_id}-{utcnow()}", "actor":"console", "action":"reply", "resource":msg_id, "created_at":utcnow(), "payload": payload})
    return {"ok": True, "msg_id": msg_id, "queued": True}
