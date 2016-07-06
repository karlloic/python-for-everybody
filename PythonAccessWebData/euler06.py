# Project Euler Problem 6

r = range(101)
s = sum(r)
print(s * s - sum(x * x for x in r))
