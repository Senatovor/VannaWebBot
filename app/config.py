import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Параметры базы данных
    DB_HOST: str
    DB_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    # Параметры LM
    OLLAMA_HOST: str
    OLLAMA_MODEL: str
    # Параметры векторной базы Qdrant
    QDRANT_URL: str
    # Параметры админа
    ADMIN_EMAIL: str
    ADMIN_PASSWORD: str
    # Параметры телеграмм бота
    TELEGRAM_BOT_TOKEN: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
    )

    def get_db_url(self) -> str:
        return (f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@'
                f'{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}')

    def get_users(self):
        return [
            {"email": self.ADMIN_EMAIL, "password": self.ADMIN_PASSWORD}
        ]


settings = Settings()
