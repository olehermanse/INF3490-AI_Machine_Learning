# Python has two very important data structures:
l = [] # Lists
d = {} # Dictionaries

# lists are 'like' arrays:
fibonacci = [1, 1, 2, 3, 5, 8]
# Add element to list:
fibonacci.append(13)

# dictionaries are 'like' hash-maps:
database = {"boss": "Foo Bar"}

# Add a key value pair to a dictionary:
database["foo"] = "test"

person = {}
person["age"]         = age
person["height"]      = height
person["description"] = "{} is a {} year old, {}m tall girl."\
                        .format(name,age,height)

database[name] = person

# Python is dynamically typed, so we don't need to worry about types:
database["fib_numbers"] = fibonacci

# Print using JavaScript Object Notation:
import json
print(json.dumps(database, indent=2))
