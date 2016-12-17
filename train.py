import importlib
import os
import sys
import getopt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import ast

args,_ = getopt.getopt(sys.argv[1:], "i:t:m:a:p:o:")
args = dict(args)
if not ("-i" in args and "-m" in args and "-t" in args):
	print("USAGE : train.py -i inputFile -t target -m model")
	quit()



target = args["-t"]
preprocessing = args["-p"]
modelParameters = ast.literal_eval(args["-a"])
model = getattr(importlib.import_module("Models."+args["-m"]), args["-m"])(**modelParameters)
pre = getattr(importlib.import_module("Preprocessing."+args["-p"]), "preprocess")
data = pre(pd.read_csv(args["-i"]))
outputFile = args["-o"]

os.system("clear")


print("\nInput file : "+args["-i"])
print("Target : "+args["-t"])
print("Model : "+args["-m"])
print("Models parameters : "+args["-a"])
print("Preprocessing method : "+args["-p"])
print("Output file : "+args["-o"])

Y = data[target]
X = data.drop(target, axis=1)

msk = np.random.rand(len(X)) < 0.5

trainX = X[msk]
testX = X[~msk]
trainY = Y[msk]
testY = Y[~msk]

model.fit(trainX, trainY)

print("Train score = " + str(model.score(trainX, trainY)))
print("Test score = " + str(model.score(testX, testY)))

pd.DataFrame(model.predict(X), columns=[target]).to_csv(outputFile)
