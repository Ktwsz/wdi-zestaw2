from math import log
def foo(eps):
    b = 5
    prev = 0
    while abs(b - prev) > eps:
        prev = b
        a = b**b*(1+log(b))
        b = b**b-2022-a*b
        b = -b/a
    return b

EPS = 0.000000001
print(foo(EPS))

