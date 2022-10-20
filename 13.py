def foo(n):
    a = n%10
    n //= 10
    while n > 0:
        if n % 10 == a:
            return False
        n //= 10
    return True

print(foo(int(input())))
