
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

# Builds a Pandas DataFrame from the source data from the URL
df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")

# Un-comment the below lines to see the first few lines of df and a list of its columns.

#print(df.head)
#print(df.columns)

# Organizes the data by average honey production per year and reshapes it to the format needed format for later plotting and linear regression.
prod_per_year = df.groupby('year').totalprod.mean().reset_index()
X = prod_per_year['year']
X = X.values.reshape(-1, 1)

y = prod_per_year['totalprod']

# Builds a linear regression model and train it with our data using .fit
regr = LinearRegression()
regr.fit(X, y)

# Uses the above model to make predictions
y_predict = regr.predict(X)

'''print(regr.coef_) will give you slop of the line
print(regr.intercept_) will give you intercept'''


# Simple scatter plot to show data points and model predictions.
plt.scatter(X, y, alpha=0.4)
plt.plot(X, y, 'o')
plt.plot(X, y_predict, 'o')
plt.title("Honey")
plt.xlabel("Year")
plt.ylabel("Honey Production")
#plt.show()

# Extends the model into the future to predict honey production for years to come.
X_future = np.array(range(2013, 2053))
X_future = X_future.reshape(-1, 1)
future_predict = regr.predict(X_future)

# This gives the last value (2050 honey production)
print(future_predict[-1])

# Displays scatter plot that includes predictions for future years.
plt.plot(X, y, 'o')
plt.plot(X_future, future_predict, 'o')
plt.show()

