"""
sanity_checks.py

Podstawowe testy poprawności modelu decyzyjnego.
"""

from src.model.build_network import build_network


def check_model():
    net = build_network()

    # Sprawdzenie istnienia kluczowych węzłów
    required_nodes = [
        "Pogoda", "Natężenie_ruchu", "Środek_transportu",
        "Czas_podróży", "Koszt", "Komfort", "Użyteczność"
    ]

    for node in required_nodes:
        assert net.get_node(node) is not None, f"Brak węzła: {node}"

    print("✔ Wszystkie wymagane węzły istnieją.")


if __name__ == "__main__":
    check_model()
