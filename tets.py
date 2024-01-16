import gensim.downloader as api

wv = api.load("word2vec-google-news-300")

word1 = "asshole"

print(wv[word1], word1)