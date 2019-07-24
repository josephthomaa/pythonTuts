import os
import random
import statistics
from datetime import date
dire=os.getcwd()
#print("Dir = ",dire)
#print(help(os))
a=random.sample(range(100),1)
b=random.randrange(10)

print(a," and b= ",b)

data = [10, 10, 10, 10, 10, 10, 10]
meanr=statistics.mean(data)
med = statistics.median(data)
vari = statistics.variance(data)
#print(meanr," ",med," ",vari)
print(date.today())
