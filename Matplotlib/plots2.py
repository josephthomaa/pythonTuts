import matplotlib.pyplot as plt

population_ages = [22,25,29,5,32,33,40,45,47,48,52,56,63,75,77,80,81,82,95]
#ids = [x for x in range(len(population_ages))]

x = [1,2,3,4,5,6,7,8]
y = [7,4,2,6,4,1,6,3]
#histogram
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('matplotlib \n Histogram')

plt.show()

#scatter plot
plt.scatter(x,y, label = 'scatterplot', color='g' ,s =100 ,marker = '*')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('matplotlib \n scatterplot')
plt.legend()
plt.show()   

#slackplot

days = [1,2,3,4,5]

sleeping = [7,7,7,7,8]
eating = [2,2,3,2,2]
working = [10,11,9,12,10]
playing = [5,4,5,3,4]

#adding legend in stackplot
plt.plot([], [], color='m', label='Sleeping', linewidth=5)
plt.plot([], [], color='c', label='Eating', linewidth=5)   
plt.plot([], [], color='r', label='Working', linewidth=5)   
plt.plot([], [], color='k', label='Playing', linewidth=5)     

plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','k']) 

plt.xlabel('x')
plt.ylabel('y')
plt.title('stackplot')
plt.legend()
plt.show()                                                                                          