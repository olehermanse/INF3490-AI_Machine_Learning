#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This python program illustrates how to structure python programs. """
import os
import sys

def sample_function(msg):
	print(msg)

if __name__ == "__main__":
	print(sys.argv)              # List of cmd line arguments
	sample_function(sys.argv[1])
