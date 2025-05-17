import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Параметры базы данных
    db_host: str
    db_port: int
    postgres_db: str
    postgres_user: str
    postgres_password: str
    # Параметры LM
    ollama_host: str
    ollama_model: str
    # Параметры векторной базы Qdrant
    qdrant_url: str
    # Параметры админа
    admin_email: str
    admin_password: str
    # Параметры телеграмм бота
    telegram_bot_token: str
    # SQL код для просмотра таблицы
    first_ddl: str
    first_sql: str
    first_question: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
    )

    def get_db_url(self) -> str:
        return (f'postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@'
                f'{self.db_host}:{self.db_port}/{self.postgres_db}')

    def get_users(self):
        return [
            {"email": self.admin_email, "password": self.admin_password}
        ]


settings = Settings()
