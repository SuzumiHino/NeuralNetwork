import numpy as np
# import tensorflow as tf
import time
# from tqdm import tqdm
from utils import Vars
from rich.progress import Progress
# import trained

# def epochsprint(func):
# 	def wrapper(*args, **kwargs):
# 		print("Training started")
# 		func()
# 		print("Training completed")
# 	return wrapper()

def nn():
	for i in range(100000):
		return i + i

def load(epochs: int):
	with Progress() as progress:
		task1 = progress.add_task("[red]Downloading...", total=epochs)

		while not progress.finished:
			progress.update(task1, advance=0.9)
			nn()

def main():
	load(Vars.epochs)