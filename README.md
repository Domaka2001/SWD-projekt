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

- Streamlit (Interfejs użytkownika)

- Pandas / Matplotlib (Wizualizacja danych)

- GeNIe Modeler (opcjonalnie, GUI)



---



## Uruchomienie



### 1. Instalacja bibliotek

Wymagana jest instalacja biblioteki PySMILE z serwera producenta oraz pozostałych zależności:



```bash

pip install --index-url https://support.bayesfusion.com/pysmile-A/ pysmile

pip install streamlit pandas matplotlib

```



### 2. Aplikacja Interaktywna (Streamlit)

Najwygodniejszym sposobem korzystania z systemu jest aplikacja webowa:



```bash

streamlit run app.py

```



### 3. Scenariusze testowe (CLI)

Możesz również uruchomić gotowe scenariusze eksperymentalne:



```bash

python -m experiments.scenario_1_bad_weather

```
