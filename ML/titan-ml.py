#data analysis libraries 
import numpy as np
import pandas as pd
#visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from xgboost.sklearn import XGBClassifier


from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score,recall_score,confusion_matrix
#ignore warnings
import warnings
warnings.filterwarnings('ignore')

#import train and test CSV files
train = pd.read_csv('data-titanic/input/train.csv')
test = pd.read_csv('data-titanic/input/test.csv')

#take a look at the training data
print(train.describe(percentiles = [.30, .62]))
print(train.dtypes)
print(train.info())
print('-' * 40)
print(test.info())

#The survival percentage
survived_data = train[train['Survived'] == 1]
survived = survived_data.count().values[1]
survival_percent = (survived/891) * 100
print('The percentage of survived people in training data are {}'.format(survival_percent))

#check for any other unusable values
print(pd.isnull(train).sum())

# *** Data Visualization ***
#draw a bar plot of survival by sex
sns.barplot(x="Sex", y="Survived", data=train)
#print percentages of females vs. males that survive
print("Percentage of females who survived:", train["Survived"][train["Sex"] == 'female'].value_counts(normalize = True)[1]*100)
print("Percentage of males who survived:", train["Survived"][train["Sex"] == 'male'].value_counts(normalize = True)[1]*100)
#plt.show()
#draw a bar plot of survival by Pclass
sns.barplot(x="Pclass", y="Survived", data=train)

#print percentage of people by Pclass that survived
print("Percentage of Pclass = 1 who survived:", train["Survived"][train["Pclass"] == 1].value_counts(normalize = True)[1]*100)
print("Percentage of Pclass = 2 who survived:", train["Survived"][train["Pclass"] == 2].value_counts(normalize = True)[1]*100)
print("Percentage of Pclass = 3 who survived:", train["Survived"][train["Pclass"] == 3].value_counts(normalize = True)[1]*100)


# *** Data cleansing ***
# Removing cabin columns
train = train.drop(['Cabin','Ticket','Name','Fare'], axis = 1)
test = test.drop(['Cabin','Ticket','Name','Fare'], axis = 1)


#plt.show()

# filling missing values in the Embarked feature
print("Number of people embarking in Southampton (S):")
southampton = train[train["Embarked"] == "S"].shape[0]
print(southampton)
print("Number of people embarking in Cherbourg (C):")
cherbourg = train[train["Embarked"] == "C"].shape[0]
print(cherbourg)
print("Number of people embarking in Queenstown (Q):")
queenstown = train[train["Embarked"] == "Q"].shape[0]
print(queenstown)

train = train.fillna({"Embarked": "S"})
#map each Sex value to a numerical value
sex_mapping = {"male": 0, "female": 1}
train['Sex'] = train['Sex'].map(sex_mapping)
test['Sex'] = test['Sex'].map(sex_mapping)

#map each Embarked value to a numerical value
embarked_mapping = {"S": 1, "C": 2, "Q": 3}
train['Embarked'] = train['Embarked'].map(embarked_mapping)
test['Embarked'] = test['Embarked'].map(embarked_mapping)

print(train.head(5))
print(train.shape)
#train = train.dropna(axis=0)
train.Age.fillna(train.Age.mean(), inplace=True)
print(train.shape)

predictors = train.drop(['Survived', 'PassengerId'], axis=1)
target = train["Survived"]
x_train, x_val, y_train, y_val = train_test_split(predictors, target, test_size = 0.22, random_state = 0)

Results = pd.DataFrame({'Model': [],'Accuracy Score': [],"Confusion Matrix":[],
                    "Precision Score":[],"Recall Score":[]})

#DecisionTreeClassifier
titanic_model = DecisionTreeClassifier(criterion="entropy",max_depth=5,
                                class_weight = 'balanced',min_weight_fraction_leaf = 0.009,
                                random_state=1)
titanic_model.fit(x_train, y_train)
y_pred = titanic_model.predict(x_val)
dt_val_mae = mean_absolute_error(y_val, y_pred)
print("\n MAE for DecisionTreeRegressor: {}".format(dt_val_mae))
res = pd.DataFrame({"Model":['DecisionTreeClassifier'],
                    "Accuracy Score": [accuracy_score(y_pred,y_val)],"Confusion Matrix":[confusion_matrix(y_pred,y_val)],
                    "Precision Score":[precision_score(y_pred,y_val)],"Recall Score":[recall_score(y_pred,y_val)]})
                 
Results = Results.append(res)


# Define the RandomForestClassifier. 
rf_model = RandomForestClassifier(n_estimators=2500, max_depth=4)
rf_model.fit(x_train, y_train)
y_pred = rf_model.predict(x_val)
rf_val_mae = mean_absolute_error(y_val, y_pred)

print("\n MAE for Random Forest Model: {}".format(rf_val_mae))
res = pd.DataFrame({"Model":['RandomForestClassifier'],
                    "Accuracy Score": [accuracy_score(y_pred,y_val)],"Confusion Matrix":[confusion_matrix(y_pred,y_val)],
                    "Precision Score":[precision_score(y_pred,y_val)],"Recall Score":[recall_score(y_pred,y_val)]})
Results = Results.append(res)

#KNeighborsClassifier
model = KNeighborsClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_val)
res = pd.DataFrame({"Model":['KNeighborsClassifier'],
                    "Accuracy Score": [accuracy_score(y_pred,y_val)],"Confusion Matrix":[confusion_matrix(y_pred,y_val)],
                    "Precision Score":[precision_score(y_pred,y_val)],"Recall Score":[recall_score(y_pred,y_val)]})
Results = Results.append(res)

#SVM
model = SVC()
model.fit(x_train, y_train)
y_pred = model.predict(x_val)
res = pd.DataFrame({"Model":['SVC'],
                    "Accuracy Score": [accuracy_score(y_pred,y_val)],"Confusion Matrix":[confusion_matrix(y_pred,y_val)],
                    "Precision Score":[precision_score(y_pred,y_val)],"Recall Score":[recall_score(y_pred,y_val)]})
Results = Results.append(res)

#LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_val)
from sklearn.metrics import accuracy_score
res = pd.DataFrame({"Model":['LogisticRegression'],
                    "Accuracy Score": [accuracy_score(y_pred,y_val)],"Confusion Matrix":[confusion_matrix(y_pred,y_val)],
                    "Precision Score":[precision_score(y_pred,y_val)],"Recall Score":[recall_score(y_pred,y_val)]})
Results = Results.append(res)

#XGBClassifier
model = XGBClassifier(learning_rate=0.001,n_estimators=2500,
                                max_depth=4, min_child_weight=0,
                                gamma=0, subsample=0.7,
                                colsample_bytree=0.7,
                                scale_pos_weight=1, seed=27,
                                reg_alpha=0.00006)
model.fit(x_train, y_train)
y_pred = model.predict(x_val)

res = pd.DataFrame({"Model":['XGBClassifier'],
                    "Accuracy Score": [accuracy_score(y_pred,y_val)],"Confusion Matrix":[confusion_matrix(y_pred,y_val)],
                    "Precision Score":[precision_score(y_pred,y_val)],"Recall Score":[recall_score(y_pred,y_val)]})
Results = Results.append(res)
print(Results)
F1_Score = 2*(recall_score(y_pred,y_val) * precision_score(y_pred,y_val)) / (recall_score(y_pred,y_val) + precision_score(y_pred,y_val))
print(F1_Score)
plt.subplots(figsize = (12,8))
sns.lineplot(x="Model", y="Accuracy Score",markers=True, data=Results,lw=1)
plt.show()