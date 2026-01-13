"""
Scenariusz 2:
Dobra pogoda i niski ruch.
"""
from src.inference.decision_engine import solve_decision
from src.model.variables import WEATHER, TRAFFIC

def scenario_good_weather_low_traffic():
    print("--- SCENARIUSZ: Dobra pogoda + niski ruch ---")

    evidence = {
        WEATHER: "Dobra",
        TRAFFIC: "Niskie"
    }
    
    decision, eu = solve_decision(evidence)

    print(f"\nNajlepsza decyzja: {decision}")
    print(f"Oczekiwana użyteczność: {eu:.2f}")

if __name__ == "__main__":
    scenario_good_weather_low_traffic()
