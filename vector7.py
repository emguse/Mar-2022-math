import numpy as np

a = np.array([2, 4])
b = np.array([3, 1])
cross_ab = np.cross(a, b)
s = np.linalg.norm(cross_ab)
print(s / 2)