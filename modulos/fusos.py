import streamlit as st


def calcular_fuso_utm(longitude: float) -> int:
    """Calcula o fuso UTM convencional (1 a 60) a partir da longitude."""
    if not -180 <= longitude <= 180:
        raise ValueError("A longitude deve estar entre -180° e 180°.")
    # A longitude 180° pertence ao fuso 60.
    return min(60, int((longitude + 180) // 6) + 1)


def mostrar_calculo_fuso():
    st.subheader("Cálculo do fuso UTM")
    longitude = st.number_input(
        "Longitude (graus)",
        min_value=-180.0,
        max_value=180.0,
        value=0.0,
        format="%.8f",
        key="longitude_fuso",
    )

    if st.button("Determinar fuso", key="botao_determinar_fuso"):
        fuso = calcular_fuso_utm(longitude)
        meridiano_central = fuso * 6 - 183
        st.success(f"Fuso UTM: {fuso}")
        st.write(f"Meridiano central: {meridiano_central}°")
        st.caption(
            "Nota: esta é a regra convencional de fuso por longitude. "
            "Existem zonas especiais em algumas regiões; podem ser acrescentadas depois."
        )
