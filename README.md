#README


##Parameters
The scripts takes as input the following parameters :
	-i Input csv file
	-t Target feature
	-m Model (one of the model defined in the Models/ directory)
	-a Model's parameters (as a dict-like string on the command line) ex : "{'max_depth':3, 'n_estimators':100}"
	-p Preprocessing method, called before the training (one of the methods defined in the Preprocessing/ directory)
	-o The output file containing the predicted column


##Dataflow
The input file will be loaded and preprocessed thanks to the function specified trought the -p parameter.
The target column will be extracted and the data will be splited in half (test/train).
The model will be fited on the train data then evaluated on the test data.
The prediction will be computed on the whole data and exported to the output csv file.


##Exemple : 

ipython -i -- train.py -i data/train.csv -t Survived -m RFC -a "{'max_depth':3, 'n_estimators':10}" -p myPreprocessing -o output.csv


##Adding your own modules
###Models
To add a model, simply create a .py file under the Models/folder.
The model must define a class named as the file.
Therefore, at least 3 functions must be defined, fit, predict and score.
See Models/Dummy.py.
###Preprocessing functions
To add a preprocessing function create a py file under Preprocessing/.
The .py file must contain at least one function named preprocess.
See Preprocessing/Dummy.py.
