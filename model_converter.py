import tensorflow as tf

# Load the model from .h5 format
model = tf.keras.models.load_model("touch_classifier.h5", compile=False)

# Save the model in the new .keras format
model.save("touch_classifier.keras")

print("✅ Model converted successfully to touch_classifier.keras!")
