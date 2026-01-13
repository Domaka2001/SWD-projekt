"""
Scenariusz 3:
Brak informacji o pogodzie, preferencja niskiego kosztu
(wynik pośredni – decyzja w warunkach niepełnej informacji).
"""

from src.inference.decision_engine import solve_decision

if __name__ == "__main__":
    evidence = {}

    decision, eu = solve_decision(evidence)

    print("SCENARIUSZ: Brak obserwacji")
    print("Rekomendowana decyzja:", decision)
    print("Oczekiwana użyteczność:", eu)
