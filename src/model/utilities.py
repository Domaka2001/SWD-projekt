"""
utilities.py

Definiuje ostateczną funkcję użyteczności dla sieci.
"""
from . import variables

def set_utility_table(net, weights=None):
    """
    Defines the utility table for the final UTILITY node based on the states
    of its parent criteria nodes (TIME, COST, COMFORT) and user-provided weights.
    """
    if weights is None:
        weights = {
            variables.TIME: 1.0,
            variables.COST: 1.0,
            variables.COMFORT: 1.0
        }

    # 1. Define base utility scores for each state of the criteria.
    time_scores = { "Krótki": 100, "Średni": 50, "Długi": 0 }
    cost_scores = { "Niski": 100, "Średni": 50, "Wysoki": 0 }
    comfort_scores = { "Wysoki": 100, "Średni": 50, "Niski": 0 }

    # 2. Get the states in the order SMILE expects them.
    # The order of parents is determined by add_arc calls in structure.py.
    # The table is a flattened array where the last parent's outcomes vary fastest.
    # Assumed parent order for UTILITY node: TIME, COST, COMFORT
    # Therefore, the CPT changes fastest for COMFORT, then COST, then TIME.
    
    time_states = net.get_outcome_ids(variables.TIME)
    cost_states = net.get_outcome_ids(variables.COST)
    comfort_states = net.get_outcome_ids(variables.COMFORT)

    utility_table = []
    
    # Iterate through all combinations in the correct order to build the flattened array.
    for time_state in time_states:
        for cost_state in cost_states:
            for comfort_state in comfort_states:
                # Weighted additive utility function
                total_utility = (
                    time_scores.get(time_state, 0) * weights.get(variables.TIME, 1.0) +
                    cost_scores.get(cost_state, 0) * weights.get(variables.COST, 1.0) +
                    comfort_scores.get(comfort_state, 0) * weights.get(variables.COMFORT, 1.0)
                )
                utility_table.append(total_utility)
    
    # The utility table should have 3 * 3 * 3 = 27 entries.
    net.set_node_definition(variables.UTILITY, utility_table)
    
    print("Final utility table defined on UTILITY node.")
