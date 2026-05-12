from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
router = APIRouter()
templates = Jinja2Templates(directory="templates")
SECTIONS = {"main", "base", "plan", "sources", "channels", "dashboard", "inbox"}
@router.get("/console")
def console_root():
    return RedirectResponse("/console/main", status_code=302)
@router.get("/console/{section}")
def console_section(request: Request, section: str):
    template = f"console/{section}.html" if section in SECTIONS else "console/main.html"
    return templates.TemplateResponse(template, {"request": request, "section": section})
