import numpy as np


def conv2D(input_2Ddata, kern):
    # Height and width of input data
    (h, w) = input_2Ddata.shape
    # Height and width of convolution kernel
    (kern_h, kern_w) = kern.shape
    padding_h = (kern_h - 1) // 2
    padding_w = (kern_w - 1) // 2
    padding = np.zeros(shape=(h + 2 * padding_h, w + 2 * padding_w))
    padding[padding_h:-padding_h, padding_w:-padding_w] = input_2Ddata
    # input data and output data has the same size
    output_2Ddata = np.zeros(shape=(h, w))
    for i in range(h):
        for j in range(w):
            # Partial window
            window = padding[i:i + kern_h, j:j + kern_w]
            # Inner product
            output_2Ddata[i, j] = np.sum(kern * window)


# Height of input data
h = 32
# Width of input data
w = 48
# Depth of input data
in_d = 12
# Depth of output data
out_d = 24
input_3Ddata = np.random.randn(h, w, in_d)
output_3Ddata = np.zeros(shape=(h, w, out_d))
