"""Runs the model on demo pilot data (the figures shown on the HTML pages).

Demo data only - not measured. 6 Tshwane routes into Pretoria CBD.
"""
import supply_chain_model as m

# stop: (route, distance_km, stops_ahead, pin_reports, gps_confirms, waiting, taxis_present)
stops = {
    "Mamelodi Rank":       ("Mamelodi - Pretoria CBD",       2, 0, 4, 3, 210, 4),
    "Denneboom":           ("Mamelodi - Pretoria CBD",       6, 3, 4, 2, 95, 3),
    "Silverton":           ("Silverton - Pretoria CBD",   None, 0, 1, 0, 25, 3),
    "Soshanguve Rank":     ("Soshanguve - Pretoria CBD",     4, 1, 5, 2, 130, 6),
    "Atteridgeville Rank": ("Atteridgeville - Pretoria CBD", 3, 1, 2, 0, 60, 5),
    "Mabopane Station":    ("Mabopane - Pretoria CBD",       5, 2, 3, 3, 70, 5),
    "Hammanskraal Rank":   ("Hammanskraal - Pretoria CBD",   8, 2, 6, 2, 150, 4),
}

print("LIVE STOPS")
for name, (route, km, ahead, pins, gps, _, _) in stops.items():
    eta = "No GPS" if km is None else f"{m.eta_minutes(km, 30, ahead)} min"
    print(f"  {name} | {route} | {eta} | confidence {m.confidence_score(pins, gps)}")

print("DEMAND")
for name, (*_, waiting, taxis) in stops.items():
    level = m.demand_level(m.demand_intensity(waiting, taxis))
    print(f"  {name}: waiting {waiting}, taxis {taxis}, intensity {m.demand_intensity(waiting, taxis)} = {level}")
print("Deploy 20 spare taxis:", m.deploy_taxis({s: v[5:] for s, v in stops.items()}, 20))
print("Expected wait (20 min headway):", m.expected_wait(20), "min")
print("Occupancy percentage (12 of 15):", m.occupancy_percentage(12), "%")
print("Forecast next hour:", m.forecast_demand([700, 760, 820, 840]), "passengers")
