"""Eyabantu supply chain model (BFB 321, Group 05).

Standalone module: no Flask, no database. Each function states its formula.
"""


def eta_minutes(distance_km, avg_speed_kmh, stops_ahead, dwell_min=1.5):
    """ETA = travel time + dwell time.  ETA = (d / v) * 60 + n * dwell."""
    if distance_km < 0 or avg_speed_kmh <= 0 or stops_ahead < 0:
        raise ValueError("distance >= 0, speed > 0, stops_ahead >= 0")
    return round(distance_km / avg_speed_kmh * 60 + stops_ahead * dwell_min, 1)


def expected_wait(headway_min):
    """Random passenger arrivals: average wait = headway / 2."""
    if headway_min <= 0:
        raise ValueError("headway must be > 0")
    return headway_min / 2


def occupancy_percentage(passengers, seats=15):
    """Occupancy % = passengers carried / seats available x 100 (max 100%)."""
    if seats <= 0:
        raise ValueError("seats must be > 0")
    return round(min(passengers / seats, 1.0) * 100, 1)


def confidence_score(pin_reports, gps_confirms, min_reports=3):
    """Route confidence (0 - 1) for a crowdsourced stop.

    Driver GPS counts double. Fewer than min_reports -> 'unverified' (score capped
    at 0.5) so a single wrong pin or low participation cannot publish a stop.
    """
    evidence = pin_reports + 2 * gps_confirms
    score = min(evidence / 10, 1.0)
    return round(score if evidence >= min_reports else min(score, 0.5), 2)


def forecast_demand(history, alpha=0.3):
    """Simple exponential smoothing: F(t+1) = a*A(t) + (1-a)*F(t).

    Replaces MPS (built for production) with a passenger-demand method.
    """
    if not history:
        raise ValueError("history cannot be empty")
    forecast = history[0]
    for actual in history[1:]:
        forecast = alpha * actual + (1 - alpha) * forecast
    return round(forecast, 1)


def demand_intensity(waiting_passengers, taxis_present, seats=15):
    """Heat-map value = passengers waiting / seats on hand. >1 means under-served."""
    capacity = taxis_present * seats
    return round(waiting_passengers / capacity, 2) if capacity else float("inf")


def demand_level(intensity):
    """Turn demand intensity into plain words for the heat map.

    Above 3 = Very high, 1.1 to 3 = High, 0.8 to below 1.1 = Moderate, below 0.8 = Low.
    """
    if intensity > 3:
        return "Very high"
    if intensity >= 1.1:
        return "High"
    if intensity >= 0.8:
        return "Moderate"
    return "Low"


def deploy_taxis(stops, spare_taxis, seats=15):
    """Deployment decision: send spare taxis to stops with the biggest seat shortfall.

    stops: {name: (waiting_passengers, taxis_present)}. Returns {name: taxis_sent}.
    """
    shortfall = {s: max(w - t * seats, 0) for s, (w, t) in stops.items()}
    plan = {s: 0 for s in stops}
    for _ in range(spare_taxis):
        worst = max(shortfall, key=shortfall.get)
        if shortfall[worst] == 0:
            break
        plan[worst] += 1
        shortfall[worst] = max(shortfall[worst] - seats, 0)
    return plan
