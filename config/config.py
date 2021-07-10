from pydantic import BaseSettings
from functools import lru_cache
import os

env = os.environ.get("ENV")
if env is None:
    env = ""


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50
    mysql_host: str
    mysql_user: str
    mysql_password: str
    mysql_db: str

    class Config:
        env_file = f"config/{env}.env"


class AppSettings:

    @staticmethod
    @lru_cache()
    def get_settings():
        return Settings()
