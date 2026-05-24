import streamlit as st
import pandas as pd

st.title("Gestor de TDC - Control de Gastos")

# Inicializar historial
if 'movimientos' not in st.session_state:
    st.session_state.movimientos = []

# Formulario
with st.form("registro"):
    col1, col2 = st.columns(2)
    concepto = col1.text_input("Concepto")
    monto = col1.number_input("Monto", min_value=0.0)
    moneda = col2.selectbox("Moneda", ["Bs", "USD"])
    tasa = col2.number_input("Tasa BCV del día", min_value=1.0, value=36.0)
    
    if st.form_submit_button("Registrar"):
        monto_bs = monto if moneda == "Bs" else monto * tasa
        st.session_state.movimientos.append({
            "Concepto": concepto,
            "Monto Bs": monto_bs,
            "Moneda": moneda
        })

# Lógica de totales
if st.session_state.movimientos:
    df = pd.DataFrame(st.session_state.movimientos)
    st.table(df)
    
    total_deuda = df["Monto Bs"].sum()
    interes_mensual = (total_deuda * 0.60) / 12
    pago_minimo = (total_deuda * 0.15) # Estimación: 15% del total
    
    st.subheader("Resumen Financiero")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Deuda (Bs)", f"{total_deuda:,.2f}")
    c2.metric("Interés Mensual", f"{interes_mensual:,.2f}")
    c3.metric("Pago Mínimo Est.", f"{pago_minimo:,.2f}")
    
    if st.button("Limpiar todo"):
        st.session_state.movimientos = []
        st.rerun()
