from math import log10

def check(n, pot):
    t = n
    sum = 0
    while t > 0:
        sum += (t%10)**pot
        t //= 10
    return n == sum

def foo(n):
    num = 10**(n-1)

    while int(log10(num)+1) == n:
        if check(num, n):
            print(num)
        num += 1


foo(int(input()))
