#!/usr/bin/env python3
# author: github.com/olehermanse

# import libraries used for plotting and mathematical operations:
import numpy as np
import matplotlib.pyplot as plt

# Define a mathematical expression as a function:
def f(t):
    return t**3

def df(t):
    return 3*t**2

def sub_plots():
    t = np.linspace(-6, 6, 100) # Make array of 100 values

    fig = plt.figure("Sub plots example figure")
    fig.suptitle("Sub plots example title")

    plt.subplot(211)            # 2 rows, 1 col, plot no. 1
    plt.plot(t,f(t))            # Plot the function
    plt.ylabel("d[m]")
    plt.subplot(212)            # 2 rows, 1 col, plot no. 2
    plt.plot(t,df(t))           # Plot the derivative
    plt.xlabel("t[s]")
    plt.ylabel("v[m/s]")

    plt.savefig("plot.eps", format="eps")
    plt.show()                  # Show all subplots in new window

if __name__ == "__main__":
    sub_plots()
