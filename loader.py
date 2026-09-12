import pandas as pd
import joblib
from PIL import Image
from data.config import thresholds



from sklearn.metrics import accuracy_score

data = pd.read_csv('datasets/diabetes.csv')
X = data[['Pregnancies', 'Glucose', 'Insulin', 'BMI', 'Age']]
y = data['Outcome']

page_icon = Image.open("image/page_icon.jpeg")

model = joblib.load('model.pkl')



y_score = model.predict_proba(X)[:, 1]
y_pred = (y_score >= thresholds).astype(int)

# Accuracy Score
accuracy_result = round(accuracy_score(y, y_pred) * 100, 2)
