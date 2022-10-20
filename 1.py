from operator import truediv


def gen(a, b, n):
    c, d = a, b
    while d <= 1000000:
        c, d = d, c+d
        if c * a == n:
            return True
    return False

def foo(n):
    a, b = 0, 1
    while b <= 1000000:
        a, b = b, a+b
        if n % a == 0:
            if gen(a, b, n):
                return True
    return False

print(foo(int(input())))


