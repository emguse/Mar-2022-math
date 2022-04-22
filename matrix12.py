import numpy as np
import matplotlib.pyplot as plt

p = np.matrix([[3, 3, 5, 5, 3], [3, 1, 1, 3, 3]])

th = np.radians(45)
a = np.matrix([[np.cos(th), np.sin(-th)], [np.sin(th), np.cos(th)]])

p2 = a * p

print(p2)

p = np.array(p)
p2 = np.array(p2)
plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color='0.8')
plt.show()



