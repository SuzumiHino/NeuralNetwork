import gensim.downloader as api

# wv = api.load("word2vec-google-news-300")
#
# word1 = "asshole"
#
# print(wv[word1], word1)

# import markdown as md
# text = "**chto?**"
# print(md.markdown(text))



import time
from rich.progress import Progress

def load():
	with Progress() as progress:
		task1 = progress.add_task("[red]Downloading...", total=100)
		task2 = progress.add_task("[green]Processing...", total=100)
		task3 = progress.add_task("[cyan]Installing...", total=100)

		while not progress.finished:
			progress.update(task1, advance=0.9)
			progress.update(task2, advance=0.6)
			progress.update(task3, advance=0.3)
			time.sleep(0.02)
