import tensorflow as tf
# from tensorflow.python.client import device_lib
# gpu_device_name = tf.test.gpu_device_name()
# print(gpu_device_name)
print(tf.test.is_built_with_cuda())
# tf.test.is_built_with_cuda()
print(tf.test.is_gpu_available())