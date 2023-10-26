import numpy as np
import datetime
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense



model = Sequential()

model.add(Conv2D(16,(3, 3), activation='relu', input_shape=(150 ,60 ,3)))
model.add(MaxPooling2D((2 ,2)))
model.add(Conv2D(32 , (5 ,5),activation='relu'))
model.add(MaxPooling2D((2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(32, (7, 7),activation='relu'))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(units=256, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(units=2,activation = 'softmax'))

model.summary()

model.compile(optimizer = 'adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# create graph
time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
log_dir = "logs/fit/" +'L' +time
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
# choose M or L size's dataset
#img_np = np.load(file="image_train_Msize.npy")
#label_np = np.load(file="info_label_Msize.npy")
img_np = np.load(file="image_train_Lsize.npy")
label_np = np.load(file="info_label_Lsize.npy")

model.fit(img_np, label_np, epochs=14, validation_split=0.2, batch_size=32,callbacks=[tensorboard_callback])

#model.save('model_Msize.h5')
model.save('model_Lsize.h5')

#(check graph com)
#tensorboard --logdir=logs\fit 