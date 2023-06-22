import matplotlib.pyplot as plt
a=[12,14,15,16,17]
b=['one','two','three','four','five']
t=[0,0,0,0.5,0]
plt.pie(a,labels=b,explode=t,shadow=True)
plt.legend(title='Number :')
plt.show()