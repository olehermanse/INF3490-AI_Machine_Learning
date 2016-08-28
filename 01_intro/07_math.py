#!/usr/bin/env python3
""" Simple numpy demo"""
import os
import sys
import numpy as np

def numpy_demo():
	print("NumPy has a lot of standard math functions and constants:")
	print("np.linspace(0,1,11): "+str(np.linspace(0,1,11)))
	print("np.pi:               "+str(np.pi))
	print("np.e:                "+str(np.e))
	print("np.sin(np.pi/2):     "+str(np.sin(np.pi/2)))

	print("Numpy has matrices:")
	a = np.matrix([[1,2],[3,4],[5,6]], dtype=float)
	b = np.matrix(np.zeros((2,3)))
	b[1,1] = 1.0

	print("a{} = ".format(a.shape))
	print(a)
	print("b{} = ".format(b.shape))
	print(b)

	ab = a.dot(b)
	print("a . b = a * b = ")
	if not np.array_equal(ab, a*b):
		print("These should be the same!")
		sys.exit(1)
	print(ab)

if __name__ == "__main__":
	numpy_demo()
