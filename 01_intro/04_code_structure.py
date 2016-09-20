#!/usr/bin/env python
""" This python program illustrates how to structure python programs. """
import os
import sys

def sample_function(msg):
	print(msg)

if __name__ == "__main__":
	print("sys.argv = "+str(sys.argv))          # List of cmd line arguments
	if len(sys.argv) > 1:
		sample_function(sys.argv[1])
	else:
		print("ERROR: too few arguments!")
		print("USAGE: python3 04_code_structure.py 'Some text'")
