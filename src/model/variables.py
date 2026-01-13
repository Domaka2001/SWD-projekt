"""
variables.py

Definicje zmiennych decyzyjnych, losowych i kryterialnych
dla systemu Inteligentny Asystent Dojazdu.
"""

# Węzeł decyzyjny
DECISION_TRANSPORT = "Środek_transportu"
TRANSPORT_OPTIONS = [
    "Samochód",
    "Komunikacja",
    "Rower",
    "Pieszo"
]

# Węzły losowe (niepewność)
WEATHER = "Pogoda"
WEATHER_STATES = ["Dobra", "Zła"]

TRAFFIC = "Natężenie_ruchu"
TRAFFIC_STATES = ["Niskie", "Wysokie"]

PUBLIC_TRANSPORT = "Punktualność_KM"
PUBLIC_TRANSPORT_STATES = ["Dobra", "Zła"]

# Węzły kryterialne
TIME = "Czas_podróży"
COST = "Koszt"
COMFORT = "Komfort"

CRITERIA_STATES = ["Krótki", "Średni", "Długi"]
COST_STATES = ["Niski", "Średni", "Wysoki"]
COMFORT_STATES = ["Niski", "Średni", "Wysoki"]

# Węzeł użyteczności
UTILITY = "Użyteczność"
