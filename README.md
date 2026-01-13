# Inteligentny Asystent Dojazdu  
System Wspomagania Decyzji (SWD)

## Opis projektu
Projekt przedstawia system wspomagania decyzji o nazwie **Inteligentny Asystent Dojazdu**,
którego celem jest rekomendacja najbardziej satysfakcjonującego środka transportu
w warunkach niepewności.

System został zaprojektowany zgodnie z zasadami **teorii decyzji** i wykorzystuje
**sieć decyzyjną (Influence Diagram)** zaimplementowaną przy użyciu biblioteki **SMILE / PySMILE**.

Decyzja podejmowana jest na podstawie:
- warunków pogodowych,
- natężenia ruchu,
- jakości komunikacji miejskiej,
- kryteriów: czasu podróży, kosztu i komfortu.

Rekomendacja opiera się na **maksymalizacji oczekiwanej użyteczności**.

---

## Struktura projektu

InteligentnyAsystentDojazdu/
* models/ # modele .xdsl i wersja pythonowa
* src/ # implementacja logiki SWD
* experiments/ # scenariusze decyzyjne
* docs/ # dokumentacja projektowa
* README.md
---

## Technologie
- Python 3.10+
- PySMILE (SMILE)
- GeNIe Modeler (opcjonalnie, GUI)

---

## Uruchomienie przykładowego scenariusza

```bash
 python -m pip install --index-url https://support.bayesfusion.com/pysmile-A/ pysmile
python -m experiments.scenario_1_bad_weather