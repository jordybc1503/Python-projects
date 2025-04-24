import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from sklearn.model_selection import train_test_split
from utils import load_galaxy_data

import app


input_data, labels = load_galaxy_data()
print(input_data.shape)
print(labels.shape)

#Split data into training and validation

x_train, x_validation, y_train, y_validation = train_test_split(input_data, labels, test_size =0.20, random_state = 222, stratify=labels)

#data generator

data_generator = ImageDataGenerator(rescale=1/255)

#4. NumpyArrayIterators

training_iterator = data_generator.flow(x_train, y_train,batch_size=5)
validation_iterator = data_generator.flow(x_validation, y_validation, batch_size=5)

#5. Build de model

model = tf.keras.Sequential()
model.add(tf.keras.Input(shape=(128, 128, 3)))

#7. Convolutional layers
model.add(tf.keras.layers.Conv2D(8, 3, strides=2, activation="relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2,2)))

model.add(tf.keras.layers.Conv2D(8, 3, strides=2, activation="relu")) 
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))

model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(16, activation="relu"))

#5. Build model 
model.add(tf.keras.layers.Dense(4,activation = "softmax"))



#6. Compile your model with an optimezer

optimizer_mod = tf.keras.optimizers.Adam(
    learning_rate=0.001,
    )
loss_mod = tf.keras.losses.CategoricalCrossentropy()

model.compile(optimizer=optimizer_mod, loss=loss_mod, metrics=[tf.keras.metrics.CategoricalAccuracy(),tf.keras.metrics.AUC()])

#8.  Model summary

model.summary()

#9. Train the model

model.fit(training_iterator, steps_per_epoch=len(x_train)/5, epochs=8, validation_data=validation_iterator,
        validation_steps=len(x_validation)/5)
from visualize import visualize_activations 

visualize_activations(model, validation_iterator )