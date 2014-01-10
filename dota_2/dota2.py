
# Importing the libraries

import sys

import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier


##########################
# Data manipulation
##########################

# Loading the data

# Training set
data = np.recfromcsv('trainingdata.txt')

# Test set
data_test = map(lambda x: x.strip().split(','), sys.stdin.readlines())
data_test = data_test[1:]

# Transform the record array into regular array

# Training set
data = np.array(data.tolist())

# Test set
data_test = np.asarray(data_test)

##########################
# Dealing with the heroes
##########################

heroes = set()
heroes_dict = {}

# We get all the unique names of the heroes
for i in data[:,3]:
	heroes.add(i)

# Each name is associated with a unique value
for k,v in enumerate(heroes):
    heroes_dict[v] = k 

#############################################
# Transforming the text in data into integers
#############################################

# Training set
for j in xrange(len(data)):
    for i in range(10):
       data[j][i] = heroes_dict[data[j][i]]

# Test set
for j in xrange(len(data_test)):
    for i in range(10):
       data_test[j][i] = heroes_dict[data_test[j][i]]

print data_test

####################
# Building the model
####################

labels = data[:, 10]

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.10)

clf = RandomForestClassifier()

clf = clf.fit(x_train, y_train)

preds = clf.predict(data_test)

print preds


[ x for x in input if any(map(lambda w: sorted(x) == sorted(w) and x != w, input)) ]
