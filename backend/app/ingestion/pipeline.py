from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from app.ingestion.csv_loader import load_csv


@dataclass(frozen=True)
class IngestionResult:
    source_name: str
    rows_loaded: int


def run_ingestion(source_name: str, path: Path) -> IngestionResult:
    frame = load_csv(source_name=source_name, path=path)
    return IngestionResult(source_name=source_name, rows_loaded=frame.height)
