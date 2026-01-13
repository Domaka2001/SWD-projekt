"""
Scenariusz 1:
Zła pogoda i wysokie natężenie ruchu.
"""

from src.inference.decision_engine import solve_decision
if __name__ == "__main__":
    evidence = {
        "Czas_podróży": "Długi"
    }

    decision, eu = solve_decision(evidence)

    print("Rekomendowana decyzja:", decision)
    print("Oczekiwana użyteczność:", eu)

