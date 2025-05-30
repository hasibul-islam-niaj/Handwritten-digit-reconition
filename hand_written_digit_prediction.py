# -*- coding: utf-8 -*-
"""hand written digit prediction.ipynb

Automatically generated by Colab.

Original file is located at Colab
"""

import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Step 1: Load the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print("1. Data Loaded... total: ", y_train.size)

# Step 2: Normalize the images (scale pixel values between 0 and 1)
x_train = x_train / 255.0
x_test = x_test / 255.0
print("2. Image Normalized...")

# Step 3: Reshape the data for CNN input (28x28x1)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)
print("3. Image Reshaped...")

# Step 4: Build the CNN model
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 digits (0 to 9)
])
print("4. CNN Model Build...")

# Step 5: Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
print("5. Model Compiled...")

# Step 6: Train the model
model.fit(x_train, y_train, epochs=5, validation_split=0.1)
print("6. Model Trained...")

# Step 7: Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc * 100:.2f}%")
print("7. Model Evaluated...")

import numpy as np

# Step 8: Make a prediction on test images
predictions = model.predict(x_test)
print("8. Predicted...")

# Step 9: Display a few predictions
def plot_image(i, predictions_array, true_label, img):
    # plt.grid(True)
    # plt.xticks([])
    # plt.yticks([])
    plt.imshow(img.reshape(28, 28), cmap=plt.cm.binary)
    predicted_label = np.argmax(predictions_array)
    true_label = true_label[i]

    color = 'blue' if predicted_label == true_label else 'red'
    plt.xlabel(f"Predicted: {predicted_label} (Actual: {true_label})", color=color)

# Show first 5 images with predictions
for i in range(5):
    plt.figure()
    plot_image(i, predictions[i], y_test, x_test[i])
    plt.show()
print("9. Finished...")

# If need to input from user

# from google.colab import files
# from IPython.display import display, Image
# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt

# uploaded = files.upload()
# filename = list(uploaded.keys())[0]
# image = Image.open(filename).convert('L')

# image = image.resize((28, 28))
# image_array = np.array(image) / 255.0
# image_array = image_array.reshape(1, 28, 28, 1)

# prediction = model.predict(image_array)
# predicted_label = np.argmax(prediction)

# plt.imshow(image_array.reshape(28, 28), cmap=plt.cm.binary)
# plt.title(f"Predicted: {predicted_label}")
# plt.show()