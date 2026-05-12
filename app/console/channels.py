from fastapi import APIRouter
router = APIRouter(prefix="/api/console", tags=["console"])
@router.get("/channels")
def get_channels():
    return {"channels": [{"id":"email","enabled":True,"provider":"azure_communication_email"},{"id":"sms","enabled":True,"provider":"azure_communication_sms","requires_activation":True},{"id":"whatsapp","enabled":True,"provider":"configured_webhook","requires_activation":True},{"id":"voice","enabled":True,"provider":"compeak"},{"id":"web_text","enabled":True,"agent_id":"PENDING_TEXT_AGENT_TO_CREATE"},{"id":"web_voice","enabled":True,"agent_id":"e746d2df-e0cb-4edc-91bc-15826a6d38ba"},{"id":"web_avatar","enabled":True,"agent_id":"79b01efe-adcc-4718-a61c-e108e9a06e64"}]}
