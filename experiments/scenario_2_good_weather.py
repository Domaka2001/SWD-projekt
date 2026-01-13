"""
Scenariusz 2:
Dobra pogoda i niski ruch.
"""

from src.inference.decision_engine import solve_decision

if __name__ == "__main__":
    evidence = {
        "Pogoda": "Dobra",
        "Natężenie_ruchu": "Niskie"
    }

    decision, eu = solve_decision(evidence)

    print("SCENARIUSZ: Dobra pogoda + niski ruch")
    print("Rekomendowana decyzja:", decision)
    print("Oczekiwana użyteczność:", eu)
