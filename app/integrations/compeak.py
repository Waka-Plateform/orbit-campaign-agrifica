import httpx
from app.config import Settings
class CompeakClient:
    def __init__(self, settings: Settings, token: str):
        self.base_url=settings.compeak_base_url.rstrip("/")
        self.token=token
    async def call(self, to: str, script_id: str, payload: dict):
        async with httpx.AsyncClient(timeout=30) as client:
            r=await client.post(f"{self.base_url}/calls", headers={"Authorization": f"Bearer {self.token}"}, json={"to":to,"script_id":script_id,"payload":payload})
            r.raise_for_status()
            return r.json()
