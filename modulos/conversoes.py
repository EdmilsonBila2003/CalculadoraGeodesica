import math
import streamlit as st


def mostrar_conversoes():
    st.subheader("Conversão de graus e radianos")

    operacao = st.selectbox(
        "Tipo de conversão",
        ["Graus para radianos", "Radianos para graus"],
        key="conversao_angular_tipo",
    )
    valor = st.number_input(
        "Valor angular",
        value=0.0,
        format="%.10f",
        key="conversao_angular_valor",
    )

    if st.button("Converter", key="botao_conversao_angular"):
        if operacao == "Graus para radianos":
            resultado = math.radians(valor)
            st.success(f"Resultado: {resultado:.10f} rad")
            st.caption("Fórmula: radianos = graus × π / 180")
        else:
            resultado = math.degrees(valor)
            st.success(f"Resultado: {resultado:.10f}°")
            st.caption("Fórmula: graus = radianos × 180 / π")
