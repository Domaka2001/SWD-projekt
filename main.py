import pysmile_license
import pysmile
from src.inference.decision_engine import solve_decision
from src.model import variables

def get_user_weights():
    print("\n" + "="*40)
    print(" 1. KONFIGURACJA PREFERENCJI")
    print("="*40)
    print("Oceń ważność poniższych kryteriów w skali od 0 do 5\n(0 - nieistotne, 5 - kluczowe):")
    
    def ask_weight(label):
        while True:
            try:
                val = input(f" -> {label}: ")
                f_val = float(val)
                if 0 <= f_val <= 5:
                    return f_val
                print("Proszę podać liczbę z zakresu 0-5.")
            except ValueError:
                print("To nie jest poprawna liczba.")

    w_time = ask_weight(variables.TIME)
    w_cost = ask_weight(variables.COST)
    w_comfort = ask_weight(variables.COMFORT)
    
    return {
        variables.TIME: w_time,
        variables.COST: w_cost,
        variables.COMFORT: w_comfort
    }

def get_external_conditions():
    print("\n" + "="*40)
    print(" 2. OKREŚLANIE WARUNKÓW ZEWNĘTRZNYCH")
    print("="*40)
    evidence = {}

    def ask_condition(label, states):
        print(f"\nJaki/jaka jest dzisiaj {label}?")
        for i, state in enumerate(states):
            print(f"  {i+1}. {state}")
        print(f"  {len(states)+1}. Nie wiem / Losowo")
        
        while True:
            choice = input(" Wybór: ")
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(states):
                    return states[idx-1]
                if idx == len(states) + 1:
                    return None
            print(f"Wybierz numer od 1 do {len(states)+1}.")

    # Pogoda
    cond_weather = ask_condition(variables.WEATHER, variables.WEATHER_STATES)
    if cond_weather: evidence[variables.WEATHER] = cond_weather

    # Natężenie ruchu
    cond_traffic = ask_condition(variables.TRAFFIC, variables.TRAFFIC_STATES)
    if cond_traffic: evidence[variables.TRAFFIC] = cond_traffic

    # Punktualność komunikacji
    cond_pt = ask_condition(variables.PUBLIC_TRANSPORT, variables.PUBLIC_TRANSPORT_STATES)
    if cond_pt: evidence[variables.PUBLIC_TRANSPORT] = cond_pt

    return evidence

def main():
    print("========================================")
    print("   INTELIGENTNY ASYSTENT DOJAZDU")
    print("========================================")
    print("Witaj! Pomogę Ci wybrać optymalny środek transportu.")
    
    weights = get_user_weights()
    evidence = get_external_conditions()
    
    print("\n" + "-"*40)
    print("Analizuję dane i obliczam użyteczność...")
    print("-"*40)
    
        print("\nUruchamiam wnioskowanie...")
        decision, utility, _ = solve_decision(evidence, weights)
        
        print("\n" + "="*40)        print(f" REKOMENDACJA: {decision.upper()}")
        print(f" Szacowany poziom Twojej satysfakcji: {utility:.2f} pkt")
        print("!"*40 + "\n")
    except Exception as e:
        print(f"\nWystąpił nieoczekiwany błąd podczas obliczeń: {e}")

if __name__ == "__main__":
    main()
