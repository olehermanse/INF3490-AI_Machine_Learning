#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**4 + 2 * x**3 + 2 * x**2 - x

def df(x):
    return -4 * x**3 + 6 * x**2 + 4 * x - 1

x = np.linspace(-2, 3, 100)
plt.plot(x,f(x))
plt.plot(x,df(x))
plt.savefig("w1e1b.eps", format="eps")
plt.show()
