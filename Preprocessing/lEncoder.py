from sklearn import preprocessing

#this function will treat non-categorical data
def preprocess(data):
	lEncoder = preprocessing.LabelEncoder()
	for i in data.keys():
		data[i] = lEncoder.fit_transform(data[i])
	return data
