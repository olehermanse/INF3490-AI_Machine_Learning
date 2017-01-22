# Python has dynamic types, declaring variables is simple:
name   = "Alice" # String
age    = 23      # Integer
height = 1.76    # Float

# Converting types is straight forward:
age_string    = str(age)
height_string = str(height)
height_cm     = int(height*100)

# A tuple is a collection of objects:
person = (name, age, height)
print(person[0]+":")
print(person)

# Mathematical operators:
total     = 10 + 3
diff      = 10 - 3
product   = 10 * 3
real_div  = 10/3	# This will give a float answer in python3 (!)
int_div   = 10//3
remainder = 10%3
exponent  = 10**3   # 10^3 = 1000

print("10/3  = " + str(10/3))
print("10%3  = " + str(10%3))
print("10//3 = " + str(10//3))
print("10**3 = " + str(10**3))
