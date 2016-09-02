#!/usr/bin/env python3
# author: github.com/olehermanse

# import libraries used for plotting and mathematical operations:
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**4 + 2 * x**3 + 2 * x**2 - x

def exhaustive(function, start, stop, step, plotting=False):
    x = start
    best = (x, function(x))
    while x < stop:
        y = function(x)
        if y > best[1]:
            best = (x,y)
        x += step
    return best

def plot_with_max(func,start,stop,steps):
    x = np.linspace(start, stop, steps)

    plt.plot(x,func(x))
    step = (stop - start) / steps
    maximum = exhaustive(func, start, stop, step, plotting=True)
    (x,y) = maximum
    plt.plot(x,y, color="yellow", marker="*", markersize=16)

    plt.show()

if __name__ == "__main__":
    plot_with_max(f,-2,3,80)
