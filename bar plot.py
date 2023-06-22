import matplotlib.pyplot as plt
india=['Bikaner','Jaipur','Mumbai','Delhi','Bangalore','Chennai','Kolkata']
pop=[250000,400000,1500000,1600000,1400000,900000,750000]
clr=['y','g','b','r','k','c','brown']
plt.bar(india,pop,color=clr)
plt.xticks()
plt.xlabel("India")
plt.ylabel("Population")
plt.title("Bar Graph")
plt.show()