import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


disease = pd.read_csv('/Users/khuyentran/Desktop/heart.csv')
disease.describe()


# Good news. No missing data


X = disease.drop(['target','fbs'],axis=1)
y = disease['target']


from sklearn.ensemble import RandomForestClassifier

forest_clf = RandomForestClassifier(random_state=1)
forest_clf.fit(X, y)

#Save the model
from sklearn.externals import joblib

joblib.dump(forest_clf, 'forest.pkl')
print('Model dumped')

forest_clf = joblib.load('forest.pkl')

model_columns = list(X.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print('Models columns dumped')


