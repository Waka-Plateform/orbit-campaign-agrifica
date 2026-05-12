import importlib
from datetime import datetime, timezone
from app.actions._scheduler import should_run
SEND_NODES=["A1","A2","A3","G","J"]
async def tick(settings, store, schedule: dict):
    if not should_run(schedule, datetime.now(timezone.utc)):
        return {"ok": True, "ran": [], "deferred": True}
    ran=[]
    for node_id in SEND_NODES:
        module=importlib.import_module(f"app.actions.{node_id}")
        result=await module.run(settings, store)
        ran.append({"node_id": node_id, "result": result})
    return {"ok": True, "ran": ran, "deferred": False}
