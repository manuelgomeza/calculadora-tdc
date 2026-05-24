import streamlit as st
import pandas as pd

st.title("Gestor de TDC - Control de Gastos")

if 'movimientos' not in st.session_state:
    st.session_state.movimientos = []

# Formulario de entrada
with st.form("registro_gastos"):
    col1, col2 = st.columns(2)
    descripcion = col1.text_input("Concepto del consumo")
    monto_bs = col1.number_input("Monto en Bs", min_value=0.0, step=1.0)
    tasa_dia = col2.number_input("Tasa BCV del día", min_value=1.0, value=523.67)
    
    if st.form_submit_button("Registrar"):
        monto_usd = monto_bs / tasa_dia
        st.session_state.movimientos.append({
            "Concepto": descripcion,
            "Monto Bs": monto_bs,
            "Monto USD": monto_usd,
            "Tasa Usada": tasa_dia
        })

if st.session_state.movimientos:
    df = pd.DataFrame(st.session_state.movimientos)
    st.write("### Tus movimientos:")
    st.table(df)

    # Botón para descargar a Excel/CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Descargar movimientos a Excel (CSV)",
        data=csv,
        file_name='mis_consumos_tdc.csv',
        mime='text/csv',
    )

    # Cálculos
    total_bs = df["Monto Bs"].sum()
    total_usd = df["Monto USD"].sum()
    interes_total = total_bs * 0.60 * (6/12)
    cuota_mensual = (total_bs + interes_total) / 6
    
    st.subheader("Resumen Financiero")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Deuda (Bs)", f"{total_bs:,.2f}")
    c2.metric("Total Deuda (USD)", f"{total_usd:,.2f}")
    c3.metric("Cuota Mensual (6 meses)", f"{cuota_mensual:,.2f}")
    
    if st.button("Limpiar todo"):
        st.session_state.movimientos = []
        st.rerun()
        import streamlit as st
import pandas as pd

# [Resto del código igual...]

    # Lógica de sugerencia
    st.subheader("💡 Sugerencia Financiera")
    if total_bs > 0:
        # Si el interés mensual es muy alto comparado con el pago mínimo, se recomienda pagar total
        if interes_mensual > (pago_minimo_est * 0.2):
            st.warning("⚠️ **Recomendación:** Pagar el total es altamente sugerido para evitar el impacto acumulado del 60% anual en intereses.")
        else:
            st.info("ℹ️ **Nota:** Si tienes liquidez, pagar el total siempre será más eficiente para tu bolsillo.")
    
    # ...[Fin del código]
