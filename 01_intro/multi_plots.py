#!/usr/bin/env python3
# author: github.com/olehermanse

# import libraries used for plotting and mathematical operations:
import numpy as np
import matplotlib.pyplot as plt

# Define a mathematical expression as a function:
def f(x):
    return x**3

def df(x):
    return 3*x**2

x = np.linspace(-2, 3, 100) # Make array of 100 values between -2 and 3 (linear)
plt.subplot(121)            # 1 row of plots, 2 columns of plots, plot number 1
plt.plot(x,f(x))            # Plot the function
plt.subplot(122)            # 1 row of plots, 2 columns of plots, plot number 2
plt.plot(x,df(x))           # Plot the derivative

plt.show()              # Show all subplots in new window
