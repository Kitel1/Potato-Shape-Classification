import tensorflow as tf
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

tf.config.list_physical_devices()
print("Num CPU/GPUs Available: ", (tf.config.list_physical_devices()))

