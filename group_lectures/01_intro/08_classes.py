#!/usr/bin/env python3
""" Illustrates classes in Python. """
import os
import sys

class Vehicle:
	count = 0
	objects = []

	# Constructor:
	def __init__(self, name, weight):
		# Attributes / Variables specific to this object:
		self.name = name
		self.weight = weight

		# Class Variables:
		Vehicle.count += 1
		Vehicle.objects.append(self)

	def rm(self):
		Vehicle.objects.remove(self)

	# Called when reference counter hits 0
	def __del__(self):
		Vehicle.count -= 1

	def print_vehicle(self):
		print("'{}' weighs {} kg.".format(self.name, self.weight))

	@classmethod
	def get_all(cls):
		return cls.objects

	@classmethod
	def print_all(cls):
		class_name = cls.__name__
		class_count = cls.count
		print("{}s({}):".format(class_name, class_count))
		# Ex: "Cars(3):""
		for x in cls.get_all():
			x.print_vehicle()

class Car(Vehicle):
	count = 0
	objects = []
	def __init__(self, name, weight):
		super(Car,self).__init__(name, weight)
		Car.count += 1
		Car.objects.append(self)

	# Called when reference counter hits 0
	def __del__(self):
		super(Car,self).__del__()
		Car.count -= 1

	def rm(self):
		Car.objects.remove(self)
		super(Car,self).rm()

	def print_vehicle(self):
		print("'{}' is a Car and weighs {} kg.".format(self.name, self.weight))

def classes_demo():
	a = Vehicle("Olabil", 293.928)
	a = Car("Mom's car", 432.1)
	a = Car("Dad's car", 350.0)
	a = Car("Visitor's car", 350.0)
	a.rm()
	a = Car("Alice's car", 350.0)

	Vehicle.print_all()
	Car.print_all()

if __name__ == "__main__":
	classes_demo()
