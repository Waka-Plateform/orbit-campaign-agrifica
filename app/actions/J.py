from app.storage.tables import utcnow
async def run(settings, store):
    store.upsert("audit_log", {"audit_id": f"J-{utcnow()}", "actor":"scheduler", "action":"voice_call", "resource":"J", "created_at":utcnow()})
    return {"queued": True, "channel": "voice", "node_id": "J"}
