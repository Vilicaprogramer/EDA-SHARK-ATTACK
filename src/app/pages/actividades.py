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
st.markdown('# ¿Qué actividades se estaban haciendo cuando se sufrió el ataque?')
actividades_x_ano()