from datetime import date, timedelta

from fastapi import APIRouter

from app.metrics.service import MetricsService
from app.schemas.metrics import MetricsOverview

router = APIRouter(prefix="/api/v1/metrics", tags=["metrics"])
service = MetricsService()


@router.get("/overview", response_model=MetricsOverview)
def get_overview(start_date: date | None = None, end_date: date | None = None) -> MetricsOverview:
    resolved_end = end_date or date.today()
    resolved_start = start_date or (resolved_end - timedelta(days=30))
    return service.get_overview(start_date=resolved_start, end_date=resolved_end)


@router.get("/users", response_model=MetricsOverview)
def get_users_metrics(start_date: date | None = None, end_date: date | None = None) -> MetricsOverview:
    return get_overview(start_date=start_date, end_date=end_date)


@router.get("/gpts", response_model=MetricsOverview)
def get_gpts_metrics(start_date: date | None = None, end_date: date | None = None) -> MetricsOverview:
    return get_overview(start_date=start_date, end_date=end_date)


@router.get("/projects", response_model=MetricsOverview)
def get_projects_metrics(start_date: date | None = None, end_date: date | None = None) -> MetricsOverview:
    return get_overview(start_date=start_date, end_date=end_date)


@router.get("/impact", response_model=MetricsOverview)
def get_impact_metrics(start_date: date | None = None, end_date: date | None = None) -> MetricsOverview:
    return get_overview(start_date=start_date, end_date=end_date)
