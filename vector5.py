import math
import numpy as np

a = np.array([2, 7])
b = np.array([6, 1])
c = np.array([2, 3])
d = np.array([6, 5])


va = b - a
vb = d - c

# Vector magnitude
norm_a = np.linalg.norm(va)
norm_b = np.linalg.norm(vb)

# inner product of vectors
dot_ab = np.dot(va, vb)

cos_th = dot_ab / (norm_a * norm_b)
rad = math.acos(cos_th)
deg = math.degrees(rad)
print(deg)