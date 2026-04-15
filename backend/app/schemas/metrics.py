from datetime import date

from pydantic import BaseModel


class MetricsOverview(BaseModel):
    start_date: date
    end_date: date
    activation_rate: float
    wau: int
    mau: int
    messages_per_active_user: float
    gpt_adoption_rate: float
    tool_adoption_rate: float
    project_adoption_rate: float
    impact_positive_response_rate: float
