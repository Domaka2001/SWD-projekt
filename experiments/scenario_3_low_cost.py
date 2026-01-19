"""
Scenariusz 3:
Brak obserwacji (inferencja bez początkowych dowodów).
"""
from src.inference.decision_engine import solve_decision
from src.model.variables import WEATHER, PUBLIC_TRANSPORT # Import for potential future use in scenarios

def scenario_no_observations():
    print("--- SCENARIUSZ: Brak obserwacji ---")

    # W tym scenariuszu nie ustawiamy żadnych początkowych dowodów.
    # System podejmie decyzję bazując tylko na rozkładach a priori.
    evidence = {} 
    
    decision, eu, _ = solve_decision(evidence)

    print(f"\nNajlepsza decyzja (bez obserwacji): {decision}")
    print(f"Oczekiwana użyteczność: {eu:.2f}")

if __name__ == "__main__":
    scenario_no_observations()
