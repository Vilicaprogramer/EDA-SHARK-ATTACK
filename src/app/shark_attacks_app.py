import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df_shark = pd.read_csv(r'C:\Users\Vicen\Visual Code\The_Bridge\Personal_2506_dsft_thebridge\2-Analytics\EDA\EDA-SHARK-ATTACK\src\data\shark_attack_clean.csv', index_col=1)

# Configurar el tema
st.set_page_config(page_title="Ataques de Tiburones", layout="wide", page_icon="🦈")

# Título
st.title("🦈 Análisis de Ataques de Tiburones")
st.markdown("""
Una exploración visual de los ataques de tiburones en los últimos 100 años.
""")

# Barra lateral
selectbox = st.sidebar.selectbox('Seleccion de Pais para ', df_shark['country'].unique(), placeholder='Elige un país', index= None)
selectslider = st.sidebar.select_slider('Selecciona un rango de años', sorted(df_shark['year'].unique()))

# Evolución de los ataques por años
anos_disp= df_shark['year'].value_counts().sort_index(ascending=True).to_frame().reset_index()
fig_evo_x_anos = px.line(anos_disp, x="year", y="count")
st.subheader('Evolución de los ataques por años')
event = st.plotly_chart(fig_evo_x_anos)

# Booble plot
df_shark['decade'] = (df_shark['year'] // 10 * 10).astype(int)
# Agrupar por década y actividad, y contar
activity_counts = df_shark.groupby(['decade', 'activity']).size().reset_index(name='count')

# Para cada década, seleccionar las 5 actividades más comunes
top5_by_decade = (
    activity_counts.groupby('decade')
    .apply(lambda x: x.nlargest(5, 'count'))
    .reset_index(drop=True)
)

# Ahora unimos con país para graficar después
df_top5 = df_shark.merge(top5_by_decade[['decade', 'activity']], on=['decade', 'activity'])

summary = (
    df_top5.groupby(['decade', 'activity', 'country'])
    .size()
    .reset_index(name='count')
)

if selectbox == None:
    fig_top5 = px.scatter(
        summary,
        x="decade",
        y="activity",
        size="count"
    )
else:
    fig_top5 = px.scatter(
        summary[summary['country'] == selectbox],
        x="decade",
        y="activity",
        size="count",
    )

st.subheader('Top 5 actividades por decada')
event = st.plotly_chart(fig_top5)






