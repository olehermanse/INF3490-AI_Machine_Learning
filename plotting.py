# import libraries used for plotting and mathematical operations:
import numpy as np
import matplotlib.pyplot as plt

# Define a mathematical expression as a function:
def f(x):
    return -x**4 + 2*(x**3) + 2*(x**2) - x

# and its derivative:
def df(x):
    return -4*(x**3) + 6*(x**2) + 4*x - 1

x = np.linspace(-2, 3, 100)     # Make array of 100 values between -2 and 3 (linear)
plt.subplot(121)                # 1 row of plots, 2 columns of plots, plot number 1
plt.plot(x,f(x))                # Plot the function
plt.subplot(122)                # 1 row of plots, 2 columns of plots, plot number 2
plt.plot(x,df(x))               # Plot the derivative

#plt.show() # We will add some more to the plot, so dont show() yet

# One way to do exhaustive search in 1 dimension
def exhaustive(start, stop, step):
    cur = start                 # The current x value
    maximum = f(start)          # The highest visited y value, initialized to first value
    while(cur<=stop):           # Step through range from start to stop
        if(f(cur) > maximum):   # Check for new maximum
            maximum = f(cur)    # Set new maximum
        cur += step             # Step to next x
    
    # Should be improved to return (x,y) of maximum
    return maximum              # Return the highest value found

res = exhaustive(-2,3,0.5)
print 'result: ', res

# Add result from exhaustive search to plot number 1
plt.subplot(121)
plt.plot(2, res, 'bs')  # plot blue square at (2, res)
plt.show()              # Show all subplots in new window