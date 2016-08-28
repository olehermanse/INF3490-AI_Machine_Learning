# The simple hello world:
print("Hello, Python!")

# Empty line:
print("")

# Variables:
name = "Alice"
age = 22

# String concatenation:
print(name + " is " + str(age) + " years old.")

# String format:
print("{} is {} years old.".format(name, age))
print("The {1} year old girl {0}".format(name, age))

print("")
print("If {0} beats {1},\n and {1} beats {2},\n then {0} beats {2}"\
      .format("Alice", "Bob", "Eve"))

# Multi line message:
print("")
msg = """Dear reader,
thank you for reading.
-Writer."""
print(msg)
