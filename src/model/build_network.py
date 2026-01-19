"""
build_network.py

Budowa kompletnej sieci decyzyjnej.
"""
import pysmile_license
import pysmile

from . import variables
from .structure import add_structure
from .probabilities import set_conditional_probabilities
from .utilities import set_utility_table

def create_node_with_outcomes(net, node_type, node_id, outcomes):
    """
    Creates a node, renaming default outcomes and adding new ones as needed,
    exactly as shown in the SMILE documentation tutorial.
    """
    handle = net.add_node(node_type, node_id)
    
    if outcomes: # Utility nodes might not have outcomes
        initial_outcome_count = net.get_outcome_count(handle)
        
        # Rename existing default outcomes
        for i in range(initial_outcome_count):
            if i < len(outcomes):
                net.set_outcome_id(handle, i, outcomes[i])
        
        # Add new outcomes if required
        for i in range(initial_outcome_count, len(outcomes)):
            net.add_outcome(handle, outcomes[i])
            
    return handle

def build_decision_network(weights=None):
    net = pysmile.Network()
    print("Building network (method from documentation)...")

    # 1. Create Nodes using the documentation's method
    create_node_with_outcomes(net, pysmile.NodeType.CPT, variables.WEATHER, variables.WEATHER_STATES)
    create_node_with_outcomes(net, pysmile.NodeType.CPT, variables.TRAFFIC, variables.TRAFFIC_STATES)
    create_node_with_outcomes(net, pysmile.NodeType.CPT, variables.PUBLIC_TRANSPORT, variables.PUBLIC_TRANSPORT_STATES)
    create_node_with_outcomes(net, pysmile.NodeType.CPT, variables.TIME, variables.CRITERIA_STATES)
    create_node_with_outcomes(net, pysmile.NodeType.CPT, variables.COST, variables.COST_STATES)
    create_node_with_outcomes(net, pysmile.NodeType.CPT, variables.COMFORT, variables.COMFORT_STATES)
    create_node_with_outcomes(net, pysmile.NodeType.DECISION, variables.DECISION_TRANSPORT, variables.TRANSPORT_OPTIONS)
    
    # Utility node has no outcomes and is created differently
    net.add_node(pysmile.NodeType.UTILITY, variables.UTILITY)
    
    print("All nodes created.")

    # 2. Add Arcs (Structure)
    add_structure(net)
    print("Structure added.")

    # 3. Set Probabilities (CPTs)
    set_conditional_probabilities(net)
    print("Probabilities set.")

    # 4. Set Utilities
    set_utility_table(net, weights)
    print("Utilities set.")

    print("Decision network built successfully.")
    return net
