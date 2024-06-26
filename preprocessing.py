# import dataset
# Import libraries
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def process_data():
  housing = fetch_california_housing()
  data = pd.DataFrame(housing.data, columns=housing.feature_names)
  data['PRICE'] = housing.target
  
  X = data.drop("PRICE", axis=1)
  y = data["PRICE"]
  
  X_train,X_test,y_train,y_test = train_test_split(X,y, random_state=42)
  
  scaler = StandardScaler()
  X_train = scaler.fit_transform(X_train)
  X_test=scaler.fit_transform(X_test)

  return X_train,X_test,y_train,y_test
