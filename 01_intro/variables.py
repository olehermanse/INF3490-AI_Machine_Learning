# Python has dynamic types, declaring variables is simple:
name   = "Alice" # String
age    = 23      # Integer
height = 1.76    # Float

# Converting types is straight forward:
age_string    = str(age)
height_string = str(height)
height_cm     = int(height*100)

person = (name, age, height) # Tuple
print(person)
