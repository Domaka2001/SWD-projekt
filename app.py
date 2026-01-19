import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.inference.decision_engine import solve_decision
from src.model import variables

# Page configuration
st.set_page_config(page_title="Inteligentny Asystent Dojazdu", layout="wide")

st.title("🚗 Inteligentny Asystent Dojazdu")
st.markdown("""
Ten system wspomagania decyzji pomoże Ci wybrać optymalny środek transportu 
na podstawie Twoich osobistych preferencji oraz aktualnych warunków zewnętrznych.
""")

# Sidebar for Preferences
st.sidebar.header("⚙️ Twoje Preferencje")
st.sidebar.info("Określ, jak ważne są dla Ciebie poszczególne kryteria (0-5).")

w_time = st.sidebar.slider(f"Waga: {variables.TIME}", 0.0, 5.0, 1.0, 0.5)
w_cost = st.sidebar.slider(f"Waga: {variables.COST}", 0.0, 5.0, 1.0, 0.5)
w_comfort = st.sidebar.slider(f"Waga: {variables.COMFORT}", 0.0, 5.0, 1.0, 0.5)

user_weights = {
    variables.TIME: w_time,
    variables.COST: w_cost,
    variables.COMFORT: w_comfort
}

# Main area for External Conditions
st.header("🌦️ Warunki Zewnętrzne")
col1, col2, col3 = st.columns(3)

with col1:
    weather = st.selectbox(f"Stan: {variables.WEATHER}", ["Losowo"] + variables.WEATHER_STATES)

with col2:
    traffic = st.selectbox(f"Stan: {variables.TRAFFIC}", ["Losowo"] + variables.TRAFFIC_STATES)

with col3:
    pt_punctuality = st.selectbox(f"Stan: {variables.PUBLIC_TRANSPORT}", ["Losowo"] + variables.PUBLIC_TRANSPORT_STATES)

# Prepare evidence dictionary
evidence = {}
if weather != "Losowo": evidence[variables.WEATHER] = weather
if traffic != "Losowo": evidence[variables.TRAFFIC] = traffic
if pt_punctuality != "Losowo": evidence[variables.PUBLIC_TRANSPORT] = pt_punctuality

# Decision Button
if st.button("🚀 Oblicz optymalny dojazd"):
    with st.spinner("Analizuję model decyzyjny..."):
        try:
            best_decision, max_utility, all_results = solve_decision(evidence, user_weights)
            
            # Calculate max possible utility for normalization
            # Each criterion has a max score of 100. Sum of (weight * 100)
            max_possible = sum(user_weights.values()) * 100
            
            # Avoid division by zero if all weights are 0
            if max_possible == 0: max_possible = 1 
            
            # Normalize results to 0-100 scale
            normalized_results = {k: (v / max_possible) * 100 for k, v in all_results.items()}
            norm_max_utility = (max_utility / max_possible) * 100

            # Display Results
            st.success(f"### Rekomendowany środek transportu: **{best_decision}**")
            st.metric("Oczekiwana Satysfakcja", f"{norm_max_utility:.1f}%")
            
            # Visualization
            st.subheader("📊 Porównanie opcji (skala procentowa)")
            
            # Prepare data for chart
            df = pd.DataFrame(list(normalized_results.items()), columns=['Środek transportu', 'Satysfakcja (%)'])
            df = df.sort_values(by='Satysfakcja (%)', ascending=False)
            
            # Plot
            fig, ax = plt.subplots()
            bars = ax.bar(df['Środek transportu'], df['Satysfakcja (%)'], 
                          color=['#FF4B4B' if x == best_decision else '#1C83E1' for x in df['Środek transportu']])
            ax.set_ylabel('Stopień realizacji preferencji (%)')
            ax.set_ylim(0, 105) # Always show 0-100 range
            ax.set_title('Przewidywana satysfakcja z dojazdu')
            
            # Add labels on top of bars
            for bar in bars:
                yval = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}%", ha='center', va='bottom')
            
            st.pyplot(fig)
            
            # Breakdown info
            st.info("""
            **Jak to czytać?** 
            Model oblicza prawdopodobieństwo wystąpienia różnych stanów kryteriów (Czas, Koszt, Komfort) 
            dla każdej opcji transportu, a następnie mnoży je przez Twoje wagi. 
            Wybierana jest opcja, która statystycznie daje najwyższą wartość.
            """)
            
        except Exception as e:
            st.error(f"Wystąpił błąd podczas obliczeń: {e}")

st.divider()
st.caption("Projekt Systemy Wspomagania Decyzji | Silnik: SMILE | Interfejs: Streamlit")
