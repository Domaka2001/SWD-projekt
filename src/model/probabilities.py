"""
probabilities.py

Specyfikacja probabilistyczna zgodna z dokumentacją SMILE
dla diagramów decyzyjnych.
"""

from .variables import (
    DECISION_TRANSPORT, TRANSPORT_OPTIONS,
    WEATHER, WEATHER_STATES,
    TRAFFIC, TRAFFIC_STATES,
    PUBLIC_TRANSPORT, PUBLIC_TRANSPORT_STATES,
    TIME, CRITERIA_STATES,
    COST, COST_STATES,
    COMFORT, COMFORT_STATES
)

def set_conditional_probabilities(net):
    # CPT for WEATHER (Prior distribution)
    # States: ["Dobra", "Zła"]
    net.set_node_definition(WEATHER, [0.7, 0.3]) # 70% Dobra, 30% Zła

    # CPT for PUBLIC_TRANSPORT (Prior distribution)
    # States: ["Dobra", "Zła"]
    net.set_node_definition(PUBLIC_TRANSPORT, [0.8, 0.2]) # 80% Dobra, 20% Zła

    # CPT for TRAFFIC (Parent: WEATHER)
    # States: ["Niskie", "Wysokie"]
    # Parent states (WEATHER): ["Dobra", "Zła"]
    # Order: P(T=N|W=D), P(T=W|W=D), P(T=N|W=Z), P(T=W|W=Z)
    net.set_node_definition(TRAFFIC, [
        0.8, 0.2, # If Weather = Dobra, Traffic is Niskie (0.8), Wysokie (0.2)
        0.3, 0.7  # If Weather = Zła, Traffic is Niskie (0.3), Wysokie (0.7)
    ])

    # CPT for COST (Parent: DECISION_TRANSPORT)
    # States: ["Niski", "Średni", "Wysoki"]
    # Parent states (DECISION_TRANSPORT): ["Samochód", "Komunikacja", "Rower", "Pieszo"]
    # Order for CPT values corresponds to parent state order, then child state order.
    net.set_node_definition(COST, [
        # Samochód
        0.1, 0.4, 0.5,
        # Komunikacja
        0.4, 0.5, 0.1,
        # Rower
        0.8, 0.2, 0.0,
        # Pieszo
        0.9, 0.1, 0.0
    ])

    # CPT for COMFORT (Parents: DECISION_TRANSPORT, WEATHER)
    # States: ["Niski", "Średni", "Wysoki"]
    # Parent states order: DECISION_TRANSPORT (4 states), WEATHER (2 states)
    # Total combinations: 4 * 2 = 8
    # Order: DECISION_TRANSPORT then WEATHER, then COMFORT states
    net.set_node_definition(COMFORT, [
        # Samochód | Dobra
        0.0, 0.2, 0.8,
        # Samochód | Zła
        0.1, 0.4, 0.5,
        # Komunikacja | Dobra
        0.1, 0.6, 0.3,
        # Komunikacja | Zła
        0.3, 0.5, 0.2,
        # Rower | Dobra
        0.1, 0.3, 0.6,
        # Rower | Zła (rain/snow makes it low comfort)
        0.8, 0.2, 0.0,
        # Pieszo | Dobra
        0.1, 0.3, 0.6,
        # Pieszo | Zła (rain/snow makes it low comfort)
        0.8, 0.2, 0.0
    ])

    # CPT for TIME (Parents: DECISION_TRANSPORT, TRAFFIC, PUBLIC_TRANSPORT)
    # States: ["Krótki", "Średni", "Długi"]
    # Parent states order: DECISION_TRANSPORT (4), TRAFFIC (2), PUBLIC_TRANSPORT (2)
    # Total combinations: 4 * 2 * 2 = 16
    # Each combination has 3 states for TIME. Total values: 16 * 3 = 48
    net.set_node_definition(TIME, [
        # DECISION_TRANSPORT: Samochód
            # TRAFFIC: Niskie
                # PUBLIC_TRANSPORT: Dobra (Car, Low Traffic, Good PT Punctuality)
                0.8, 0.2, 0.0,
                # PUBLIC_TRANSPORT: Zła
                0.7, 0.3, 0.0,
            # TRAFFIC: Wysokie
                # PUBLIC_TRANSPORT: Dobra
                0.2, 0.6, 0.2,
                # PUBLIC_TRANSPORT: Zła
                0.1, 0.5, 0.4,
        # DECISION_TRANSPORT: Komunikacja
            # TRAFFIC: Niskie
                # PUBLIC_TRANSPORT: Dobra
                0.2, 0.7, 0.1,
                # PUBLIC_TRANSPORT: Zła
                0.1, 0.5, 0.4,
            # TRAFFIC: Wysokie
                # PUBLIC_TRANSPORT: Dobra
                0.1, 0.7, 0.2,
                # PUBLIC_TRANSPORT: Zła
                0.0, 0.4, 0.6,
        # DECISION_TRANSPORT: Rower
            # TRAFFIC: Niskie
                # PUBLIC_TRANSPORT: Dobra
                0.3, 0.6, 0.1,
                # PUBLIC_TRANSPORT: Zła
                0.3, 0.6, 0.1, # PT punctuality less relevant for bike
            # TRAFFIC: Wysokie
                # PUBLIC_TRANSPORT: Dobra
                0.2, 0.6, 0.2,
                # PUBLIC_TRANSPORT: Zła
                0.2, 0.6, 0.2,
        # DECISION_TRANSPORT: Pieszo
            # TRAFFIC: Niskie
                # PUBLIC_TRANSPORT: Dobra
                0.1, 0.6, 0.3,
                # PUBLIC_TRANSPORT: Zła
                0.1, 0.6, 0.3, # PT punctuality less relevant for walk
            # TRAFFIC: Wysokie
                # PUBLIC_TRANSPORT: Dobra
                0.1, 0.5, 0.4,
                # PUBLIC_TRANSPORT: Zła
                0.1, 0.5, 0.4,
    ])

    print("Conditional probabilities defined.")
