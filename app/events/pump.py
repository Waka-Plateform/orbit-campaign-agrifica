import asyncio
import structlog
log=structlog.get_logger()
async def poll_shared_mailbox(interval_seconds: int = 60):
    while True:
        log.info("mailbox_poll_tick")
        await asyncio.sleep(interval_seconds)
