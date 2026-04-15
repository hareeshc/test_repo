from __future__ import annotations

from pathlib import Path

import polars as pl


class CsvSchemaError(ValueError):
    pass


REQUIRED_COLUMNS_BY_SOURCE: dict[str, set[str]] = {
    "users": {"user_id", "email", "active_flag", "exported_at"},
    "gpts": {"gpt_id", "name", "owner_user_id", "exported_at"},
    "projects": {"project_id", "name", "owner_user_id", "exported_at"},
    "impact": {"response_id", "user_id", "is_positive", "exported_at"},
}


def load_csv(source_name: str, path: Path) -> pl.DataFrame:
    if source_name not in REQUIRED_COLUMNS_BY_SOURCE:
        raise CsvSchemaError(f"Unsupported source: {source_name}")

    data = pl.read_csv(path)
    required_columns = REQUIRED_COLUMNS_BY_SOURCE[source_name]
    missing = required_columns - set(data.columns)
    if missing:
        missing_joined = ", ".join(sorted(missing))
        raise CsvSchemaError(f"Missing required columns for {source_name}: {missing_joined}")

    return data
