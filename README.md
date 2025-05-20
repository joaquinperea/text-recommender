# 🧠 Text Recommender System

A semantic text recommender system built with Python, FastAPI, FAISS, and Sentence Transformers.  
It indexes a corpus of articles and returns the most semantically similar ones based on a user query.

## 📌 Features

- 🔍 Semantic search using sentence-transformers embeddings.
- ⚡ Fast and scalable similarity search with FAISS.
- 🚀 REST API built with FastAPI.
- 🧪 Unit tested with Pytest.
- 🐳 Easy to run with Docker and Docker Compose.

---

## 🧰 Tech Stack

- **Python 3.10**
- **FastAPI**
- **FAISS (Facebook AI Similarity Search)**
- **Sentence-Transformers**
- **Uvicorn**
- **Pytest**
- **Docker**

---

## 📁 Project Structure
```bash
text-recommender/
├── app/
│ ├── main.py # FastAPI entry point
│ ├── recommender.py # Core logic for embedding and querying
│ ├── models.py # Pydantic models
│ ├── config.py # Environment configuration (Pydantic v2)
│ └── data/articles.json # Default dataset
├── tests/
│ └── test_recommender.py # Unit test for recommendation logic
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```


## 🚀 Getting Started

### 🔧 Prerequisites
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 🏗️ Build and Run
```bash
# Build the image
docker compose build

# Start the container
docker compose up
API will be available at:
📍 http://localhost:8000/docs (Swagger UI)
```

🧪 Run Tests
```bash
docker compose exec recommender pytest tests/
```

🧠 How It Works
At startup, the app loads a list of articles from data/articles.json.
Each article is embedded using a sentence-transformers model (all-MiniLM-L6-v2 by default).
The embeddings are indexed using FAISS for fast vector similarity search.
You can send a GET request to /recommend?query=... and the app will return the most similar articles.

Example:
```bash
GET /recommend?query=climate change

Response:
{
  "query": "climate change",
  "results": [
    {
      "text": "New climate policies have been introduced...",
      "score": 0.89
    },
    ...
  ]
}
```

⚙️ Configuration
You can customize the model and dataset using environment variables:
```bash
Variable	Default	Description
MODEL_NAME	sentence-transformers/all-MiniLM-L6-v2	HuggingFace model for embeddings
DATA_PATH	data/articles.json	Path to the input articles JSON
```

You can set these in a .env file or directly in docker-compose.yml.

📦 Future Improvements
- 🧠 Persist embeddings on disk (e.g., using ChromaDB).
- 🔒 Add authentication for protected API access.
- 💾 Allow uploading custom datasets.
- 📊 Track query statistics.

📬 Contact

Made by Joaquín Perea

Currently seeking new opportunities as a Python developer or backend engineer.

Feel free to connect or reach out!