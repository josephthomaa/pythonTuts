# Code you have previously used to load data
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
# Import the train_test_split function and uncomment
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Path of the file to read
iowa_file_path = 'data/train.csv'

home_data = pd.read_csv(iowa_file_path)
#print(home_data.head())
y = home_data.SalePrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_columns]

# Specify Model
iowa_model = DecisionTreeRegressor()
# Fit Model
iowa_model.fit(X, y)

#split data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

iowa_model2 = DecisionTreeRegressor(random_state=1)
iowa_model2.fit(train_X, train_y)

val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)

print("mean_absolute_error : ", val_mae)

print("First in-sample predictions:", iowa_model.predict(X.head()))
print("Train2 : ",iowa_model2.predict(train_X.head()))
print("Actual target values for those homes:", y.head().tolist())