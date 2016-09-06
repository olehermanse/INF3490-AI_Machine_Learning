#!/usr/bin/env python3
""" Illustrates classes in Python. """
import os
import sys

class Vehicle:
	count = 0

	# Constructor:
	def __init__(self, name, weight):
		# Attributes / Variables specific to this object:
		self.name = name
		self.weight = weight

		# Class Variables:
		Vehicle.count += 1

	# Called when reference counter hits 0
	def __del__(self):
		Vehicle.count -= 1

	def print_vehicle(self):
		print("'{}' is a {} and weighs {} kg."\
		      .format(self.name, type(self).__name__, self.weight))

class Car(Vehicle):
	count = 0
	def __init__(self, name, weight):
		super(Car,self).__init__(name, weight)
		Car.count += 1

	# Called when reference counter hits 0
	def __del__(self):
		super(Car,self).__del__()
		Car.count -= 1

def classes_demo():
	a = Vehicle("Olabil", 293.928)
	b = Car("Ghosts BMW", 432.1)

	# This will delete the previous car: (!)
	b = Car("Alice's Ford", 350.0)
	print("Vehicles: " + str(Vehicle.count))
	print("Cars: " + str(Car.count))

	a.print_vehicle()
	b.print_vehicle()

if __name__ == "__main__":
	classes_demo()
