# Python has two very important data structures:
l = [] # Lists
d = {} # Dictionaries

print("Lists are 'like' arrays. Lets create and manipulate a list:")
fib = [1, 1, 2, 3]
length = len(fib)
print("{} (length {})".format(fib,length))

print("Add 5 to end of list:")
fib.append(5)
print(fib)

print("Remove last element:")
fib.pop()
print(fib)

print("Delete element at index 2:")
del fib[2]
print(fib)

print("Get slice 0:2 from list:")
fib = fib[0:2] # List elements from index 0 to 2, not including 2
print(fib)

print("Generate the first 10 fibonacci numbers using a for loop:")
# Loop from 2 to 10, not including 10
for i in range(2,10):
	fib.append(fib[i-1]+fib[i-2])
print(fib)

print("Double all numbers in list using a for loop:")
# Iterate through list:
for i in range(len(fib)):
	fib[i] = 2*fib[i]
print(fib)

print("Halve all numbers in list using one line for loop:")
fib = [x // 2 for x in fib] # Dividing to reverse last doubling
print(fib)
