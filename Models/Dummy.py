import random
import numpy as np
#Here is a dummy model.
#Every model must define at least 3 functions :
#fit, predict, and score
#Moreover, a model must define a class of its own name including the 3 overmentioned methods


class Dummy():

	def __init__(self):
		print("Dummy model !")

	#this method sets the parameters of the model
	def fit(self, X, Y):
		print("No fitting needed...")
		return

	def predict(self, X):
		return np.array([random.randint(0,1) for x in X])

	def score(self, X, Y):
		return np.abs(self.predict(X) - Y).mean()
