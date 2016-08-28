#!/usr/bin/env python3
# author: github.com/olehermanse

# import libraries used for plotting and mathematical operations:
import numpy as np
import matplotlib.pyplot as plt

# Define a mathematical expression as a function:
def f(x):
    return x**3

x = np.linspace(-3, 3, 100) # Make array of 100 values between -2 and 3 (linear)
plt.plot(x,f(x))            # Plot the function
plt.show()              # Show all subplots in new window
