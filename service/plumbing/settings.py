from pydantic import BaseSettings, PostgresDsn, AnyHttpUrl, EmailStr

class Settings(BaseSettings):
    # Authentication
    first_user_email:EmailStr = "admin@example.com"
    first_user_password:str = "password"
    
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    
    # Database
    pg_dsn: PostgresDsn = 'postgres://user:pass@postgres:5432/ftsbffwebadmin'

    # FreeTakServer configuration
    fts_url: AnyHttpUrl
    fts_public_url: AnyHttpUrl
    fts_secret_key: str # Not yet sure what this does
    
    fts_certpath: str = "/opt/fts/certs/" # Mount in this directory for now
    fts_crtfilepath: str = f"{fts_certpath}pubserver.pem"
    fts_keyfilepath:str = f"{fts_certpath}pubserver.key.unencrypted"
    
    # the webSocket  key used by the UI to communicate with FTS.
    fts_websocket_key: str
    
    # the API key used by the UI to comunicate with FTS. generate a new system user and then set it
    fts_api_key:str = 'Bearer token'
    
    class Config:
        env_prefix = 'setting_' # Enables you to set env vars for all settings: export setting_fts_url=https://123.32.21.12:8081
    
settings = Settings()