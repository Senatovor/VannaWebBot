from vanna.ollama import Ollama
from vanna.qdrant import Qdrant_VectorStore
from qdrant_client import QdrantClient
from config import settings


class MyVanna(Qdrant_VectorStore, Ollama):
    def __init__(self, config=None):
        Qdrant_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config={
            'OLLAMA_HOST': settings.OLLAMA_HOST,
            'model': settings.OLLAMA_MODEL
        })


vn = MyVanna(
    config={
        'client': QdrantClient(url=settings.QDRANT_URL),
    })

vn.connect_to_postgres(
    host=settings.DB_HOST,
    dbname=settings.POSTGRES_DB,
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    port=settings.DB_PORT
)
