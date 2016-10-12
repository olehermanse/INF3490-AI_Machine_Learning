''' Feel free to use numpy for matrix multiplication and
	other neat features.
	You can write some helper functions to
	place some calculations outside the other functions
	if you like to.

	This pre-code is a nice starting point, but you can
	change it to fit your needs.
'''
import numpy as np

class mlp:
	def __init__(self, inputs, targets, nhidden):
		self.beta = 1
		self.eta = 0.1
		self.momentum = 0.0

		print('To be implemented')

	def earlystopping(self, inputs, targets, valid, validtargets):
		print('To be implemented')

	def train(self, inputs, targets, iterations=100):
		print('To be implemented')

	def forward(self, inputs):
		print('To be implemented')

	def confusion(self, inputs, targets):
		print('To be implemented')
