def foo(n):
    t = n
    c = 0
    while t > 0:
        c += 1
        t //= 10
    
    while n > 0:
        if n % 10 == c:
            return True
        n //= 10

    return False

print(foo(int(input())))


