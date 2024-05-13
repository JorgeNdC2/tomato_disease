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
    ### Model selection 🤖

    You can select the model you want to use to classify the tomato leaf image.

    We have two models available:

    - **Pretrained Model**: A model trained with a pretrained model (`DenseNet121`) and trained with the Tomato Leaf Disease Dataset.

    - **Basic Model from Scratch**: A model trained from scratch with the Tomato Leaf Disease Dataset.

    - **CNN Model**: Qirun

    Note that the pretrained model has a higher accuracy than the basic model from scratch, but has a higher computational cost.

    You can select the model you want to use in the dropdown below!
    """
)

model = st.selectbox("Select the model you want to use", ["Pretrained Model", "Basic Model from Scratch", "CNN Model"])

st.markdown(
    """
    ### Upload your tomatoes! 📸

    You can upload an image of a tomato leaf and we will predict if it has a disease or not.

    Just click on the button below and upload your image. We will take care of the rest! 🚀
    """
)

uploaded_file = st.file_uploader("Choose a tomato leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded tomato leaf.", width=364)
    st.write("")
    st.write("Classifying...")

    # Classify the image
    image = Image.open(uploaded_file)
    prediction, prob = predict_disease(image, model=model)
    st.write("Done! 🎉")
    st.write(f"Prediction: {prediction}" + 
             (" 🍅! That's a good looking tomato!" if prediction == "Healthy" 
              else " disease 🤒 You may want to take it to the tomato doctor 👨‍⚕️🏥"))
    st.write(f"Probability: {prob:.2f}" + 
             (" ✅" if prob >= 0.8
              else " ⚠️ Probability is a bit low, you should double check if the answer is OK" if prob >= 0.5 and prob < 0.8
              else " ❌ Probability is too low, you should double check if the answer is OK"))


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
