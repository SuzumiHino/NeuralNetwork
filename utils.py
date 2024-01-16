from numpy import array

def vars() -> None:
	"""
	...
	"""
	# weights for 3 hidden layers
	weight_in2h = array()
	weight_h2hh = array()
	weight_hh2hhh = array()
	weight_hhh2out = array()

	# bias
	bias_in2h = array()
	bias_h2hh = array()
	bias_hh2hhh = array()
	bias_hhh2out = array()

	epochs = 50
	...

def forwardpropagetion() -> float:
	...

def backpropagagtion():
	...