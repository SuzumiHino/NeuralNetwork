import numpy as np
import tensorflow as tf

# def load_dataset():
#     with np.load("mnist.npy") as f:
#         # convert to RGB to Unit RGB
#         x_train = f['x_train'].astype("float32") / 255
#
#         # reshape form (60000, 28, 28) into (60000, 784)
#         x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1]*x_train.shape[2]))
#
#         # labels
#         y_train = f['y_train']
#
#         # convert to output layer format
#         y_train = np.eye(10)[y_train]
#
#         return x_train, y_train

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def load_dataset(data_url):
	DATA_URL = data_url
	path = tf.keras.utils.get_file('mnist.npz', DATA_URL)
	with np.load(path) as data:
		train_examples = data['x_train']
		train_labels = data['y_train']
		test_examples = data['x_test']
		test_labels = data['y_test']

# load_dataset(data_url="https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz")