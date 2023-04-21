import numpy as np
from sklearn.linear_model import LinearRegression
import csv
import joblib

X = []
y = []
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        X.append(row[1:])
        y.append(row[0])
n = len(X)
X = np.array(X[:], dtype="float")
y = np.array(y[:], dtype="float")
MAX = np.amax(X, axis=0)  # max cua hang
MIN = np.amin(X, axis=0)  # min cua hang
att = [1, 3, 1, 1, 3, 1, 1, 1, 1, 2]
for i in X:
    for j in range(0, len(i)):
        i[j] = (i[j] - MIN[j]) ** att[j]
X_train = np.array(X[:int(n * 8 / 10)], dtype="float")
y_train = y[:int(n * 8 / 10)]
X_val = X[int(n * 8 / 10):]
y_val = y[int(n * 8 / 10):]
model = LinearRegression().fit(X_train, y_train)
val = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1]])
print(model.score(X_train, y_train))
print(model.score(X_val, y_val))
print(model.predict(val[0:1]))

model_path = "model.sav"
joblib.dump(model, model_path)

model = joblib.load(model_path)
val = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1]])
print(model.score(X_train, y_train))
print(model.score(X_val, y_val))
print(model.predict(val[0:1]))
