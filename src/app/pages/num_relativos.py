import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from funcionalidades import *

page_configuration()
fondeo_pantalla()
st.markdown("# ¿Cambia algo si miramos números relativos en vez de absolutos?")
porcentaje_ano()
st.markdown("### Para el que no lo sepa, el símbolo µ representa el prefijo 'micro', que indica una división por un millón (10^-6)")