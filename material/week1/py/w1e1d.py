#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import random

def f(x):
    return -x**4 + 2 * x**3 + 2 * x**2 - x

def exhaustive(function, start, stop, step):
    x = start
    best = (x, function(x))
    while x < stop:
        y = function(x)
        if y > best[1]:
            best = (x,y)
        plt.plot(x,y, color="red", marker="s", markersize=3)
        x += step
    return best

def plot_exhaustive(function,start,stop,steps):
    x = np.linspace(start, stop, steps)

    plt.plot(x,function(x))
    randx = random.uniform(start,stop)
    sol = exhaustive(function, start, stop, step=0.5)
    plt.plot(sol[0],sol[1], color="yellow", marker="*", markersize=16)
    plt.savefig("eps/w1e1d.eps", format="eps")
    plt.show()

if __name__ == "__main__":
    plot_exhaustive(f,-2,3,100)
