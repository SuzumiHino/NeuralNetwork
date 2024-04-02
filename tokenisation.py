import sys
import gensim
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

f = 'sext.txt'
data = gensim.models.word2vec.LineSentence(f)
model = gensim.models.Word2Vec(data, size=500, window=10, min_count=2, sg=0)
model.init_sims(replace=True)
print(len(model.wv.vocab))
model.save('.model')