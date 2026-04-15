from app.metrics.calculations import (
    MetricInputs,
    activation_rate,
    gpt_adoption_rate,
    impact_positive_response_rate,
    messages_per_active_user,
    project_adoption_rate,
    safe_rate,
    tool_adoption_rate,
)


def test_safe_rate_zero_division() -> None:
    assert safe_rate(10, 0) == 0.0


def test_core_metric_calculations() -> None:
    inputs = MetricInputs(
        eligible_users=100,
        activated_users=55,
        wau_users=40,
        mau_users=65,
        active_users=65,
        messages_sent=1300,
        users_using_gpts=50,
        users_using_tools=45,
        users_using_projects=35,
        impact_positive_responses=80,
        impact_total_responses=100,
    )

    assert activation_rate(inputs) == 0.55
    assert messages_per_active_user(inputs) == 20.0
    assert gpt_adoption_rate(inputs) == 0.5
    assert tool_adoption_rate(inputs) == 0.45
    assert project_adoption_rate(inputs) == 0.35
    assert impact_positive_response_rate(inputs) == 0.8
