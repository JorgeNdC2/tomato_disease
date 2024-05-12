# Imports
import streamlit as st
from predict import predict_disease
from PIL import Image

# Streamlit code
st.set_page_config(
    page_title="Tomato Leaf Disease Project",
    page_icon="🍅",
)

st.write("# Welcome to our Tomato Leaf Disease Project! 🍅")
st.sidebar.title("Pages")
st.sidebar.success("Select a page above.")

st.markdown(
    """
    Hey there! 👋 

    This is a dashboard for our Tomato Leaf Disease Project.

    You can navigate through the pages using the sidebar on the left, where you can find the following options:

    - **Home** 🏘️: This page.

    - **Models** 🤖: A summary with the results we have obtained from the models we have trained. You can find a line chart with the accuracy and validation accuracy of the models in the `Models` tab.

    - **Data** 📝: A summary of the data we have used to train our models. You can get a glimpse of the data in the `Data` tab.
    """
)

st.markdown(
    """
    ### Upload your tomatoes! 📸

    You can upload an image of a tomato leaf and we will predict if it has a disease or not.

    Just click on the button below and upload your image. We will take care of the rest! 🚀
    """
)

uploaded_file = st.file_uploader("Choose a tomato leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded tomato leaf.", use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Classify the image
    image = Image.open(uploaded_file)
    prediction, prob = predict_disease(image)
    st.write("Done! 🎉")
    st.write(f"Prediction: {prediction}" + 
             (" 🍅! That's a good looking tomato!" if prediction == "Healthy" 
              else " disease 🤒 You may want to take it to the tomato doctor 👨‍⚕️🏥"))
    st.write(f"Probability: {prob:.2f}")


st.markdown(
    """
    ### About the dataset 📋

    The dataset we are using is the [Tomato Leaf Disease Dataset](https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf) from Kaggle.
    It contains images of tomato leaves with different diseases, such as Mosiac Virus, Yellow Leaf Curl Virus and Bacterial Spot.

    ### About us 📧

    We are a group of students from the Non Structured Data Analysis course at the University of Comillas (ICAI):

    - Raúl Blázquez Bullón ([@raulblazquezb](https://github.com/raulblazquezb)).

    - Jorge Núñez de Cela Román ([@JorgeNdC2](https://github.com/JorgeNdC2)).

    - Qirun Wu ([@quirunw](https://github.com/qirunw)).
    """,
)

# Run the app
# streamlit run Home.py
