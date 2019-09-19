import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# Path of the file to read
file_path = 'data-titanic/input/train.csv'

titan_data = pd.read_csv(file_path)
#print(titan_data.info())
#import pdb;pdb.set_trace()
titan_data = titan_data.dropna(axis=0)
#titan_data.loc[titan_data['Sex']=='male'] = 1
titan_data['Sex'] = titan_data['Sex'].apply(lambda sex: 1 if sex=='male' else 0)
train_data = titan_data.head(50)

#print(titan_data.head(150)['Sex'])

Y = train_data.Survived

feature_columns = ['Pclass',  'Age', 'SibSp', 'Parch']
X = train_data[feature_columns]

titanic_model = DecisionTreeRegressor(random_state=1)
titanic_model.fit(X, Y)
#print(X.head())



#predict error
test_data = titan_data[:50]
X2 = test_data[feature_columns]
print("Making predictions for the following 50 people:")

print(test_data)
print("The predictions are")

predicted_person_survival = titanic_model.predict(X2)
print(titanic_model.predict(X2))

mae = mean_absolute_error(Y, predicted_person_survival)

print(mae)
