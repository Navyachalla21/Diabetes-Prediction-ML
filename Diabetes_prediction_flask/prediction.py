import os
import pickle
import numpy as np
import pandas as pd

# 1. Start looking from where prediction.py is currently running
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Try to find the models folder relative to this script
models_dir = os.path.join(CURRENT_DIR, 'models')

# 3. Cloud Fallback: If it's not found there, try the common Render structures
if not os.path.exists(os.path.join(models_dir, 'RandomForestClassifier_model.pkl')):
    models_dir = '/opt/render/project/src/models'
    
    if not os.path.exists(os.path.join(models_dir, 'RandomForestClassifier_model.pkl')):
        models_dir = '/opt/render/project/src/Diabetes_prediction_flask/models'

# Set the definitive final file targets
rf_model_path = os.path.join(models_dir, 'RandomForestClassifier_model.pkl')
scaler_path = os.path.join(models_dir, 'scaler.pkl')

# Load your machine learning model binaries safely
with open(file=rf_model_path, mode="rb") as file:
    model = pickle.load(file=file)

with open(file=scaler_path, mode="rb") as file:
    scaler = pickle.load(file=file)

class_labels = ['Positive', "Negative"]

def predict_res(input_data):
    print(f'Input data: {input_data}')
    scaled_data = scaler.transform(np.array(input_data).reshape(1, -1))
    model_prediction = model.predict(scaled_data)
    class_label = int(model_prediction[0])
    class_name = class_labels[class_label]
    return class_label, class_name
