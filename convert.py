import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the Keras model
model = load_model('model.h5')

# Convert the Keras model to a TensorFlow SavedModel
tf.saved_model.save(model, 'saved_model')

print("Model successfully converted to TensorFlow SavedModel.")
