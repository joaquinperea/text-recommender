from sentence_transformers import SentenceTransformer
from app.config import settings

class EmbeddingModel:
    """A class to handle the embedding model for text data."""
    def __init__(self):
        self.model = SentenceTransformer(settings.model_name)

    def encode(self, texts):
        """Encode a list of texts into embeddings."""
        return self.model.encode(texts, convert_to_tensor=True)

embedding_model = EmbeddingModel()
