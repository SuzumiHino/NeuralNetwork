import gensim.downloader as download_api
from numpy.random import uniform
from numpy import zeros

# en_model = download_api("word2vec-google-news-300")

def vars():
	"""
	...
	"""
	# weights for 3 hidden layers
	weight_in2h = uniform(-1, 1, ())
	weight_h2hh = uniform(-1, 1, ())
	weight_hh2out = uniform(-1, 1, ())

	# bias
	bias_in2h = zeros(())
	bias_h2hh = zeros(())
	bias_hh2out = zeros(())

	epochs = 50
	learning_rate = 0.01

def forwardpropagetion():
	...

def backpropagagtion():
	...