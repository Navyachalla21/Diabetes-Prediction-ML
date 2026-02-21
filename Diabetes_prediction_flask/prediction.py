import pandas as pd
import numpy as np
import pickle


with open(file="models/RandomForestClassifier_model.pkl", mode="rb") as file:
    model = pickle.load(file=file)


with open(file="models/scaler.pkl", mode="rb") as file:
    scaler = pickle.load(file=file)


class_labels = ['Positive', "Negative"]


def predict_res(input_data):

    print(f'Input data: {input_data}')

    scaled_data = scaler.transform(np.array(input_data))
    print(scaled_data)

    model_prediction = model.predict(scaled_data)
    class_label = model_prediction[0]
    class_name = class_labels[class_label]

    print(f"model_prediction : {model_prediction}")
    print(f"CLASS LABEL : {class_label}")
    print(f"CLASS NAME : {class_name}")

    return class_label, class_name
