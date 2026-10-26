"""Unit tests checked against hand calculations. Run: py -m pytest"""
import pytest
import supply_chain_model as m


def test_eta():  # 5 km at 30 km/h = 10 min, + 2 stops x 1.5 = 13 min
    assert m.eta_minutes(5, 30, 2) == 13.0


def test_wait_and_occupancy():
    assert m.expected_wait(20) == 10
    assert m.occupancy_percentage(12) == 80.0  # 12 / 15 x 100


def test_confidence_low_participation_capped():
    assert m.confidence_score(1, 0) == 0.1
    assert m.confidence_score(4, 3) == 1.0


def test_forecast():  # 100 -> 0.3*130 + 0.7*100 = 109
    assert m.forecast_demand([100, 130]) == 109.0


def test_demand_intensity_and_level():  # 210 / (4 x 15) = 3.5
    assert m.demand_intensity(210, 4) == 3.5
    assert m.demand_level(3.5) == "Very high"
    assert m.demand_level(3) == "High"
    assert m.demand_level(1.1) == "High"
    assert m.demand_level(0.8) == "Moderate"
    assert m.demand_level(0.79) == "Low"


def test_deploy_goes_to_biggest_shortfall():
    plan = m.deploy_taxis({"Mamelodi": (60, 1), "Silverton": (10, 1)}, 3)
    assert plan == {"Mamelodi": 3, "Silverton": 0}


def test_bad_input():
    with pytest.raises(ValueError):
        m.eta_minutes(5, 0, 1)
