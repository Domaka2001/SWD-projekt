"""
Scenariusz 1:
Zła pogoda.
"""
from src.inference.decision_engine import solve_decision
from src.model.variables import WEATHER

def scenario_bad_weather():
    print("--- SCENARIUSZ: ZŁA POGODA ---")
    
    evidence = {
        WEATHER: "Zła"
    }
    
    decision, eu, _ = solve_decision(evidence)

    print(f"\nNajlepsza decyzja w warunkach złej pogody: {decision}")
    print(f"Oczekiwana użyteczność: {eu:.2f}")

if __name__ == "__main__":
    scenario_bad_weather()
