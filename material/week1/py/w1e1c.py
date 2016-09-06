#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import random

def f(x):
    return -x**4 + 2 * x**3 + 2 * x**2 - x

def df(x):
    return -4 * x**3 + 6 * x**2 + 4 * x - 1

def gradient_ascent(gamma, x, precision):
    dx = gamma * df(x)
    while abs(dx) > precision:
        plt.plot(x,f(x), color="red", marker="s", markersize=3)
        x  = x + dx
        dx = gamma * df(x)
    return x,f(x)

def plot_gradient_ascent(start,stop,steps):
    x = np.linspace(start, stop, steps)

    plt.plot(x,f(x))
    randx = random.uniform(start,stop)
    sol = gradient_ascent(gamma=0.1, x=randx, precision=0.0001)
    plt.plot(sol[0],sol[1], color="yellow", marker="*", markersize=16)
    plt.savefig("eps/w1e1c.eps", format="eps")
    plt.show()

if __name__ == "__main__":
    plot_gradient_ascent(-2,3,100)
