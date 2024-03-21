import tensorflow as tf
import pickle

# Load the Keras model
model = tf.keras.models.load_model('model.h5')

# Convert the Keras model to a TensorFlow SavedModel
tf.saved_model.save(model, 'saved_model')

# Serialize the SavedModel using pickle
with open('model.pkl', 'wb') as f:
    pickle.dump('saved_model', f)

print("Model successfully converted to pickle file.")
print('deploy')