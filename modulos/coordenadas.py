import streamlit as st


def mostrar_utm_geografico():
    st.subheader("Conversão de UTM para coordenadas geográficas")
    col1, col2 = st.columns(2)

    with col1:
        st.number_input("Este (E), em metros", value=500000.0, key="utm_e")
        st.number_input(
            "Fuso UTM", min_value=1, max_value=60, value=36, step=1, key="utm_fuso"
        )
    with col2:
        st.number_input("Norte (N), em metros", value=0.0, key="utm_n")
        st.selectbox("Hemisfério", ["Sul", "Norte"], key="utm_hemisferio")

    st.info(
        "Interface preparada. A transformação será implementada depois de "
        "definirmos o elipsoide e os parâmetros que serão utilizados."
    )


def mostrar_geografico_utm():
    st.subheader("Conversão de coordenadas geográficas para UTM")
    col1, col2 = st.columns(2)

    with col1:
        st.number_input(
            "Latitude (graus)", min_value=-90.0, max_value=90.0,
            value=0.0, format="%.8f", key="geo_latitude"
        )
    with col2:
        st.number_input(
            "Longitude (graus)", min_value=-180.0, max_value=180.0,
            value=0.0, format="%.8f", key="geo_longitude"
        )

    st.info(
        "Interface preparada. A transformação será implementada numa fase "
        "seguinte, com os parâmetros geodésicos definidos."
    )
