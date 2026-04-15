from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MetricInputs:
    eligible_users: int
    activated_users: int
    wau_users: int
    mau_users: int
    active_users: int
    messages_sent: int
    users_using_gpts: int
    users_using_tools: int
    users_using_projects: int
    impact_positive_responses: int
    impact_total_responses: int


def safe_rate(numerator: int, denominator: int) -> float:
    if denominator <= 0:
        return 0.0
    return numerator / denominator


def activation_rate(inputs: MetricInputs) -> float:
    return safe_rate(inputs.activated_users, inputs.eligible_users)


def messages_per_active_user(inputs: MetricInputs) -> float:
    return safe_rate(inputs.messages_sent, inputs.active_users)


def gpt_adoption_rate(inputs: MetricInputs) -> float:
    return safe_rate(inputs.users_using_gpts, inputs.eligible_users)


def tool_adoption_rate(inputs: MetricInputs) -> float:
    return safe_rate(inputs.users_using_tools, inputs.eligible_users)


def project_adoption_rate(inputs: MetricInputs) -> float:
    return safe_rate(inputs.users_using_projects, inputs.eligible_users)


def impact_positive_response_rate(inputs: MetricInputs) -> float:
    return safe_rate(inputs.impact_positive_responses, inputs.impact_total_responses)
