from pathlib import Path

from fastapi import APIRouter
from pydantic import BaseModel

from app.ingestion.pipeline import IngestionResult, run_ingestion

router = APIRouter(prefix="/api/v1/ingestion", tags=["ingestion"])


class IngestionRequest(BaseModel):
    source_name: str
    path: str


@router.post("/run", response_model=IngestionResult)
def trigger_ingestion(request: IngestionRequest) -> IngestionResult:
    return run_ingestion(source_name=request.source_name, path=Path(request.path))
