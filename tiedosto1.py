import numpy as np

def fir(x, k):
    x_pad = np.zeros(len(x)+len(k)-1)
    x_pad[k:] = x
    y = np.zeros_like(x)

    for i in range(len(y)):
        y[i] = np.dot(x_pad[i:i+k], k)

    return y
