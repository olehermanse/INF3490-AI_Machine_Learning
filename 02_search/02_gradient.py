#!/usr/bin/env python3
# author: github.com/olehermanse

# import libraries used for plotting and mathematical operations:
import numpy as np
import matplotlib.pyplot as plt
import random

# Define a mathematical expression as a function:
def f(x):
    return -x**4 + 2 * x**3 + 2 * x**2 - x

def df(x):
    return -4 * x**3 + 6 * x**2 + 4 * x - 1

def gradient_ascent(function, derivative, gamma, x, precision):
    dx = gamma * df(x)
    while abs(dx) > precision:
        y = function(x)
        plt.plot(x,y, color="blue", marker="s", markersize=6)
        x += dx
        dx = gamma * df(x)
    return x,function(x)

def plot_gradient_ascent(function,derivative,start,stop,steps):
    x = np.linspace(start, stop, steps) # Make array of 100 values

    fig = plt.figure("INF3490 - Gradient Ascent")
    fig.suptitle("Visualization of gradient ascent")

    step = (stop - start) / steps

    plt.subplot(211)
    plt.plot(x,function(x))
    randx = random.uniform(start,stop)
    solution = gradient_ascent(function, derivative, 0.1, randx, 0.001)
    plt.plot(solution[0],solution[1], color="yellow", marker="*", markersize=16)
    plt.subplot(212)
    plt.plot(x,derivative(x))

    plt.savefig("gradient.pdf", format="pdf")
    plt.show()                  # Show all subplots in new window

if __name__ == "__main__":
    plot_gradient_ascent(f,df,-2,3,100)
