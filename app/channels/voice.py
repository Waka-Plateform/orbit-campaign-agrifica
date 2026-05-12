from app.integrations.compeak import CompeakClient
async def start_voice_call(settings, token, to, script_id, payload):
    return await CompeakClient(settings, token).call(to, script_id, payload)
