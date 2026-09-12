import streamlit as st
from loader import page_icon


st.set_page_config(
    page_title="Diabetes Prediction with AI",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
from app.header import app
app()

# Inputs
from app.input import app
input_data =  app()

# Prediction
from app.predict import app
prediction_probability = app(input_data)

# Rule-based context for the entered patient values
from app.explanation import app
app(input_data, prediction_probability)

# Input streaming
from app.explainer import app
app(input_data)

# About
from app.about import app
app()
