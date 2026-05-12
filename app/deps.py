from fastapi import Depends, Header, HTTPException, status
from app.config import Settings, get_settings
from app.storage.tables import TableStore

def get_store(settings: Settings = Depends(get_settings)) -> TableStore:
    return TableStore(settings)

def require_console_auth(settings: Settings = Depends(get_settings), authorization: str | None = Header(default=None)) -> bool:
    if not settings.console_auth_token:
        return True
    expected = f"Bearer {settings.console_auth_token}"
    if authorization != expected:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid console token")
    return True
