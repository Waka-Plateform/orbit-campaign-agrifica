import asyncio, json
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
router = APIRouter(tags=["events"])
async def stream():
    while True:
        yield f"event: heartbeat\ndata: {json.dumps({'ok': True})}\n\n"
        await asyncio.sleep(15)
@router.get("/events")
def events(): return StreamingResponse(stream(), media_type="text/event-stream")
