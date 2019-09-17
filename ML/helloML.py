# Load libraries 

import pandas 
from pandas.plotting import scatter_matrix 
import matplotlib.pyplot as plt 
from sklearn import model_selection 
from sklearn.metrics import classification_report 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
from sklearn.naive_bayes import GaussianNB 
from sklearn.svm import SVC 


url ="data/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 
		'petal-width', 'class'] 
dataset = pandas.read_csv(url, names = names) 

# shape 
# displays total rows and columns
#print(dataset.shape) 

# list the data
print(dataset.head(150))
#print(list(dataset.columns.values))
print("----------------------------------")
#class distribution

print(dataset.groupby('class').size())


#Data Visualization 
## Univariate plots - plots of each individual variable
# box and whisker plots 
dataset.plot(kind ='box', subplots = True, 
			layout =(2, 3), sharex = False, sharey = False) 
#plt.show() 

#histograms
dataset.hist()
plt.show()
