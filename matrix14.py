import numpy as np
import matplotlib.pyplot as plt

p = np.matrix([[1, 3, 3, 1], [1, 1, 2, 1], [1, 1, 1, 1]])

a = np.matrix([[1, 0, 2], [0, 1, 3], [0, 0, 1]])

th = np.radians(45)
b = np.matrix([[np.cos(th), np.sin(-th), 0], [np.sin(th), np.cos(th), 0], [0, 0, 1]])

p2 = b * a * p

print(p2)

p = np.array(p)
p2 = np.array(p2)
plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color='0.8')
plt.show()



