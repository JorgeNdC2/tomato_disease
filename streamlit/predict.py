# Imports
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

# Functions
def predict_disease(image):

    # Load the model
    model = load_model("../models/model_pretrained_10.h5")

    # Preprocess the image
    image = image.resize((256, 256))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image/255.0, axis=0) # Normalization (same as in training) and adding a dimenision for the batch
    print(image.shape)

    prediction = model.predict(image)

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
    
    prediction = classes[np.argmax(prediction)]
    return prediction
    
    