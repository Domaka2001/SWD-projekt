"""
decision_engine.py

Moduł realizujący wnioskowanie decyzyjne
(maksymalizacja oczekiwanej użyteczności).
"""

import pysmile
from src.model.variables import DECISION_TRANSPORT, UTILITY
from src.model.build_network import build_decision_network


def run_inference(net):
    """
    Uruchamia wnioskowanie i zwraca najlepszą decyzję.
    Sieć musi mieć ustawione dowody.
    """
    # Aktualizacja sieci, aby odzwierciedlić dowody i obliczyć oczekiwane użyteczności
    net.update_beliefs()

    # Pobranie wyników dla węzła decyzyjnego
    decision_node_id = net.get_node(DECISION_TRANSPORT)
    # pysmile.Network.get_node_value dla węzłów decyzyjnych zwraca listę oczekiwanych użyteczności
    # dla każdego wyniku węzła decyzyjnego, w kolejności ich zdefiniowania.
    utilities = net.get_node_value(decision_node_id)
    
    # Pobranie nazw opcji decyzyjnych
    decision_options = net.get_outcome_ids(DECISION_TRANSPORT)

    # Znalezienie najlepszej decyzji
    if not utilities: # Obsługa przypadku, gdy nie znaleziono użyteczności, choć mało prawdopodobne dla dobrze sformułowanego ID
        return None, 0.0

    best_choice_index = utilities.index(max(utilities))
    best_choice_name = decision_options[best_choice_index]
    max_utility = utilities[best_choice_index]

    print("--- Wyniki Wnioskowania ---")
    for i, option in enumerate(decision_options):
        print(f"Opcja: {option}, Oczekiwana użyteczność: {utilities[i]:.2f}")
    
    print(f"\nNajlepsza decyzja: {best_choice_name} (Użyteczność: {max_utility:.2f})")

    return best_choice_name, max_utility


def solve_decision(evidence_dict):
    """
    Builds the network, sets evidence, and solves for the best decision.
    :param evidence_dict: A dictionary where keys are node IDs and values are outcome IDs (string states).
    :return: A tuple of (best_decision_name, max_utility).
    """
    # 1. Build the complete decision network
    net = build_decision_network()

    # 2. Set all evidence provided in the dictionary
    for node, evidence in evidence_dict.items():
        net.set_evidence(node, evidence)
    
    # 3. Run inference and get the result
    best_decision, max_utility = run_inference(net)
    net.clear_all_evidence() # Clear evidence after inference for potential re-use or other scenarios
    return best_decision, max_utility
