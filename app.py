import streamlit as st

from modulos.conversoes import mostrar_conversoes
from modulos.coordenadas import mostrar_utm_geografico, mostrar_geografico_utm
from modulos.puissant import mostrar_puissant
from modulos.sodano import mostrar_sodano
from modulos.fusos import mostrar_calculo_fuso

st.set_page_config(
    page_title="Calculadora Geodésica",
    page_icon="🌐",
    layout="wide",
)

st.title("🌐 Calculadora Geodésica")
st.caption("Ferramenta de apoio a conversões de coordenadas e cálculos geodésicos.")
st.divider()

pagina = st.sidebar.radio(
    "Menu principal",
    [
        "Página inicial",
        "Graus e radianos",
        "UTM para geográfico",
        "Geográfico para UTM",
        "Problema directo — Puissant",
        "Problema inverso — Puissant",
        "Problema directo — Sodano",
        "Problema inverso — Sodano",
        "Cálculo de fuso",
        "Sobre",
    ],
)

if pagina == "Página inicial":
    st.subheader("Bem-vindo à Calculadora Geodésica")
    st.write(
        "Escolha uma operação no menu lateral. Esta primeira versão contém "
        "a estrutura da interface; os métodos geodésicos e as conversões de "
        "coordenadas serão implementados quando forem definidas as fórmulas "
        "e os parâmetros de referência."
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("📐 **Conversões angulares**")
        st.write("Conversão entre graus e radianos.")
    with c2:
        st.info("📍 **Coordenadas**")
        st.write("Interfaces para coordenadas UTM e geográficas.")
    with c3:
        st.info("🧭 **Problemas geodésicos**")
        st.write("Interfaces para os métodos de Puissant e Sodano.")

elif pagina == "Graus e radianos":
    mostrar_conversoes()

elif pagina == "UTM para geográfico":
    mostrar_utm_geografico()

elif pagina == "Geográfico para UTM":
    mostrar_geografico_utm()

elif pagina == "Problema directo — Puissant":
    mostrar_puissant(tipo="directo")

elif pagina == "Problema inverso — Puissant":
    mostrar_puissant(tipo="inverso")

elif pagina == "Problema directo — Sodano":
    mostrar_sodano(tipo="directo")

elif pagina == "Problema inverso — Sodano":
    mostrar_sodano(tipo="inverso")

elif pagina == "Cálculo de fuso":
    mostrar_calculo_fuso()

elif pagina == "Sobre":
    st.subheader("Sobre a aplicação")
    st.write(
        "A Calculadora Geodésica é um projecto em desenvolvimento para "
        "apoiar cálculos de Geodesia. Foi criada com Python e Streamlit."
    )
    st.write("Versão: 0.1 — interface inicial")
