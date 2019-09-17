import pandas as pd 
titanic_file_path='data-titanic/input/train.csv'
titanic_data=pd.read_csv(titanic_file_path)
#print(titanic_data.describe())
print(titanic_data.columns.tolist())
print("-------")
titanic_features=['PassengerId','Survived','Pclass','Sex','Age']
X = titanic_data[titanic_features]
print(X.head())
