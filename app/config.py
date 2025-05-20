import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    """Settings for the application."""
    model_name: str = os.getenv(
        "MODEL_NAME",
        "sentence-transformers/all-MiniLM-L6-v2"
    )
    data_path: str = os.getenv(
        "DATA_PATH",
        "data/articles.json"
    )

settings = Settings()
