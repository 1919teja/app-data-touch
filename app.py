from flask import Flask, request, jsonify
import tensorflow as tf
import pandas as pd
import numpy as np

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)


app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("touch_classifier.h5")

# Define expected feature names
EXPECTED_FEATURES = ["Touch Area (mm²)", "Pressure (force)"]

CLASS_LABELS = ["Child", "Teen", "Adult"]



# Define class labels (adjust if needed)
CLASS_LABELS = ["Child", "Teen", "Adult"]

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Ensure "features" is present in request
        if "features" not in data:
            return jsonify({"error": "Missing 'features' in request"}), 400
        
        # Convert input data into a DataFrame
        df = pd.DataFrame(data["features"])

        # Make predictions
        predictions = model.predict(df)

        # Convert predictions to class labels
        predicted_labels = [CLASS_LABELS[np.argmax(pred)] for pred in predictions]

        return jsonify({"predictions": predicted_labels})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
