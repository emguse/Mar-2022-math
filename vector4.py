from sympy import Symbol, solve

a = Symbol('a')
b = Symbol('b')

ex1 = -1 * a + b - 2
ex2 = 2 * a + b - 4

print(solve((ex1, ex2)))
