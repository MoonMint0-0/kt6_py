import os
from fastapi import FastAPI

app = FastAPI(title="FastAPI Docker App")


@app.get("/")
def read_root():
    return {
        "status": "ok",
        "database_url": os.getenv("DATABASE_URL", "not set"),
        "celery_broker": os.getenv("CELERY_BROKER", "not set"),
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}