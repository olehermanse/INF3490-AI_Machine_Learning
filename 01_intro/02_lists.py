# Python has two very important data structures:
l = [] # Lists
d = {} # Dictionaries

# lists are 'like' arrays:
fibonacci = [1, 1, 2, 3, 5, 8]
# Add element to list:
fibonacci.append(13)
print(fibonacci)
# It is easy to take out a slice:
part = fibonacci[0:2]
print(part)
for i in range(2,10):
	part.append(part[i-1]+part[i-2])

print(part)
