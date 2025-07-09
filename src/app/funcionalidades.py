import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import base64
import os

df_shark = pd.read_csv(r'..\data\shark_attack_enriquecido.csv')
df_tourism = pd.read_csv(r'../data/turismo_mundial.csv')
df_totales = pd.read_csv(r'../data/totales.csv')
df_tourism.drop(['Unnamed: 0', '1994', '1993', '2023', '2024'], axis=1, inplace=True)

def page_configuration():
    # Configurar el tema
    st.set_page_config(page_title="Ataques de Tiburones", layout="wide", page_icon="🦈")

    st.sidebar.page_link("shark_attacks_app.py", label="Shark Attack Home", icon="🦈")
    st.sidebar.page_link("pages/presentacion.py", label="Presentación")
    st.sidebar.page_link("pages/miedo.py", label="¿Es irracional?")
    st.sidebar.page_link("pages/num_absolutos.py", label="Numeros Absolutos")
    st.sidebar.page_link("pages/actividades.py", label="¿Qué estaban haciendo?")
    st.sidebar.page_link("pages/datos_varios.py", label="Rebuscando entre los datos")
    st.sidebar.page_link("pages/num_relativos.py", label="Numeros Relativos")
    st.sidebar.page_link("pages/conclusiones.py", label="Conclusiones")


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

    set_png_as_page_bg(r'C:\Users\Vicen\Visual Code\The_Bridge\Personal_2506_dsft_thebridge\2-Analytics\EDA\EDA-SHARK-ATTACK\src\app\img\Shark.jpg')


def mapa_dispersion():
    with st.expander('Dispersión mundial de los ataques de tiburón a lo largo de los últimos 100 años'):
        decadas = []
        for decada in df_shark['decade'].unique():
            try:
                decadas.append(int(decada))
            except:
                continue
        
        decadas = sorted(decadas)[1:]

        # Crear botones en filas de 5 columnas
        botones = []
        for i in range(0, len(decadas), 5):
            cols = st.columns(5)
            for j in range(5):
                if i + j < len(decadas):
                    boton = cols[j].button(str(decadas[i + j]))
                    botones.append((decadas[i + j], boton))

        # Aquí podrías manejar la lógica si uno de los botones fue presionado
        for decada, presionado in botones:
            if presionado:
                geo_fig = px.scatter_geo(df_shark.loc[df_shark['decade'] == str(decada)], 'lat', 'lon',
                                hover_name='area', 
                                animation_group = 'country',
                                title= 'Ataques por el mundo', 
                                width= 1500, height= 750, 
                                projection="hammer")
                event = st.plotly_chart(geo_fig)
                return event

        geo_fig = px.scatter_geo(df_shark, 'lat', 'lon',
                                hover_name='area', 
                                animation_group = 'country',
                                title= 'Ataques por el mundo', 
                                width= 1500, height= 750, 
                                projection="hammer")
        event = st.plotly_chart(geo_fig)
        return event
    
def barras_paises():
    with st.expander('Número de ataques por pais en los últimos 100 años'):
        b_paises= df_shark.groupby('country').agg('size').sort_values(ascending=False).to_frame().reset_index().rename(columns={0:'count'})
        fig = px.bar(b_paises.iloc[:25], 'country', 'count', title="25 paises con más ataques")
        fig.add_hline(50, line_width=3, line_dash="dash", line_color="red")
        fig.add_annotation(x='MOZAMBIQUE', y=50, text="Pasan de 50 ataques en 100 años", showarrow=True, arrowhead=1, arrowsize=3, arrowcolor='red', bgcolor='red') 
        event = st.plotly_chart(fig)
        return event


