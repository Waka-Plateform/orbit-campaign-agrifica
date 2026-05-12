import httpx
from app.config import Settings
class FoundryAgentsClient:
    def __init__(self, settings: Settings, token: str):
        self.base_url=settings.foundry_base_url.rstrip("/")
        self.token=token
    async def run(self, agent_id: str, payload: dict):
        async with httpx.AsyncClient(timeout=60) as client:
            r=await client.post(f"{self.base_url}/agents/{agent_id}/runs", headers={"Authorization": f"Bearer {self.token}"}, json=payload)
            r.raise_for_status()
            return r.json()
