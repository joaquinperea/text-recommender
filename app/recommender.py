import json
import faiss
import numpy as np
from app.embeddings import embedding_model
from app.config import settings

class Recommender:
    """
    A class to handle the recommendation system using FAISS for 
    fast nearest neighbor search.
    """
    def __init__(self):
        with open(settings.data_path, encoding="utf-8") as f:
            self.articles = json.load(f)

        self.texts = [a["content"] for a in self.articles]
        self.embeddings = embedding_model.encode(self.texts)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.asarray(self.embeddings, dtype=np.float32))

    def recommend(self, query, top_k=5):
        """
        Recommend articles based on a query using the FAISS index.
        """
        query_embedding = embedding_model.encode([query])[0]
        D, I = self.index.search(np.array([query_embedding]), top_k)
        return [self.articles[i] | {"score": float(D[0][j])} for j, i in enumerate(I[0])]

recommender = Recommender()
