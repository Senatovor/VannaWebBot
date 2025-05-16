from vanna.ollama import Ollama
from vanna.qdrant import Qdrant_VectorStore
from qdrant_client import QdrantClient
from config import settings


class MyVanna(Qdrant_VectorStore, Ollama):
    def __init__(self, config=None):
        Qdrant_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config={
            'ollama_host': settings.ollama_host,
            'model': settings.ollama_model
        })


def vanna_setup() -> MyVanna:
    vn = MyVanna(
        config={
            'client': QdrantClient(url=settings.qdrant_url),
        })

    vn.connect_to_postgres(
        host=settings.db_host,
        dbname=settings.postgres_db,
        user=settings.postgres_user,
        password=settings.postgres_password,
        port=settings.db_port
    )

    return vn
