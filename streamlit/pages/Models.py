# Imports
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Load data
data_path = "../data/output"
data = [pd.read_csv(f"{data_path}/{data_set}") for data_set in os.listdir(data_path) if data_set.endswith(".csv")]

# Streamlit code
st.set_page_config(
    page_title="Models",
    page_icon="🤖",
)

# Display title
st.write("# Models from Tomato Leaf Disease Project! 🍅")
st.sidebar.title("Pages")
st.sidebar.success("Select a page above.")

st.markdown(
    """
    Here you can find the models we have trained for the Tomato Leaf Disease Project.
    
    We have trained two models:
    
    - **Pretrained Model**: A model trained with a pretrained model (`DenseNet121`) and trained with the Tomato Leaf Disease Dataset.
    
    - **Basic Model from Scratch**: A model trained from scratch with the Tomato Leaf Disease Dataset.
    
    You can find a line chart with the accuracy and validation accuracy of the models below! 📈
    """
)

# Display data
for idx, df in enumerate(data):
    st.write(f"## {os.listdir(data_path)[idx].replace('.csv', '')}")
    st.write(df)
    st.write("---")

# Display line chart
st.write("## Line chart with the accuracy and validation accuracy of the models")
for idx, df in enumerate(data):
    st.write(f"### {os.listdir(data_path)[idx].replace('.csv', '')}")
    fig, ax = plt.subplots()
    ax.plot(df["epoch"], df["accuracy"], "b-", label="accuracy")
    ax.plot(df["epoch"], df["val_accuracy"], "r-", label="val_accuracy")
    ax.plot(df["epoch"], df["loss"], "b.", label="loss")
    ax.plot(df["epoch"], df["val_loss"], "r.", label="val_loss")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Value")
    ax.legend()
    st.pyplot(fig)
    st.write("---")

# Display model summary
st.markdown(
    """
    ## Model summary

    ### Pretrained Model

    The pretrained model has been trained with a DenseNet121 model and the Tomato Leaf Disease Dataset.
    It has an accuracy of 0.98 and a validation accuracy of 0.95.

    Though we initially set 50 epochs, the model stopped training at epoch 30 due to early stopping, since the validation loss was not improving.

    ### Basic Model from Scratch

    The basic model from scratch has been trained with a custom model and the Tomato Leaf Disease Dataset.
    It has an accuracy of 0.92 and a validation accuracy of 0.81.
    This shows that the model is overfitting the data.
    """
)