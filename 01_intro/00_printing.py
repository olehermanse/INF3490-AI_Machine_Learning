# The simple hello world:
print("Hello, Python!")

# Empty line:
print("")

# Multi line message:
msg = """Dear reader,
thank you for reading.
- Writer.
"""
print(msg)

# Variables:
name = "Alice"
age = 22

# Printing variables:
print(name + " is " + str(age) + " years old. (String concat)")
print("{} is {} years old. (String format)".format(name, age))

# .format is sometimes very useful:
print("\nIf {0} beats {1},\n and {1} beats {2},\n then {0} beats {2}"\
      .format("Alice", "Bob", "Eve"))
