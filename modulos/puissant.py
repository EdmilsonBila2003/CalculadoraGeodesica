import streamlit as st


def mostrar_puissant(tipo: str):
    titulo = "Problema geodésico directo — Puissant" if tipo == "directo" else "Problema geodésico inverso — Puissant"
    st.subheader(titulo)

    if tipo == "directo":
        col1, col2 = st.columns(2)
        with col1:
            st.number_input("Latitude inicial (graus)", min_value=-90.0, max_value=90.0, value=0.0, key="puissant_dir_lat")
            st.number_input("Longitude inicial (graus)", min_value=-180.0, max_value=180.0, value=0.0, key="puissant_dir_lon")
        with col2:
            st.number_input("Azimute inicial (graus)", value=0.0, key="puissant_dir_az")
            st.number_input("Distância (m)", min_value=0.0, value=0.0, key="puissant_dir_dist")
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.number_input("Latitude do ponto 1 (graus)", min_value=-90.0, max_value=90.0, value=0.0, key="puissant_inv_lat1")
            st.number_input("Longitude do ponto 1 (graus)", min_value=-180.0, max_value=180.0, value=0.0, key="puissant_inv_lon1")
        with col2:
            st.number_input("Latitude do ponto 2 (graus)", min_value=-90.0, max_value=90.0, value=0.0, key="puissant_inv_lat2")
            st.number_input("Longitude do ponto 2 (graus)", min_value=-180.0, max_value=180.0, value=0.0, key="puissant_inv_lon2")

    st.info(
        "Os campos estão prontos. A fórmula de Puissant será adicionada "
        "quando forneceres a versão exacta que pretendes utilizar."
    )
    st.button("Calcular", disabled=True, key=f"puissant_{tipo}_calcular")
