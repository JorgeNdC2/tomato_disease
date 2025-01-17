# Imports
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
from typing import Tuple

# Functions
def predict_disease(image: Image.Image, model_str: str="Pretrained Model") -> Tuple[str, float]:

    # Dict models
    dict_models = {
        "Pretrained Model": "../models/model_pretrained_50.h5",
        "Basic Model from Scratch": "../models/basic_model_from_scratch_100.h5",
        "CNN Model": "../models/model_cnn_70.h5",
    }

    # Load the model
    model = load_model(dict_models[model_str])

    # Preprocess the image
    image = image.resize((256, 256)) if model_str != "CNN Model" else image.resize((224, 224))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image/255.0, axis=0) # Normalization (same as in training) and adding a dimension for the batch

    prediction = model.predict(image)

    # Classes based on `train_data.class_names` from the notebooks
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
    
    prediction_class = classes[np.argmax(prediction)]
    return prediction_class, np.max(prediction)
