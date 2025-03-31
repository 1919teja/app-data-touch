import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib  # For saving variables

# Load dataset
data = pd.read_csv("touch_data.csv")

# Encode Age Group (Child=0, Teen=1, Adult=2)
label_encoder = LabelEncoder()
data["Age Group"] = label_encoder.fit_transform(data["Age Group"])

# Features and Labels
X = data[["Touch Area (mm²)", "Pressure (force)"]].values
y = data["Age Group"].values

# Split into Train & Test Sets (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save Data to Files
joblib.dump((X_train, X_test, y_train, y_test), "data.pkl")

print("✅ Data Loaded & Saved Successfully!")
