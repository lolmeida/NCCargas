"""
Import libraries
"""
import pandas as pd
import streamlit as st
from PIL import Image

# import plotly.express as px
# import plotly.graph_objects as go
# from cutecharts.charts import Line

pd.set_option("precision", 2)
# pd.reset_option('precision')
pd.options.display.float_format = "{:,.2f}".format


# -------------------------------------------------------------------------------
st.set_page_config(page_title="Reunião do Conselho de Direção", layout="wide")


@st.cache()
def texto_report(texto, mapa, indice=0):
    """
    descriçao da funcao
    """
    posicao = ["TextoAntes", "TextoDepois"]
    result = texto[(texto["Mapa"] == mapa) & (texto[posicao[indice]] != "")][
        posicao[indice]
    ]
    texto = result.tolist()
    return st.write(
        "".join(texto),
    )


col_1, col_2, col_3 = st.columns(3)

with col_1:
    st.write(
        """
    ## Reunião Mensal
    Mês:  **Novembro 2021**
    """
    )


# -------------------------------------------------------------------------------
# with col_2:
#    if user in users.keys():
#        st.markdown(f'#### Utilizador:')
#
# -------------------------------------------------------------------------------
with col_3:
    img = Image.open("logo.png")
    st.image(img, width=200)  # , caption='O nosso orgulho')
    st.text("Local : Edifício Sede da ENCO")
    st.text("Data/Hora: 28/12/2021  09:00 TMG")
    st.write("Plataforma: **TEAMS**")


st.markdown("---")

if st.checkbox("Convocatória"):
    col_1, _ = st.columns(2)
    # col_1.image("Convocatoria_RCD_nov_2021.png", width=800)

    if st.checkbox("Ordem dos trabalhos"):

        if st.checkbox("1. Leitura e Aprovação da Acta da Reunião Anterior"):
            # st.title('Leitura e Aprovação da Acta da Reunião Anterior')
            a_1, a_2 = st.columns(2)
            # a_2.image("ACTA/ACTA_10_rcd_2021.png", width=600)
            st.markdown("---")

        if st.checkbox(
            "2. Apresentação e aprovação do Relatório de mês de Novembro de 2021"
        ):
            st.title("Validação dos pilares extratégicos")

            st.write("[...]")

        if st.checkbox(
            "3. Apresentação e partilha de conhecimentos obtidos durante as\
                 formações realizadas em Novembro de 2021"
        ):
            # st.title('Balanço da visita à São Tomé')
            a_1, a_2 = st.columns(2)
            # a_1.image("balanco_visita_PCA/balanco_visita.jpg", width=1080)
        if st.checkbox("4. Diversos"):
            if st.checkbox(
                "4.1 Ponto da situação da Estratégia e do Roadmap \
                    de transformação digital"
            ):

                a_1, a_2 = st.columns(2)
                b_1, b_2 = st.columns(2)

                # a_1.image("Roadmap_TD/Roadmap_TD_1.jpg", width=600)
                st.markdown("---")
                b_1.write(
                    """
                ROADMAP DE TRANSFORMAÇÃO



                """
                )

                # b_1.image('Roadmap_TD/Roadmap_TD_4.jpg', width=600)

                b_2.write("""AS MELHORIAS DA TRANSFORMAÇÃO DIGITAL""")

            if st.checkbox("FIM"):
                st.markdown("### Obrigado !")
                st.balloons()
