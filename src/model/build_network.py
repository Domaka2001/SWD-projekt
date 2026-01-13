"""
build_network.py

Budowa kompletnej sieci decyzyjnej.
"""

import pysmile
import pysmile_license

from .variables import *
from .structure import add_structure
from .probabilities import (
    set_conditional_probabilities,
)
from .utilities import set_utility


def build_network():
    net = pysmile.Network()

    # 1. Węzły losowe
    for node, states in {
        TIME: ["Krótki", "Średni", "Długi"],
        COST: ["Niski", "Średni", "Wysoki"],
        COMFORT: ["Niski", "Średni", "Wysoki"],
    }.items():
        n = net.add_node(pysmile.NodeType.CPT, node)
        for s in states:
            net.add_outcome(n, s)

    # 2. Decyzja
    d = net.add_node(pysmile.NodeType.DECISION, DECISION_TRANSPORT)
    for s in TRANSPORT_OPTIONS:
        net.add_outcome(d, s)

    # 3. Utility
    net.add_node(pysmile.NodeType.UTILITY, UTILITY)

    # 4. STRUKTURA
    add_structure(net)

    # 5. CPT – DOPIERO TERAZ
    set_conditional_probabilities(net)

    # 6. Utility
    set_utility(net)

    return net
