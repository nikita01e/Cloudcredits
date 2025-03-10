# -*- coding: utf-8 -*-
"""house price prediction .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1934TzNH0eSc-UTmrXyYkxzdizINZBNeD
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score

df=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/housing 2.csv')
df.head()

df.describe()

df.isnull().sum()

import pandas as pd

df = df[['price', 'bedrooms', 'bathrooms', 'sqft_lot', 'floors', 'view', 'yr_built', 'street', 'city']]
print("Original DataFrame:")
print(df)

df['price'] = df['price'].astype(float)

print("\nDataFrame after converting 'Price' to string:")
print(df)

df.columns

sns.pairplot(df)

x=df[['bedrooms','bathrooms','sqft_lot','floors','view','yr_built','street','city']]
y=df['price']

le=LabelEncoder()

x['street_encoded'] = le.fit_transform(x['street'])
x['city_encoded'] = le.fit_transform(x['city'])

x=x.drop(['street','city'],axis=1)

numerical_features = df.select_dtypes(include=np.number).columns.tolist()
correlation_matrix = df[numerical_features].corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

model=LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

mse = mean_absolute_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print("Mean Absolute error: ",mse)
print("r2 Score:",r2)

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs. Predicted Prices")
plt.show()

residuals = y_test - y_pred
plt.scatter(y_test, residuals)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel("Actual Prices")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()

new_data = [[5, 3, 2000, 6000, 2, 0, 0, 2]]
predicted_price = model.predict(new_data)

print("Predicted Price:", predicted_price[0])





