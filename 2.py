def foo(a, b, n):
    for i in range(n):
        a %= b
        a *= 10
        print(int(a/b))

a = int(input())
b = int(input())
n = int(input())

foo(a, b, n)
