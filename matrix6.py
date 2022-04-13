import numpy as np

a = np.matrix([[5, 3], [2, 1]])
b = np.linalg.inv(a)

print(b)

a = np.matrix([[1, 3], [2, 1]])
b = np.linalg.inv(a)
print((a * b).astype(np.int64))