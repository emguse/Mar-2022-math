from turtle import color
import matplotlib.pyplot as plt
import numpy as np

r = 300
x = np.arange(-r, r + 1)
y = np.sqrt(r ** 2 - x ** 2)

plt.plot(x, y)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()