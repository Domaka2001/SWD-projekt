"""
structure.py

Definicja struktury sieci decyzyjnej (Influence Diagram).
"""

from . import variables

def add_structure(net):
    """
    Dodaje łuki do sieci zgodnie z projektem decyzyjnym.
    """

    net.add_arc(variables.DECISION_TRANSPORT, variables.TIME)
    net.add_arc(variables.DECISION_TRANSPORT, variables.COST)
    net.add_arc(variables.DECISION_TRANSPORT, variables.COMFORT)

    # Arcs from chance nodes to criteria
    net.add_arc(variables.WEATHER, variables.TRAFFIC)
    net.add_arc(variables.WEATHER, variables.COMFORT)
    net.add_arc(variables.TRAFFIC, variables.TIME)
    net.add_arc(variables.PUBLIC_TRANSPORT, variables.TIME)

    # Information arcs to Decision Node (observed before decision)
    net.add_arc(variables.WEATHER, variables.DECISION_TRANSPORT)
    net.add_arc(variables.TRAFFIC, variables.DECISION_TRANSPORT)
    net.add_arc(variables.PUBLIC_TRANSPORT, variables.DECISION_TRANSPORT)

    # Arcs from criteria to utility
    net.add_arc(variables.TIME, variables.UTILITY)
    net.add_arc(variables.COST, variables.UTILITY)
    net.add_arc(variables.COMFORT, variables.UTILITY)
