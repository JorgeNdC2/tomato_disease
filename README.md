# Tomato Leaf Disease project

---

This repo contains all the code we have used to develop a model that can predict whether a tomato has a known leaf disease or not based on photos.

The data we have used is the [Tomato Leaf Disease dataset](https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf) from Kaggle. It contains 10 classes of tomato diseases. We will not upload the dataset to this repo, so if you want to try our notebooks make sure to download the dataset and save it to `data/input/`.

We have followed 2 approaches:

* Building models from scratch and evaluating their performance. We have tried some architectures based on Non Structured Data Analysis lectures.

* Loading a rather big pre-trained model, like `DenseNet121`, and add some more layers to it. This model has been by far the most accurate one and it is the one we use to predict the photos you upload.

We have developed a `Streamlit` app where you can upload your own tomato leaf photos and check if they have any known disease.

## Authors

* Raúl Blázquez Bullón ([@raulblazquezb](https://github.com/raulblazquezb)).

* Jorge Núñez de Cela Román ([@JorgeNdC2](https://github.com/JorgeNdC2)).

* Qirun Wu ([@quirunw](https://github.com/qirunw)).

## Requirements

We highly recommend using a virutal environment, like `virtualenv`.

To run the notebooks and codes, you have to install the packages:

```bash
pip install -r requirements.txt
```

## How to

We have developed a `Streamlit` app where you can upload your own tomato leaf photos to try our model. Just run (make sure you have installed at least `streamlit` package with `pip`):

```bash
python3 streamlit.py
```

A `Streamlit` page will show up in your browser. Just drag the photo you want and `DenseNet121` + collaborators will do the rest :).
