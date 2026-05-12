from fastapi import APIRouter, HTTPException
router = APIRouter(prefix="/api/console/sources", tags=["console"])
ARTIFACTS = [
 {"id":"art_email_A1","action_id":"A1","kind":"email_prompt","channel":"email","status":"ready"},
 {"id":"art_sms_A2","action_id":"A2","kind":"sms_prompt","channel":"sms","status":"ready"},
 {"id":"art_whatsapp_A3","action_id":"A3","kind":"whatsapp_prompt","channel":"whatsapp","status":"ready"},
 {"id":"art_voice_D","action_id":"D","kind":"voice_script","channel":"voice","status":"ready"},
 {"id":"art_voice_G","action_id":"G","kind":"voice_script","channel":"voice","status":"ready"},
 {"id":"art_voice_J","action_id":"J","kind":"voice_script","channel":"voice","status":"ready"}]
@router.get("")
def list_sources(): return {"items": ARTIFACTS}
@router.get("/{id}")
def get_source(id: str):
    item=next((a for a in ARTIFACTS if a["id"]==id), None)
    if not item: raise HTTPException(status_code=404, detail="Source not found")
    return {**item, "content": "Managed in campaign artifact storage"}
@router.patch("/{id}")
def patch_source(id: str, payload: dict): return {"ok": True, "id": id, "saved": True, "version": payload.get("version", "console-edit")}
@router.get("/{id}/history")
def history(id: str): return {"id": id, "versions": []}
@router.post("/{id}/test")
def test_source(id: str, payload: dict): return {"ok": True, "id": id, "recipient": payload.get("recipient", "current_user")}
