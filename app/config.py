from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="", case_sensitive=False)
    service_name: str = "orbit-campaign-agrifica"
    campaign_id: str = "ab5b944c-e9cb-4bf7-bd69-fbdca33a1aa1"
    campaign_name: str = "AGRIFICA"
    slug: str = "agrifica"
    location: str = "francecentral"
    resource_group: str = "rg-orbit-campaign-agrifica"
    container_app: str = "orbit-campaign-agrifica"
    container_app_url: str = ""
    key_vault_name: str = "kv-orbit-camp-agrifica"
    storage_account: str = "stcampagrifica"
    managed_identity: str = "id-orbit-campaign-agrifica"
    github_repo: str = "Waka-Plateform/orbit-campaign-agrifica"
    azure_storage_connection_string: str = ""
    storage_table_endpoint: str = "https://stcampagrifica.table.core.windows.net"
    storage_blob_endpoint: str = "https://stcampagrifica.blob.core.windows.net"
    acs_email_connection_string: str = ""
    acs_sms_connection_string: str = ""
    compeak_base_url: str = ""
    foundry_base_url: str = ""
    hmac_tracking_secret: str = ""
    console_auth_token: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
