# import the lib

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

# load the data

data = pd.read_csv("diabetes.csv")
print(data.head())

# understand the data

res = data.isnull().sum()
print(res)

# features and target
features = data[["FS","FU"]]
target = data["Diabetes"]

# handle cat data
nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)

# train and test 

x_train, x_test, y_train, y_test = train_test_split(nfeatures,target)

# model

model = RandomForestClassifier(n_estimators=10)
model.fit(x_train,y_train)

# performance
cr = classification_report(y_test, model.predict(x_test))
print(cr)

# save the model

f = None
try:
	f = open("diabetes.model", "wb")
	pickle.dump(model,f)
except Exception as e:
	print("issue",str(e))
finally:
	if f is not None:
		f.close()