def ataques_ano():
    st.markdown('### Número de ataques por año')
    anos_disp = df_shark['year'].value_counts().sort_index(ascending=True).to_frame().reset_index()
    anos_disp.columns = ['year', 'count']

    # Convertir y limpiar
    anos_disp['year'] = pd.to_numeric(anos_disp['year'], errors='coerce')
    anos_disp['count'] = pd.to_numeric(anos_disp['count'], errors='coerce')
    anos_disp.dropna(inplace=True)

    # Eliminar infinitos si hay
    anos_disp = anos_disp[np.isfinite(anos_disp['year'])]
    anos_disp = anos_disp[np.isfinite(anos_disp['count'])]

    # Ajuste de línea de regresión lineal
    coef = np.polyfit(anos_disp['year'], anos_disp['count'], 1)
    poly1d_fn = np.poly1d(coef)

    # Crear gráfico base con plotly express
    fig = px.line(anos_disp, x="year", y="count", title="Numero de ataques por años")

    # Añadir línea de tendencia
    fig.add_trace(go.Scatter(
        x=anos_disp['year'],
        y=poly1d_fn(anos_disp['year']),
        mode='lines',
        name='Tendencia',
        line=dict(color='red', dash='dash')
    ))
    
    fig.update_yaxes(range=[0,161])
    event = st.plotly_chart(fig)
    return event


def turismo_ano():
    with st.expander('Número de turistas por año'):
        # Sumar las columnas de años (ignorando la primera columna, que se asume no numérica)
        anos_tourism = df_tourism.iloc[:, 1:].sum(axis=0).to_frame()
        anos_tourism = anos_tourism / 2

        # Convertir el índice (años) a numérico
        anos_tourism.index = pd.to_numeric(anos_tourism.index, errors='coerce')

        # Eliminar índices inválidos (NaN) después de la conversión
        anos_tourism.dropna(inplace=True)

        # Renombrar columna 
        anos_tourism.columns = ['count']

        # Resetear índice para que 'year' sea una columna
        anos_tourism = anos_tourism.reset_index()
        anos_tourism.columns = ['year', 'count']

        # Asegurar que ambas columnas sean numéricas
        anos_tourism['year'] = pd.to_numeric(anos_tourism['year'], errors='coerce')
        anos_tourism['count'] = pd.to_numeric(anos_tourism['count'], errors='coerce')
        anos_tourism.dropna(inplace=True)

        # Comprobar que hay al menos 2 puntos válidos
        if len(anos_tourism) >= 2:
            coef = np.polyfit(anos_tourism['year'], anos_tourism['count'], 1)
            poly1d_fn = np.poly1d(coef)

            # Crear gráfico
            fig = px.line(anos_tourism, x='year', y='count', title="Número de turistas por año")

            # Añadir línea de tendencia
            fig.add_trace(go.Scatter(
                x=anos_tourism['year'],
                y=poly1d_fn(anos_tourism['year']),
                mode='lines',
                name='Tendencia',
                line=dict(color='red', dash='dash')
            ))

            event = st.plotly_chart(fig)
        else:
            st.warning("No hay suficientes datos válidos para calcular la línea de tendencia.")
            event = None

        return event

    

def presentacion():    
    if st.button('Change'):
        return st.image(r"C:\Users\Vicen\Visual Code\The_Bridge\Personal_2506_dsft_thebridge\2-Analytics\EDA\EDA-SHARK-ATTACK\src\app\img\shark_4k.jpg", caption="Fear the Shark")  
    else:
        return st.image(r"C:\Users\Vicen\Visual Code\The_Bridge\Personal_2506_dsft_thebridge\2-Analytics\EDA\EDA-SHARK-ATTACK\src\app\img\playa.jpg", caption="Sunrise beach")
    

def actividades_x_ano():
    # Agrupar por década y actividad, y contar
    global df_shark

    df_shark = df_shark[~df_shark['activity'].isin(['UNKNOWN', 'N', 'Y'])]
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
    df_top5.groupby(['decade', 'activity'])
    .size()
    .reset_index(name='count')
    )

    fig = px.scatter(
            summary,
            x="decade",
            y="activity",
            size="count",
            size_max= 40
        )
    fig.add_hrect(y0=5, y1=7, line_width=0, fillcolor="red", opacity=0.4)
    fig.add_shape(
        type="rect",
        x0=1960,
        x1=2010,
        y0=9,
        y1=11,
        fillcolor="green",
        opacity=0.4,
        line_width=0,
        layer="below"
    )

    event = st.plotly_chart(fig)
    return event

