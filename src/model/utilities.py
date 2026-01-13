"""
utilities.py

Definicja funkcji użyteczności zgodna z API PySMILE.
"""

def set_utility(net):
    node = "Użyteczność"

    # SMILE mówi, ile wartości potrzeba
    required_size = len(net.get_node_definition(node))

    # Bazowa skala użyteczności (neutralna, rosnąca)
    base_utility = [0, 25, 50, 75, 100]

    utility = []
    i = 0
    while len(utility) < required_size:
        utility.append(base_utility[i % len(base_utility)])
        i += 1

    net.set_node_definition(node, utility)
