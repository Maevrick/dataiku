#this function calls both lEncoder and fillNa preprocessers

import lEncoder
import fillMean

def preprocess(data):
	data = fillMean.preprocess(data)
	return lEncoder.preprocess(data)
