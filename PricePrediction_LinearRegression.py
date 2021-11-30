import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Get and clean data
df = pd.read_csv('***.csv') # Local path: .csv file containing price data
df.drop(df.columns[6:], axis=1, inplace=True)
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

# Variable for predicting n days to future
pred_future = 14
# Prediction column to contain close values shifted 'pred_future' amount upwards.
df['Prediction'] = df[['Close']].shift(-pred_future)

# Independed dataset with last 14 rows removed
X = np.array(df[['Close']])
X = X[:-pred_future]
print(X)

# Dependent dataset
y = df['Prediction'].values
y = y[:-pred_future]
print(y)

# Split into train/test (75/25)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25)

# Create and train model
lr = LinearRegression()
lr.fit(X_train,y_train)

# Test the model
lr_confidence = lr.score(X_test, y_test)
print('Linear Regression Confidence: ', lr_confidence)

# X_pred equals to last 'pred_future' amount of rows from the original dataset
X_pred = np.array(df[['Close']])[-pred_future:]
print(X_pred)

# Predict the price for next 'pred_future' days.
lr_pred = lr.predict(X_pred)
print(lr_pred)