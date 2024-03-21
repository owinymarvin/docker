import tensorflow as tf

# Load the Keras model
keras_model = tf.keras.models.load_model('model.h5')

# Convert the Keras model to a TensorFlow SavedModel
tf.saved_model.save(keras_model, 'saved_model')
