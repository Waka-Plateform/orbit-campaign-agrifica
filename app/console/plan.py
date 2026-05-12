from fastapi import APIRouter, Depends
from app.deps import get_store
from app.storage.tables import utcnow
router = APIRouter(prefix="/api/console/plan", tags=["console"])
DEFAULT = {"start_at": None, "end_at": None, "timezone": "Europe/Paris", "distribution": "linear", "batch_frequency": {"every": 1, "unit": "minute"}, "batch_size": 50, "allowed_windows": [{"days": ["mon","tue","wed","thu","fri"], "start_hour": 9, "end_hour": 19}], "throttle": {"max_per_minute": 30, "max_per_hour": 500, "max_per_day": 5000}, "paused": False, "runtime_state": {"lots_sent_today": 0, "lots_deferred": 0, "throttled_count": 0}}
def merge(a, b):
    out=dict(a)
    for k,v in b.items(): out[k]=merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out
@router.get("")
def get_plan(store=Depends(get_store)):
    rows=store.query("audit_log", top=50)
    schedule=next((r.get("payload") for r in rows if r.get("action")=="schedule_saved"), None)
    return DEFAULT if not schedule else merge(DEFAULT, __import__("json").loads(schedule))
@router.post("")
def save_plan(payload: dict, store=Depends(get_store)):
    schedule=merge(DEFAULT, payload)
    store.upsert("audit_log", {"audit_id": f"schedule-{utcnow()}", "actor":"console", "action":"schedule_saved", "resource":"schedule", "created_at": utcnow(), "payload": schedule})
    return schedule
@router.post("/{action}")
def lifecycle(action: str, store=Depends(get_store)):
    mapping={"start":"running","pause":"paused","resume":"running","stop":"finished","tick":"running"}
    status=mapping.get(action)
    if not status: return {"ok": False, "new_status": "unknown"}
    store.upsert("audit_log", {"audit_id": f"{action}-{utcnow()}", "actor":"console", "action":action, "resource":"campaign", "created_at": utcnow()})
    return {"ok": True, "new_status": status}
