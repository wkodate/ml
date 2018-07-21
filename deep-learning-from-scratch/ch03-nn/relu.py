# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x) # 大きい方の値を選んで出力

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1.0, 5.5)
plt.show()
