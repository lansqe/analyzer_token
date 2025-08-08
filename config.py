import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    POLYGON_RPC_URL: str = os.getenv("POLYGON_RPC_URL")
    TOKEN_ADDRESS: str = os.getenv("TOKEN_ADDRESS")

    class Config:
        case_sensitive = True


settings = Settings()