<p align="center"> <img src=r".\img\Shark.jpg" alt="Shark banner" width="600"> </p> <h1 align="center">EDA: Ataques de Tiburón 🦈</h1> <p align="center"><em>¿Es tan peligroso el océano como creemos?</em></p>

📊 ### Exploración de Datos de Ataques de Tiburón

**¿Cuán justificado es temer a los tiburones?**
Este proyecto analiza más de un siglo de incidentes reales utilizando datos del Global Shark Attack File.


📁 Estructura del Proyecto
bash
```
EDA-SHARK-ATTACK/
│
├── 📓 Memoria_Shark_Attacks_ES.ipynb    # Análisis completo, comentado
├── src/
│   ├── app/                             # App Streamlit
│   │   ├── img/                         # Imágenes e infografías
│   │   ├── pages/                       # Módulos de navegación
│   ├── data/                            # Datos procesados
│   ├── notebooks/                       # Otros notebooks
│   ├── utils/                           # Funciones auxiliares
🚀 Cómo Ejecutar el Proyecto
```
bash

```
# 1. Clona el repositorio
git clone https://github.com/Vilicaprogramer/EDA-SHARK-ATTACK.git
cd EDA-SHARK-ATTACK

# 2. (Opcional) Crea un entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# 3. Instala dependencias
pip install pandas numpy seaborn matplotlib plotly streamli

# 4. Lanza la app
streamlit run ./src/app/shark_attacks_app.py
```
#🔬 **Hipótesis Evaluadas**
| Nº|	Pregunta	| Resultado|
|---|-----------|-----------|
|1️⃣|	¿El miedo a tiburones es irracional?|	✅ Confirmado|
|2️⃣|	¿Los ataques van en descenso?|	➖ Tendencia débil|
|3️⃣|	¿El riesgo por turista no aumenta?|	✅ Confirmado|
|4️⃣|	¿Los hombres sufren más ataques?|	✅ Confirmado|
|5️⃣|	¿El surf es la actividad más arriesgada?|	✅ Confirmado|

#🛠️ **Tecnologías Usadas**
🐍 Python (pandas, seaborn, matplotlib, plotly)

🖼️ Streamlit (para visualización interactiva)

📈 Jupyter Notebook

📊 Análisis exploratorio de datos (EDA)

#🤝 **Contribuciones**
¡Contribuciones son bienvenidas!
Si tienes ideas, errores que corregir o mejoras, abre un issue o un pull request.

#🧠 **Autor**
Vicen – Proyecto personal dentro del bootcamp de Data Science en The Bridge (2025).