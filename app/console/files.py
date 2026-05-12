from pathlib import Path
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import PlainTextResponse
router = APIRouter(prefix="/api/console/main", tags=["console"])
ROOT = Path.cwd()
def category(path: str) -> str:
    if path.startswith("app/actions/"): return "actions"
    if path.startswith("app/channels/"): return "channels"
    if path.startswith("app/console/"): return "console"
    if path.startswith("app/tracking/"): return "tracking"
    if path.startswith("app/webhooks/"): return "webhooks"
    if path.startswith("app/events/"): return "events"
    if path.startswith("app/storage/"): return "storage"
    if path.startswith("app/integrations/"): return "integrations"
    if path.startswith("infra/"): return "infra"
    if path.startswith(".github/"): return "cicd"
    if path in {"app/main.py", "app/config.py"}: return "runtime"
    return "other"
@router.get("/files")
def list_files():
    tree=[]
    for p in ROOT.rglob("*"):
        if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts:
            rel=str(p.relative_to(ROOT))
            tree.append({"path": rel, "type": "file", "size_bytes": p.stat().st_size, "category": category(rel)})
    return {"repo": "Waka-Plateform/orbit-campaign-agrifica", "tree": sorted(tree, key=lambda x: x["path"])}
@router.get("/files/content", response_class=PlainTextResponse)
def file_content(path: str = Query(...)):
    target=(ROOT / path).resolve()
    if ROOT not in target.parents and target != ROOT:
        raise HTTPException(status_code=400, detail="Path outside repository")
    if not target.is_file():
        raise HTTPException(status_code=404, detail="File not found")
    return target.read_text(encoding="utf-8")
