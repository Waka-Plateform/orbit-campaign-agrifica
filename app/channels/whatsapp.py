import httpx
async def send_whatsapp(base_url: str, token: str, to: str, body: str):
    async with httpx.AsyncClient(timeout=30) as client:
        r=await client.post(base_url.rstrip('/') + '/messages', headers={'Authorization': f'Bearer {token}'}, json={'to': to, 'body': body})
        r.raise_for_status()
        return r.json()
