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

def gradient_ascent(derivative, gamma, x, precision):
    dx = gamma * derivative(x)
    while abs(dx) > precision:
        x += dx
        dx = gamma * derivative(x)
    return x,function(x)

def plot_gradient_ascent(function,derivative,start,stop,steps):
    x = np.linspace(start, stop, steps)

    plt.plot(x,function(x))
    randx = random.uniform(start,stop)
    solution = gradient_ascent(derivative, gamma=0.01, x=randx, precision=0.001)
    plt.plot(solution[0],solution[1], color="yellow", marker="*", markersize=16)

    plt.show()

if __name__ == "__main__":
    plot_gradient_ascent(f,df,-2,3,100)
