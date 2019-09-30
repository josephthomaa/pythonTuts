import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")



# Path of the file to read
insurance_filepath = "insurance.csv"

# Read the file into a variable insurance_data
#insurance_data = pd.read_csv("data/insurance.csv")

insurance_data = pd.read_csv('Matplotlib/data/insurance.csv')

print(insurance_data.head())
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
#sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)
sns.swarmplot(x=insurance_data['smoker'],
              y=insurance_data['charges'])
plt.show()