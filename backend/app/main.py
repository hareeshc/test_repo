from fastapi import FastAPI

from app.api.v1.ingestion import router as ingestion_router
from app.api.v1.metrics import router as metrics_router
from app.core.config import get_settings

settings = get_settings()
app = FastAPI(title=settings.app_name)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "environment": settings.environment}


app.include_router(metrics_router)
app.include_router(ingestion_router)
