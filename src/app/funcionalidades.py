import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import base64
import os

df_shark = pd.read_csv(r'..\data\shark_attack_enriquecido.csv')
df_tourism = pd.read_csv(r'../data/turismo_mundial.csv')

def page_configuration():
    # Configurar el tema
    st.set_page_config(page_title="Ataques de Tiburones", layout="wide", page_icon="🦈")

    st.sidebar.page_link("shark_attacks_app.py", label="Shark Attack Home", icon="🦈")
    st.sidebar.page_link("pages/datos_generales.py", label="Datos generales", icon="1️⃣")


def fondeo_pantalla():
    @st.cache_resource
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_png_as_page_bg(png_file):
        if not os.path.exists(png_file):
            st.error(f"Imagen no encontrada: {png_file}")
            return

        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = f'''
        <style>
        html, body, [data-testid="stApp"] {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)

    set_png_as_page_bg(r'C:\Users\Vicen\Visual Code\The_Bridge\Personal_2506_dsft_thebridge\2-Analytics\9-Streamlit\img\Shark.jpg')


def mapa_dispersion():
    decada = st.columns(10, gap='small')
    with st.expander('Dispersión mundial de los ataques de tiburón a lo largo de los últimos 100 años'):
        geo_fig = px.scatter_geo(df_shark, 'lat', 'lon',
                                hover_name='area', 
                                animation_group = 'country',
                                title= 'Ataques por el mundo', 
                                width= 1500, height= 750, 
                                projection="hammer")
        event = st.plotly_chart(geo_fig)
        return event