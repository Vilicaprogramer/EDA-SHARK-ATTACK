
<p align="center">
  <img src="https://raw.githubusercontent.com/Vilicaprogramer/EDA-SHARK-ATTACK/master/docs/banner_shark.png" alt="Shark banner" width="600">
</p>

# EDA: Ataques de Tiburón 🦈

> **¿Cuán justificado es temer a los tiburones?**  
> Análisis de un siglo de incidentes documentados.

---

## 📑 Resumen
Este repositorio contiene:

* `Memoria_Shark_Attacks_ES.ipynb` – Notebook interactivo con todo el flujo de análisis, limpio y comentado.    
* `src/` – Scripts auxiliares para limpieza y descargas.  

## 🚀 Cómo reproducir

```bash
# Clonar el proyecto
git clone https://github.com/Vilicaprogramer/EDA-SHARK-ATTACK.git
cd EDA-SHARK-ATTACK

# (opcional) Crear entorno
python -m venv .venv && source .venv/bin/activate
pip install pandas numpy seaborn matplotlib plotly streamlit

# Lanzar Jupyter
streamlit run ./src/app/shark_attacks_app.py
```

## 🔎 Hipótesis evaluadas

| # | Pregunta | Resultado |
|---|-----------|-----------|
| 1 | El miedo es irracional | ✅ Apoyada |
| 2 | Los ataques disminuyen | ➖ Tendencia débil |
| 3 | La números relativos no aumenta | ✅ Apoyada |
| 4 | Mayor riesgo en hombres | ✅ Apoyada |
| 5 | Surf es la actividad con más ataques | ✅ Apoyada |


## 📈 Vistazo rápido
<img src="docs/preview_timeline.png" width="600">

*Figura 1 – Evolución de incidentes anuales.*

## 🤝 Contribuir
¡Se aceptan *pull requests*! Revisa primero las **issues** abiertas.

## 📝 Licencia
MIT. Usa, comparte y adapta el proyecto siempre citando la fuente.
