import os
import pickle
import numpy as np
import pandas as pd

# Dynamically find the absolute path of the directory containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build the absolute paths to your model files
rf_model_path = os.path.join(BASE_DIR, 'models', 'RandomForestClassifier_model.pkl')
scaler_path = os.path.join(BASE_DIR, 'models', 'scaler.pkl')

# Load the models using the absolute paths
with open(file=rf_model_path, mode="rb") as file:
    model = pickle.load(file=file)

with open(file=scaler_path, mode="rb") as file:
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
