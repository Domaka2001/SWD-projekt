"""
decision_engine.py

Moduł realizujący wnioskowanie decyzyjne
(maksymalizacja oczekiwanej użyteczności).
"""

from src.model.build_network import build_network
from src.model.variables import DECISION_TRANSPORT

def solve_decision(evidence):
    net = build_network()

    print("\n=== NODES IN NETWORK ===")
    for h in net.get_all_nodes():
        print(net.get_node_name(h), "| type:", net.get_node_type(h))

    best_decision = None
    best_eu = float("-inf")

    decision_node = DECISION_TRANSPORT
    decision_outcomes = net.get_outcome_ids(decision_node)

    for d in decision_outcomes:
        # Wyczyść evidence
        net.clear_all_evidence()

        # Ustaw decyzję (policy)
        net.set_evidence(decision_node, d)

        # Evidence losowe (jeśli są)
        for node, value in evidence.items():
            net.set_evidence(node, value)

        net.update_beliefs()

        # ODCZYT OCZEKIWANEJ UŻYTECZNOŚCI
        eu = net.get_node_value("Użyteczność")[0]


        print(f"Decyzja = {d}, EU = {eu}")

        if eu > best_eu:
            best_eu = eu
            best_decision = d

    return best_decision, best_eu


