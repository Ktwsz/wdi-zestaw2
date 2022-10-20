def foo(n):
    a = 2
    while n >= a:
        if n % a == 0:
            return True
        a = 3*a+1
    return False

print(foo(int(input())))
    