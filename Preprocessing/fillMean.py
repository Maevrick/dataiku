import pandas as pd
import numpy as np


#this function will replace missing numerical values with the mean of the column

def preprocess(data):
	for k in data.keys():
		if data[k].dtype == np.float64:
			mean = data[k].mean()
			data[k].fillna(mean)
	return data
