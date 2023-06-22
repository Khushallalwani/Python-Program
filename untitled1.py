'''
import matplotlib.pyplot as plt 
ages = [2,5,70,40,30,45,50,45,43,40,44, 60,7,13,57,18,90,77,32,21,20,40] 
range = (0, 100) 
bins = 10
plt.hist(ages, bins, range, color = 'green', histtype = 'bar', rwidth = 0.8) 
plt.xlabel('age') 
plt.ylabel('No. of people') 
plt.title('My histogram') 
plt.show()
'''


import matplotlib.pyplot as plt
value1 =[82,76,24,40,67,62,75,78,71,32,98,
89,78,67,72,82,87,66,56,52]
value2=[62,5,91,25,36,32,96,95,3,90,95,32,
27,55,100,15,71,11,37,21]
value3=[23,89,12,78,72,89,25,69,68,86,19,49,
15,16,16,75,65,31,25,52]
value4=[59,73,70,16,81,61,88,98,10,87,29,72,
16,23,72,88,78,99,75,30]
box_plot_data= [value1, value2,value3, value4]
plt.boxplot(box_plot_data)
plt.show()