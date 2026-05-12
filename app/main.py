from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import structlog
from app.config import get_settings
from app.deps import get_store
from app.console import views, main as console_main, base, plan, sources, channels, dashboard, inbox, flow_svg, files, health
from app.tracking import open as track_open, click, unsubscribe
from app.webhooks import email_delivery, sms_event, whatsapp_event, voice_event, agent_callback
from app.events import sse

structlog.configure(processors=[structlog.processors.TimeStamper(fmt="iso"), structlog.processors.JSONRenderer()])
log = structlog.get_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    try:
        get_store(settings).ensure()
        log.info("tables_ready", campaign_id=settings.campaign_id)
    except Exception as exc:
        log.warning("tables_not_ready", error=str(exc))
    yield

app = FastAPI(title="orbit-campaign-agrifica", version="1.0.0", lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
for router in [health.router, views.router, console_main.router, files.router, base.router, plan.router, sources.router, channels.router, dashboard.router, inbox.router, flow_svg.router, track_open.router, click.router, unsubscribe.router, email_delivery.router, sms_event.router, whatsapp_event.router, voice_event.router, agent_callback.router, sse.router]:
    app.include_router(router)
