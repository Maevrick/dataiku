
all :
	ipython -i -- train.py -i data/train.csv -t Survived -m RFC -a "{'max_depth':1, 'n_estimators':1}" -p myPreprocessing -o output.csv
