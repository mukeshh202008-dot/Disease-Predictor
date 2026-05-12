import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Dataset
data = {
    'fever': [1,1,0,1,0,0,1],
    'cough': [1,1,0,0,1,0,1],
    'headache': [1,0,1,1,0,1,1],
    'tiredness': [1,1,1,0,0,1,1],
    'cold': [0,1,0,1,1,0,1],
    'disease': ['Flu','Cold','Migraine','Flu','Cold','Migraine','Flu']
}

df = pd.DataFrame(data)

X = df[['fever','cough','headache','tiredness','cold']]
y = df['disease']

model = DecisionTreeClassifier()
model.fit(X, y)

def predict_disease(symptoms):
    prediction = model.predict([symptoms])
    return prediction[0]