def quesitos_varios():
    fig = make_subplots(rows=2, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}],
                                               [{'type':'domain'}, {'type':'domain'}]])

    colores_vivos = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77']

    type_counts = df_shark.loc[df_shark['type'].isin(['Unprovoked', 'Provoked', 'Watercraft', 'Invalid']), 'type'].value_counts()
    fig.add_trace(go.Pie(labels=type_counts.index, values=type_counts.values,
                         marker=dict(colors=colores_vivos),
                         title={'text': 'Tipo de Ataque', 'font': {'size': 18}}), row=1, col=1)

    sex_counts = df_shark.loc[df_shark['sex'] != 'N', 'sex'].value_counts()
    fig.add_trace(go.Pie(labels=sex_counts.index, values=sex_counts.values,
                         marker=dict(colors=colores_vivos),
                         title={'text': 'Sexo', 'font': {'size': 18}}), row=1, col=2)

    fatal_counts = df_shark['fatal_y_n'].value_counts()
    fig.add_trace(go.Pie(labels=fatal_counts.index, values=fatal_counts.values,
                         marker=dict(colors=colores_vivos),
                         title={'text': '¿Fatal?', 'font': {'size': 18}}), row=2, col=1)

    ocio_counts = df_shark['ocio_o_no'].value_counts()
    fig.add_trace(go.Pie(labels=ocio_counts.index, values=ocio_counts.values,
                         marker=dict(colors=colores_vivos),
                         title={'text': 'Actividad de Ocio o no', 'font': {'size': 18}}), row=2, col=2)

    fig.update_layout(
        title={
            'text': "Resumen de Ataques de Tiburón",
            'font': {'size': 28},
            'x': 0.5,
            'xanchor': 'center'
        },
        showlegend=False,
        height=1000
    )
    event = st.plotly_chart(fig)
    return event

def porcentaje_ano():
    fig = px.line(df_totales, x='year', y='porcentaje')
    fig.update_layout(yaxis_autorange="reversed")
    fig.add_hline(0.000021, line_width=3, line_dash="dash", line_color="red" )
    event = st.plotly_chart(fig)
    return event


def datos_finales():
    df_totales_x_pais = pd.read_csv(r"C:\Users\Vicen\Visual Code\The_Bridge\Personal_2506_dsft_thebridge\2-Analytics\EDA\EDA-SHARK-ATTACK\src\data\totales_x_pais.csv")
    col1, col2, col3 = st.columns(3)

    with col1:
        country = st.selectbox("Pais", 
                               sorted(df_totales_x_pais['country']),
                               index=None,
                               placeholder="Select a country...")
    if country:
        total_ataques = df_totales_x_pais.loc[df_totales_x_pais['country'] == country, 'totales_ataques'].item()
        total_turistas = df_totales_x_pais.loc[df_totales_x_pais['country'] == country, 'totales_turistas'].item()
    else:    
        total_ataques = df_totales['count_ataques'].sum()
        total_turistas = df_totales['count_turistas'].sum()

    with col2:
        st.markdown("""### Numero total \n ### Ataques""")
        st.metric(" ", total_ataques)
        

    with col3:
        st.markdown("""### Numero total \n ### Turistas""")
        st.metric(" ", round(total_turistas))

    
    st.image(r"C:\Users\Vicen\Visual Code\The_Bridge\Personal_2506_dsft_thebridge\2-Analytics\EDA\EDA-SHARK-ATTACK\src\app\img\Infografia-probabilidad-de-muerte-segun-deporte-de-riesgo.jpg")
    st.markdown("## Ataques de tiburón")
    st.markdown(f"#### 1 ataque por cada {round(total_turistas/total_ataques)} una probabilidad de {(total_ataques/total_turistas)*100:.6f}")