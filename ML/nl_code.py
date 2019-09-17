import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

titanic_data = pd.read_csv('data/car_sale.csv')
titanic_data.info()

# titanic_data['Month'] = titanic_data.apply(lambda row: row[0].split("-")[1], axis=1)
# month = titanic_data['Month']
sale = titanic_data['Sales']
# bins represents the number of bars needs to be shown
bins = plt.hist(sale, bins=20)
# this used to define the y axis
plt.yticks(range(1, 13))
plt.xlabel("Sales")
plt.ylabel("Month")

plt.show()