# Imports
import streamlit as st
import os

# Streamlit code
st.set_page_config(
    page_title="Data",
    page_icon="📝",
)

st.write("# Dataset from Tomato Leaf Disease Project! 🍅")
st.sidebar.title("Pages")
st.sidebar.success("Select a page above.")

st.markdown(
    """
    Here you can see some data from the Tomato Leaf Disease Project dataset.

    The dataset contains photos from tomato leaves that may have different diseases or be healthy.

    You can find the following classes in the dataset:

    - Bacterial Spot

    - Early Blight

    - Late Blight

    - Leaf Mold

    - Septoria Leaf Spot

    - Spider Mites

    - Target Spot

    - Yellow Leaf Curl Virus

    - Mosaic Virus

    - Healthy

    Let's take a look at some tomatoes from the dataset!
    """
)

# Display photos
data_path = "sample/"
classes = ["Bacterial Spot",
              "Early Blight",
              "Late Blight",
              "Leaf Mold",
              "Septoria Leaf Spot",
              "Spider Mites",
              "Target Spot",
              "Yellow Leaf Curl Virus",
              "Mosaic Virus",
              "Healthy"]

folders = ['Tomato___Bacterial_spot',
           'Tomato___Early_blight',
           'Tomato___Late_blight',
           'Tomato___Leaf_Mold',
           'Tomato___Septoria_leaf_spot',
           'Tomato___Spider_mites Two-spotted_spider_mite',
           'Tomato___Target_Spot',
           'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
           'Tomato___Tomato_mosaic_virus',
           'Tomato___healthy']

dict_classes = dict(zip(folders, classes))

for folder in folders:
    st.write(f"## {dict_classes[folder]}")
    images_in_folder = []

    for i, image in enumerate(os.listdir(os.path.join(data_path, folder))):
        images_in_folder.append(f"{data_path}/{folder}/{image}")

        if len(images_in_folder) == 4 or i == len(os.listdir(os.path.join(data_path, folder))) - 1:
            st.image(images_in_folder,
                     caption=[f"Tomato leaf sample {dict_classes[folder]} {i + 1}." for i in range(len(images_in_folder))])
            images_in_folder = []
