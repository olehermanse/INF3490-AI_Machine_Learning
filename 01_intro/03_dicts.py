# dictionaries are 'like' hash-maps:
database = {}                  # empty dict
database = {"boss": "Foo Bar"} # dict with data

# Add a key value pair to a dictionary:
database["foo"] = "test"

person = {}
name, age, height     = "Alice", 23, 1.8
person["age"]         = age
person["height"]      = height
person["description"] = "{} is a {} year old, {}m tall girl."\
                        .format(name,age,height)

# Dictionary in dictionary:
database[name] = person

# List in dictionary:
database["fib_numbers"] = [1,1,2,3,5]

# Print using JavaScript Object Notation:
import json
print(json.dumps(database, indent=2))
