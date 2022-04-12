import numpy as np

a = np.matrix([[1, 3], [2, 1]])
e = np.matrix([[1, 0], [0, 1]])

print(a * e)
print(e * a)