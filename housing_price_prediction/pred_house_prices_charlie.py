import sys
import numpy as np
from sklearn import linear_model

# Reading and formating the input
input = sys.stdin.readlines()

formated = [row.split() for row in input]

col,row = int(formated[0][0]), int(formated[0][1])

train_set = np.matrix(formated[1:row]).astype(float)

# Dividing target and predictors
X_train = train_set[:, :col]
y_train = train_set[:, col]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train)

test_row = int(formated[row+1][0])

X_test = np.matrix(formated[row+2:row+2+test_row]).astype(float)

y_pred = regr.predict(X_test)

print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      for row in y_pred]))
