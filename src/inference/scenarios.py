"""
scenarios.py

Zdefiniowane scenariusze decyzyjne.
"""

SCENARIOS = {
    "zla_pogoda_duzy_ruch": {
        "Pogoda": "Zła",
        "Natężenie_ruchu": "Wysokie"
    },
    "dobra_pogoda_maly_ruch": {
        "Pogoda": "Dobra",
        "Natężenie_ruchu": "Niskie"
    },
    "idealna_komunikacja": {
        "Punktualność_KM": "Dobra",
        "Natężenie_ruchu": "Wysokie"
    }
}
