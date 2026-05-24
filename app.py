import streamlit as st

st.title("Calculadora de Intereses TDC")

# Entradas del usuario
monto = st.number_input("Monto de la deuda ($ o Bs):", min_value=0.0, step=10.0)
tasa_anual = st.number_input("Tasa de interés anual (%):", min_value=0.0, step=0.1)

if st.button("Calcular"):
    if monto > 0 and tasa_anual > 0:
        # Cálculos básicos
        tasa_mensual = (tasa_anual / 100) / 12
        interes_mensual = monto * tasa_mensual
        
        st.success(f"Tu interés estimado mensual es: {interes_mensual:,.2f}")
        st.info(f"Interés diario aproximado: {interes_mensual / 30:,.2f}")
    else:
        st.error("Por favor, ingresa montos y tasas válidas.")
