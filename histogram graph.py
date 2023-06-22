import matplotlib.pyplot as plt
import numpy as np
a=np.random.normal(1,5,20)
print(a)
plt.xlabel("chirag")
plt.ylabel("veer")
plt.title("Histogram Graph")
plt.hist(a)
plt.show()
