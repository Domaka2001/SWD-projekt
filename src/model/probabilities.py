"""
probabilities.py

Specyfikacja probabilistyczna zgodna z dokumentacją SMILE
dla diagramów decyzyjnych.
"""

def _set_uniform_cpt(net, node_name, base_dist):
    """
    Ustawia CPT o dokładnie takim rozmiarze,
    jakiego oczekuje SMILE.
    """
    required_size = len(net.get_node_definition(node_name))
    cpt = []
    i = 0
    while len(cpt) < required_size:
        cpt.append(base_dist[i % len(base_dist)])
        i += 1
    net.set_node_definition(node_name, cpt)


def set_conditional_probabilities(net):
    # Czas podróży (3 stany)
    _set_uniform_cpt(net, "Czas_podróży", [0.4, 0.4, 0.2])

    # Koszt (3 stany)
    _set_uniform_cpt(net, "Koszt", [0.3, 0.4, 0.3])

    # Komfort (3 stany)
    _set_uniform_cpt(net, "Komfort", [0.3, 0.4, 0.3])
