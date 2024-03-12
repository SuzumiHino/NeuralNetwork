import numpy as np
import matplotlib.pyplot as plt

import utils

from time import time

start_time = time()

DATA_URL = "https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz"

images, labels = utils.load_dataset(data_url=DATA_URL)

weights_input_to_hidden = np.random.uniform(-0.5, .5, (30, 784))
# weights_hidden_to_hidden = np.random.uniform(-0.5, .5, (20, 20))
weights_hidden_to_output = np.random.uniform(-0.5, .5, (10, 30))

bias_input_to_hidden = np.zeros((30, 1))
# bias_hidden_to_hidden = np.zeros((20, 1))
bias_hidden_to_output = np.zeros((10, 1))

epochs = 50
e_loss = 0
e_correct = 0
learning_rate = 0.01



for epoch in range(epochs):
    print(f"Epoch №{epoch+1}")

    for image, label in zip(images, labels):
        image = np.reshape(image, (-1, 1))
        label = np.reshape(label, (-1, 1))

        # Forward propagation (to hidden layer)
        hidden_raw = bias_input_to_hidden + weights_input_to_hidden @ image
        hidden = utils.sigmoid(hidden_raw)

        # # Forward propagation (to second hidden layer)
        # hidden_second_raw = bias_hidden_to_hidden + weights_hidden_to_hidden @ hidden_first_raw
        # hidden_second = utils.sigmoid(hidden_second_raw)

        # Forward propagation (to output layer)
        output_raw = bias_hidden_to_output + weights_hidden_to_output @ hidden
        output = utils.sigmoid(output_raw)

        # Loss / Error calculating
        e_loss += 1 / len(output) * np.sum((output - label) ** 2, axis=0)
        e_correct += int(np.argmax(output) == np.argmax(label))

        # Backpropagation (output layer)
        delta_output = output - label
        weights_hidden_to_output += -learning_rate * delta_output @ np.transpose(hidden)
        bias_hidden_to_output += -learning_rate * delta_output

        # # Backpropagation (second hidden layer)
        # delta_hidden_second = np.transpose(weights_hidden_to_output) @ delta_output * (hidden_second * (1 - hidden_second))
        # weights_hidden_to_hidden += -learning_rate * delta_hidden_second @ np.transpose(hidden_first)
        # bias_hidden_to_hidden += -learning_rate * delta_hidden_second

        # Backpropagation (first hidden layer)
        delta_hidden = np.transpose(weights_hidden_to_output) @ delta_output * (hidden * (1 - hidden))
        weights_input_to_hidden += -learning_rate * delta_hidden @ np.transpose(image)
        bias_input_to_hidden += -learning_rate * delta_hidden

    print(f"Loss: {round((e_loss[0] / images.shape[0]) * 100, 3)}%")
    print(f"Accuracy: {round((e_correct / images.shape[0]) * 100, 3)}%")
    e_loss = 0
    e_correct = 0

test_image = plt.imread("custom_numbers/custom6.jpeg", format="jpeg")

# Grayscale
gray = lambda rgb: np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
test_image = 1 - (gray(test_image).astype("float32") / 255)

# reshape
test_image = np.reshape(test_image, (test_image.shape[0] * test_image.shape[1]))

# Predict
image = np.reshape(test_image, (-1, 1))

# Forward propagation (to hidden layer)
hidden_raw = bias_input_to_hidden + weights_input_to_hidden @ image
hidden = utils.sigmoid(hidden_raw)

# # Forward propagation (to second hidden layer)
# hidden_second_raw = bias_hidden_to_hidden + weights_hidden_to_hidden @ hidden_first_raw
# hidden_second = utils.sigmoid(hidden_second_raw)

# Forward propagation (to output layer)
output_raw = bias_hidden_to_output + weights_hidden_to_output @ hidden
output = utils.sigmoid(output_raw)

end_time = time()
print(f'Execution time: {round((end_time - start_time) / 60)} min')

plt.imshow(test_image.reshape(28, 28), cmap="Greys")
plt.title(f"NN suggests the number is : {output.argmax()}")
plt.show()
