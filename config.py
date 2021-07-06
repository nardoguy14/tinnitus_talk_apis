from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50
    mysql_host: str
    mysql_user: str
    mysql_password: str
    mysql_db: str

    class Config:
        env_file = ".env"


class AppSettings:

    @staticmethod
    @lru_cache()
    def get_settings():
        return Settings()