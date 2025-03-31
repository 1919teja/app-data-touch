from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load the updated model
model = tf.keras.models.load_model("touch_classifier.keras")

@app.route("/", methods=["GET"])
def home():
    return "Touch Classifier API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()  # Expecting a JSON request
        input_data = np.array(data["features"]).reshape(1, -1)  # Reshape for model
        
        prediction = model.predict(input_data)
        response = {"prediction": prediction.tolist()}
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
