"""
This script trains a Logistic Regression model on the Iris dataset
and saves it to disk for later use in an API.

Steps:
1. Load the Iris dataset (features: sepal length/width, petal length/width; 
   targets: species labels 0=Setosa, 1=Versicolor, 2=Virginica).
2. Train a multi-class Logistic Regression classifier to learn the 
   relationship between flower measurements and species.
3. Save the trained model as 'iris_model.joblib' using joblib so it can be 
   quickly loaded and used for predictions without retraining.

The saved model is later loaded in a FastAPI application to classify new
flower measurements sent via an API request.
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

# load example dataset
iris = load_iris()
X, y = iris.data, iris.target

# train a model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# snave the model to disk
joblib.dump(model, "iris_model.joblib")
print("Model saved as iris_model.joblib")