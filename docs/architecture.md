# Architecture Plan: ChatGPT Enterprise Workspace Analytics

## Constraints to design around
- Data is currently CSV-export based (batch ingest).
- Workspace Analytics is aggregated (not prompt-level).
- Task insights are not exportable yet.
- No real-time guarantees; freshness should be explicit.

## Recommended tech stack
- Backend: Python, FastAPI, SQLAlchemy, Alembic, Polars.
- DB: PostgreSQL (production), SQLite for local tests.
- Frontend: React + TypeScript + Vite + Recharts.
- Infra: Docker for local parity, cron/scheduler for ingestion.

## Proposed repo layout
```text
backend/
  app/
    api/v1/
      metrics.py
      ingestion.py
    core/
      config.py
    db/
      base.py
      models.py
      session.py
    ingestion/
      csv_loader.py
      pipeline.py
    metrics/
      calculations.py
      service.py
    schemas/
      metrics.py
  tests/
frontend/
  src/
    pages/
```

## Normalized data model

### Dimensions
- `dim_user(user_id, email, department, role, is_active, created_at, updated_at)`
- `dim_gpt(gpt_id, name, owner_user_id, visibility, is_archived, created_at, updated_at)`
- `dim_project(project_id, name, owner_user_id, status, created_at, updated_at)`
- `dim_tool(tool_id, tool_name, tool_category, created_at, updated_at)`
- `dim_date(date_key, calendar_date, week_start, month_start, quarter, year)`

### Facts
- `fact_user_activity_daily(date_key, user_id, messages_sent, active_flag)`
- `fact_gpt_activity_daily(date_key, gpt_id, unique_users, messages, runs)`
- `fact_project_activity_daily(date_key, project_id, unique_users, messages, active_flag)`
- `fact_tool_usage_daily(date_key, tool_id, user_id, invocations)`
- `fact_impact_survey_response(response_id, date_key, user_id, question_key, response_value, is_positive)`

### Ingestion/audit
- `ingestion_batch(batch_id, source_name, source_file, exported_at, ingested_at, row_count, checksum, status)`

## CSV ingestion plan
1. **Landing**: store raw files in immutable path (`/data/raw/<source>/<export_date>/file.csv`).
2. **Validation**: schema checks, required columns, dedupe keys, date parse validation.
3. **Standardization**: map source column names to canonical model names.
4. **Load dimensions**: upsert users/GPTs/projects/tools.
5. **Load facts**: insert daily aggregates with `batch_id` and `exported_at` lineage.
6. **Data quality**: freshness, row-count anomaly checks, null threshold checks.
7. **Publish**: refresh metric views/tables used by API.

## Metrics layer
Define metrics in code-first form (versioned):
- `activation_rate = activated_users / eligible_users`
- `wau = distinct active users over trailing 7 days`
- `mau = distinct active users over trailing 30 days`
- `messages_per_active_user = total_messages / active_users`
- `gpt_adoption_rate = users_using_any_gpt / eligible_users`
- `tool_adoption_rate = users_using_any_tool / eligible_users`
- `project_adoption_rate = users_active_in_projects / eligible_users`
- `impact_positive_response_rate = positive_responses / total_responses`

## Backend API plan
- `GET /health`: health + data freshness.
- `GET /api/v1/metrics/overview?start_date=&end_date=`
- `GET /api/v1/metrics/users?start_date=&end_date=`
- `GET /api/v1/metrics/gpts?start_date=&end_date=`
- `GET /api/v1/metrics/projects?start_date=&end_date=`
- `GET /api/v1/metrics/impact?start_date=&end_date=`
- `POST /api/v1/ingestion/run`: trigger batch pipeline.

## Frontend dashboard plan
- Executive Overview: KPI cards + trend charts + freshness banner.
- User Adoption: activation cohorts, WAU/MAU trends, messages/user.
- GPT Portfolio: top GPTs, adoption distribution, stale GPT detection.
- Projects: active projects, adoption by team, project health.
- Impact: positive rate trend, question-level breakdown.

## Phased roadmap
1. **Phase 0 (Week 1)**: scaffold repo, schemas, ingestion MVP, overview API.
2. **Phase 1 (Weeks 2-3)**: all key metrics + dashboard pages + tests.
3. **Phase 2 (Weeks 4-5)**: data quality checks, lineage/audit UI, auth/RBAC.
4. **Phase 3 (Weeks 6+)**: add Codex analytics + engineering productivity facts.

## Extensibility for Codex analytics
Add new facts without breaking current consumers:
- `fact_codex_usage_daily` (runs, tokens, repositories touched, PRs generated)
- `fact_engineering_productivity_daily` (cycle time, merged PRs, incidents)

Keep metrics versioned (`metric_definitions` table) so formulas evolve safely.
