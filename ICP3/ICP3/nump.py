import numpy as np
x = np.random.randint(1, 20, 15)
b= x.reshape((3, 5))
print(b)
maxv = np.max(b, axis=1)
print(maxv)
print(np.where(b == np.max(b, axis=1, keepdims=True), 0, b))

