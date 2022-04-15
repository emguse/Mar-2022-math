
# ax + by = s
# cx + dy = t
# [[a, b], [c, d]] * [[x, y]] = [[s, t]] 

a = 5
b = 3
c = 2
d = 1
s = 9
t = 4

k = a * d - b * c
x = ((d/k)*s) + ((-b/k)*t)
y = ((-c/k)*s) + ((a/k)*t)

print(x, y)