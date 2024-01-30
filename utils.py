import gensim.downloader as download_api
from numpy.random import uniform
from numpy import zeros

# en_model = download_api("word2vec-google-news-300")

def vars():
	"""
	...
	"""
	# weights for 3 hidden layers
	weight_in2h = uniform(-1, 1, (50, "x")) # uniform(min, max, (out, in))
	weight_h2hh = uniform(-1, 1, (50, 50))
	weight_hh2out = uniform(-1, 1, ())

	# bias
	bias_in2h = zeros((50, 1)) # zeros(out, 1)
	bias_h2hh = zeros((50, 1))
	bias_hh2out = zeros((0, 1))

	epochs = 50
	learning_rate = 0.01

def forwardpropagetion():
	...

def backpropagagtion():
	...