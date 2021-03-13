
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

'''print(regr.coef_) will give you slop of the line
print(regr.intercept_) will give you intercept'''

X_future = np.array(range(2013, 2051))
X_future = X_future.reshape(-1, 1)

future_predict = regr.predict(X_future)

#plt.plot(X, y, 'o')
plt.plot(X_future, future_predict, 'o')
plt.show()
print(future_predict[-1]) # This gives the last value (2050 honey production)
