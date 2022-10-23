def check(a, b, pod):
    tab = []
    while a > 0:
        tab.append(a%pod)
        a //= pod
    while b > 0:
        if b%pod in tab:
            return False
        b //= pod

    return True

def foo(a, b):
    for i in range(2, 17):
        if check(a, b, i):
            return i

    return -1


a = int(input())
b = int(input())
print(foo(a, b))
