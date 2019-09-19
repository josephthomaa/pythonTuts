import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# Path of the file to read
train_file_path = 'data-titanic/input/train.csv'
test_file_path = 'data-titanic/input/test.csv'

def read_file(path):
    new_data = pd.read_csv(path)
    new_data = new_data.dropna(axis=0)
    new_data['Sex'] = new_data['Sex'].apply(lambda sex: 1 if sex=='male' else 0)
    return new_data

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)    

titan_data = read_file(train_file_path)
#titan_data = titan_data.dropna(axis=0)
#titan_data['Sex'] = titan_data['Sex'].apply(lambda sex: 1 if sex=='male' else 0)
#print(titan_data.head(150))

Y = titan_data.Survived

feature_columns = ['Pclass','Sex','Age','SibSp','Parch']
X = titan_data[feature_columns]

titanic_model = DecisionTreeRegressor(random_state=1)
titanic_model.fit(X, Y)
#print(X.head())

print("Making predictions for the following 5 people:")
print(X.head())
print("The predictions are")
print(titanic_model.predict(X.head()))

#predict error
predicted_person_survival = titanic_model.predict(X)
mae = mean_absolute_error(Y, predicted_person_survival)

train_X, val_X, train_y, val_y = train_test_split(X, Y, random_state = 0)
# Define model
titanic_model = DecisionTreeRegressor()
# Fit model
titanic_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = titanic_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
print(mae)

titanic_max_leaf_nodes = [5, 50, 60, 100, 250, 500]
# Write loop to find the ideal tree size from titanic_max_leaf_nodes
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in titanic_max_leaf_nodes}

# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
best_tree_size = min(scores, key=scores.get)

print('best ',best_tree_size)

# Fill in argument to make optimal size and uncomment
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)

# fit the final model and uncomment the next two lines
final_model.fit(X, Y)
final_model_person_survival = final_model.predict(X)
print(final_model_person_survival)
print(mean_absolute_error(Y, final_model_person_survival))

#Random Forest
# Define the model. Set random_state to 1
rf_model = RandomForestRegressor()
# fit your model
rf_model.fit(train_X, train_y)

# Calculate the mean absolute error of your Random Forest model on the validation data
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))