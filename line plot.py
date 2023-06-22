import matplotlib.pyplot as plt
a=[1,2,3,4,5,6,7]
b=[2,3,4,6,5,6,5]
plt.plot(a,color='b',marker='s',label='in',linestyle='dotted')
plt.plot(b,color='r',marker='s',label='vk',linestyle='dashed')
plt.xlabel('c')
plt.ylabel('b')
plt.title("Line Plot")
plt.legend()
plt.show()


plt.subplot(a,b)
plt.show()