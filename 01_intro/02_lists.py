# Python has two very important data structures:
l = [] # Lists
d = {} # Dictionaries

# lists are 'like' arrays:
fib = [1, 1, 2, 3]
length = len(fib)
print("{} (length {})".format(fib,length))

# Add element to list:
fib.append(5)
print(fib)

# Remove last element:
fib.pop()
print(fib)

# Delete element by index:
del fib[2]
print(fib)

# It is easy to take out a slice:
fib = fib[0:2] # List elements from index 0 to 2, not including 2
print(fib)

# Loop from 2 to 10, not including 10
for i in range(2,10):
	fib.append(fib[i-1]+fib[i-2])
	print(fib)

# Iterate through list:
for i in range(len(fib)):
	fib[i] = 2*fib[i]
print(fib)

# Or even faster:
fib = [x * 2 for x in fib]
print(fib)
