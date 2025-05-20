from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Text Recommender API")
app.include_router(router)
