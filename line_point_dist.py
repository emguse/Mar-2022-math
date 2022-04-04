import math

x = 1
y = 6

# y=(3/4)x-1
# 3x-4y-4=0
# a=3, b=-4, c=-4
a = 3
b = -4
c = -4

d = math.fabs(a*x + b*y + c) / math.sqrt(a**2 + b**2)

print(d)