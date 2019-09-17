import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,25,30,25]

x2 = [1,2,3,4,5]
y2 = [5,0,5,10,15]

#plot x, y value in graph with indicating label name
plt.plot(x, y, label='plot1')
plt.plot(x2, y2, label='plot2')
#define name for x and y axis
plt.xlabel('Plot Number', fontdict=None, labelpad=None)
plt.ylabel('Value', fontdict=None, labelpad=None)
plt.title('First Plot', fontdict=None, loc='center', pad=None)
plt.legend()

plt.show()

