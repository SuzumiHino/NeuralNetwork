from numpy import zeros
from numpy.random import uniform

def vars() -> None:
	"""
	...
	"""
	# weights for 3 hidden layers
	weight_in2h = uniform()
	weight_h2hh = uniform()
	weight_hh2out = uniform()

	# bias
	bias_in2h = uniform()
	bias_h2hh = uniform()
	bias_hh2out = uniform()

	epochs = 50
	learning_rate = 0.01

def forwardpropagetion() -> float:
	...

def backpropagagtion():
	...