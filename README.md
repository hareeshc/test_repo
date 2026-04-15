# ChatGPT Enterprise Workspace Analytics App

Production-minded starter architecture and code skeleton for an internal analytics application built on ChatGPT Enterprise Workspace Analytics CSV exports.

## 1) Recommended tech stack

### Backend
- **Python 3.12**
- **FastAPI** for typed HTTP APIs
- **Pydantic v2** for settings and DTO validation
- **SQLAlchemy 2.0** for persistence (Postgres in prod, SQLite locally)
- **Alembic** for migrations
- **Polars** for fast CSV parsing and transformation
- **Uvicorn** ASGI server

### Data & orchestration
- **PostgreSQL** as primary warehouse-lite OLTP/analytics store
- **DuckDB (optional local)** for ad hoc dev analysis over CSV snapshots
- **APScheduler or simple cron-triggered CLI** for batch ingestion

### Frontend
- **React + TypeScript + Vite**
- **TanStack Query** for API state
- **Recharts** for charts
- **Tailwind CSS** for lightweight styling

### Testing / quality
- **pytest**, **httpx** for API tests
- **ruff** + **mypy** for lint/type checks

## 2) Repo structure

```text
.
├── backend/
│   ├── app/
│   │   ├── api/v1/
│   │   ├── core/
│   │   ├── db/
│   │   ├── ingestion/
│   │   ├── metrics/
│   │   └── schemas/
│   └── tests/
├── docs/
│   └── architecture.md
└── frontend/
    └── src/pages/
```

## 3) Normalized data model (summary)

See `docs/architecture.md` for full schema. High-level entities:
- `dim_user`
- `dim_gpt`
- `dim_project`
- `dim_tool`
- `dim_date`
- `fact_user_activity_daily`
- `fact_gpt_activity_daily`
- `fact_project_activity_daily`
- `fact_tool_usage_daily`
- `fact_impact_survey_response`
- `ingestion_batch`

## 4) CSV ingestion plan (summary)

1. Drop CSVs into an import folder by source and export date.
2. Run typed Polars loaders with schema validation + canonical column mapping.
3. Upsert dimensions, then load facts with `source_exported_at` and `batch_id` lineage.
4. Run metric refresh SQL/materialized views.
5. Expose audit and freshness in API.

## 5) Metrics layer (summary)

Implemented starter metrics:
- `activation_rate`
- `wau`
- `mau`
- `messages_per_active_user`
- `gpt_adoption_rate`
- `tool_adoption_rate`
- `project_adoption_rate`
- `impact_positive_response_rate`

## 6) Backend API plan (summary)

- `GET /health`
- `GET /api/v1/metrics/overview`
- `GET /api/v1/metrics/users`
- `GET /api/v1/metrics/gpts`
- `GET /api/v1/metrics/projects`
- `GET /api/v1/metrics/impact`
- `POST /api/v1/ingestion/run`

## 7) Frontend dashboard plan (summary)

Initial pages scaffolded:
- Executive Overview
- User Adoption
- GPT Portfolio
- Projects
- Impact

## 8) Phased implementation roadmap

Detailed in `docs/architecture.md`.

## Run backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
uvicorn app.main:app --reload
```

## Run tests

```bash
cd backend
pytest
```
