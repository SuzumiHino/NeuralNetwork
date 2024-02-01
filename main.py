import numpy as np
# import tensorflow as tf
# import trained
from tqdm import tqdm
from utils import Vars

def epochsprint(function):
	def wrapper(*args, **kwargs):
		print("Training started")
		function()
		print("Training completed")
	return wrapper()
@epochsprint
def main():
	iterated = Vars.epochs
	for epoch in tqdm(range(iterated)):
		print(f"Epoch {epoch+1}: \n")


try:
	lambda x: main()
except TypeError:
	print("Warning: \n  TypeError\n> Script is complete with TypeError")
else:
	print("> Scripts is complete without errors\nVery Good")
finally:
	print("\nProgram completed.")


