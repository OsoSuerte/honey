
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")
prod_per_year = df.groupby('year').totalprod.mean().reset_index()

X = prod_per_year['year']
X = X.values.reshape(-1, 1)

y = prod_per_year['totalprod']



regr = LinearRegression()
regr.fit(X, y)
y_predict = regr.predict(X)

plt.scatter(X, y, alpha=0.4)
# Plot line here:

plt.plot(X, y, 'o')
plt.plot(X, y_predict, 'o')

plt.title("Honey")
plt.xlabel("Year")
plt.ylabel("Honey Production")
plt.show()



