def foo(n):
    i = 1
    a = i*i+i+1
    while a <= n:
        if n%a == 0:
            return True
        i += 1
        a = i*i+i+1
    return False



n = int(input())
print(foo(n))
