import random
numbers = random.sample(range(1,101), 10)
print(numbers)



import numpy as np
numbers = np.random.choice(np.arange(1, 11), 10, replace=False)
print(numbers)
