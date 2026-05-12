# orbit-campaign-agrifica

Runtime FastAPI de la campaña AGRIFICA.

## Service

- Console: `/console/*`
- API console: `/api/console/*`
- Health: `/health`
- Port: `8000`

## Azure naming

- Resource group: `rg-orbit-campaign-agrifica`
- Container App: `orbit-campaign-agrifica`
- Storage: `stcampagrifica`
- Key Vault: `kv-orbit-camp-agrifica`
- Managed identity: `id-orbit-campaign-agrifica`

## Local run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Runtime storage requires Azure credentials and campaign environment variables.
