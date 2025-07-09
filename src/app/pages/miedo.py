import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import base64
import os
from funcionalidades import *

page_configuration()
fondeo_pantalla()
st.markdown('# ¿Qué tan irracional es ese miedo?')
mapa_dispersion()
barras_paises()