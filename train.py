import joblib  # Import joblib to load the data
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# Load the saved dataset
X_train, X_test, y_train, y_test = joblib.load("data.pkl")

# Define Model with Proper Input Shape
model = Sequential([
    Input(shape=(2,)),  # Define input layer explicitly
    Dense(16, activation="relu"),
    Dense(8, activation="relu"),
    Dense(3, activation="softmax")  # Output Layer (3 categories)
])

# Compile the Model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train the Model
model.fit(X_train, y_train, epochs=50, batch_size=4, validation_data=(X_test, y_test))

# Save the trained model
model.save("touch_classifier.h5")
print("✅ Model Trained & Saved Successfully!")
