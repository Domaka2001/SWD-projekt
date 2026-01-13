"""
structure.py

Definicja struktury sieci decyzyjnej (Influence Diagram).
"""

from .variables import *

def add_structure(net):
    """
    Dodaje łuki do sieci zgodnie z projektem decyzyjnym.
    """

    net.add_arc(DECISION_TRANSPORT, TIME)
    net.add_arc(DECISION_TRANSPORT, COST)
    net.add_arc(DECISION_TRANSPORT, COMFORT)

    net.add_arc(TIME, UTILITY)
    net.add_arc(COST, UTILITY)
    net.add_arc(COMFORT, UTILITY)
