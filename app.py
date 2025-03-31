from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("touch_classifier.h5")

# Age categories
labels = ["Child", "Teen", "Adult"]

@app.route('/')
def home():
    return "API is working!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        touch_area = float(data["touch_area"])
        pressure = float(data["pressure"])

        # Format input for the model
        input_data = np.array([[touch_area, pressure]])
        prediction = model.predict(input_data)

        # Get the highest probability class
        age_category = labels[np.argmax(prediction)]
        
        return jsonify({"age_category": age_category})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

