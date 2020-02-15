import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn import preprocessing
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

train_df = pd.read_csv('drive/My Drive/Colab Notebooks/glass.csv')
X = train_df.drop("Type",axis=1)
Y = train_df["Type"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
svc = SVC()
svc.fit(X_train, y_train)
Y_pred = svc.predict(X_test)
acc = round(svc.score(X_train, y_train)*100,2)
print("accuracy", acc)
