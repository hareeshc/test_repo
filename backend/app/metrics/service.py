from __future__ import annotations

from datetime import date

from app.metrics.calculations import (
    MetricInputs,
    activation_rate,
    gpt_adoption_rate,
    impact_positive_response_rate,
    messages_per_active_user,
    project_adoption_rate,
    tool_adoption_rate,
)
from app.schemas.metrics import MetricsOverview


class MetricsService:
    """Starter in-memory service.

    Replace this with DB queries that aggregate fact tables by date window.
    """

    def get_overview(self, start_date: date, end_date: date) -> MetricsOverview:
        inputs = MetricInputs(
            eligible_users=120,
            activated_users=84,
            wau_users=61,
            mau_users=89,
            active_users=89,
            messages_sent=3560,
            users_using_gpts=76,
            users_using_tools=63,
            users_using_projects=54,
            impact_positive_responses=230,
            impact_total_responses=290,
        )

        return MetricsOverview(
            start_date=start_date,
            end_date=end_date,
            activation_rate=activation_rate(inputs),
            wau=inputs.wau_users,
            mau=inputs.mau_users,
            messages_per_active_user=messages_per_active_user(inputs),
            gpt_adoption_rate=gpt_adoption_rate(inputs),
            tool_adoption_rate=tool_adoption_rate(inputs),
            project_adoption_rate=project_adoption_rate(inputs),
            impact_positive_response_rate=impact_positive_response_rate(inputs),
        )
