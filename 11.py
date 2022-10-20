def foo(n):
    prev = n%10
    n //= 10
    while n > 0:
        if n % 10 >= prev:
            return False
        prev = n % 10
        n //= 10

    return True


print(foo(int(input())))
