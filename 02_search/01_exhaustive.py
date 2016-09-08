#!/usr/bin/env python3
# author: github.com/olehermanse

# import libraries used for plotting and mathematical operations:
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**4 + 2 * x**3 + 2 * x**2 - x

def exhaustive(function, start, stop, step, plotting=False):
    x = start
    best = (x,-99999)
    while x < stop:
        y = function(x)
        if y > best[1]:
            best = (x,y)
            if plotting:
                plt.plot(x,y, color="blue", marker="s", markersize=3)
        else:
            if plotting:
                plt.plot(x,y, color="red", marker="s", markersize=3)
        x += step
    return best

def plot_with_max(func,start,stop,steps):
    x = np.linspace(start, stop, steps)

    fig = plt.figure("INF3490 - Exhaustive Search")
    fig.suptitle("Visualization of exhaustive search")

    plt.plot(x,func(x))
    step = (stop - start) / steps
    maximum = exhaustive(func, start, stop, step, plotting=True)
    (x,y) = maximum
    plt.plot(x,y, color="yellow", marker="*", markersize=16)

    plt.savefig("exhaustive.eps", format="eps")
    plt.show()

if __name__ == "__main__":
    plot_with_max(f,-2,3,80)
