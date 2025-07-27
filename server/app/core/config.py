from pydantic_settings import BaseSettings
from typing import List

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("init the config of the admin-user-order")


class Settings(BaseSettings):
    PROJECT_NAME: str = "admin-order-backend"
    VERSION: str = "0.1.0"

    # DB
    # DB_URL: str = "sqlite:///./app.db"  # 生产请切换到 MySQL/PostgreSQL
    # CREATE USER admin_user WITH ENCRYPTED PASSWORD 'admin14145';
    DB_URL: str = "postgresql://admin_user:admin14145@101.133.159.192/admin_order_db"

    class Config:
        env_file = ".env.development"
        env_file_encoding = "utf-8"


settings = Settings()
