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
    if not utilities:
        return None, 0.0, {}

    best_choice_index = utilities.index(max(utilities))
    best_choice_name = decision_options[best_choice_index]
    max_utility = utilities[best_choice_index]

    all_utilities = {}
    print("--- Wyniki Wnioskowania ---")
    for i, option in enumerate(decision_options):
        print(f"Opcja: {option}, Oczekiwana użyteczność: {utilities[i]:.2f}")
        all_utilities[option] = utilities[i]
    
    print(f"\nNajlepsza decyzja: {best_choice_name} (Użyteczność: {max_utility:.2f})")

    return best_choice_name, max_utility, all_utilities


def solve_decision(evidence_dict, weights=None):
    """
    Buduje sieć, ustawia dowody i rozwiązuje problem najlepszej decyzji.
    :param evidence_dict: Słownik, gdzie klucze to ID węzłów, a wartości to ID wyników (stany tekstowe).
    :param weights: Słownik wag dla kryteriów (opcjonalny).
    :return: Krotka (nazwa_najlepszej_decyzji, maksymalna_użyteczność, słownik_wszystkich_wyników).
    """
    # 1. Buduj kompletną sieć decyzyjną z uwzględnieniem wag
    net = build_decision_network(weights)

    # 2. Set all evidence provided in the dictionary
    for node, evidence in evidence_dict.items():
        net.set_evidence(node, evidence)
    
    # 3. Run inference and get the result
    best_decision, max_utility, all_utilities = run_inference(net)
    net.clear_all_evidence() # Clear evidence after inference for potential re-use or other scenarios
    return best_decision, max_utility, all_utilities
