# Imports
import streamlit as st
import pandas as pd

# Load data
data_path = "../data/output"
data = pd.read_csv(f"{data_path}/basic_model_from_scratch_100.csv")

# Display data
st.line_chart(data=data, x="epoch", y=["accuracy", "val_accuracy"], use_container_width=True)