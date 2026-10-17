import os
import pickle
import numpy as np
import pandas as pd

# Find the exact folder where this prediction.py file is running right now
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Look for the models folder directly inside that directory
models_dir = os.path.join(CURRENT_DIR, 'models')

# Set the final absolute file targets
rf_model_path = os.path.join(models_dir, 'RandomForestClassifier_model.pkl')
scaler_path = os.path.join(models_dir, 'scaler.pkl')

# Load your machine learning model binaries safely
with open(file=rf_model_path, mode="rb") as file:
    model = pickle.load(file=file)

with open(file=scaler_path, mode="rb") as file:
    scaler = pickle.load(file=file)

class_labels = ['Negative', 'Positive']  # 0 = no diabetes, 1 = diabetes

def predict_res(input_data):
    print(f'Input data: {input_data}')
    scaled_data = scaler.transform(np.array(input_data).reshape(1, -1))
    model_prediction = model.predict(scaled_data)
    class_label = int(model_prediction[0])
    class_name = class_labels[class_label]
    return class_label, class_name
