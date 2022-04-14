import numpy as np

a = np.matrix([[5, 3], [2, 1]])
a_inv = np.linalg.inv(a)

b = np.matrix([[9], [4]])

print(a_inv * b)