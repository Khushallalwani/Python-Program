import matplotlib.pyplot as plt
import numpy as np

a=[1,2,3,8,4,5,6,7]
b=[21,3,12,4,5,16,7,8]
plt.scatter(a,b,marker='*')
plt.legend(a)
plt.title("Scatter Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid()
plt.show()

'''
t=np.random.normal(5,1,100)
z=np.random.normal(5,1,100)
plt.scatter(t,z)
plt.show()
'''