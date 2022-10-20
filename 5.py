def check(n, a):
    while n > 0:
        if n % 10 == a % 10:
            a //= 10
        n //= 10
    return a == 0


def foo(n):
    a = 7
    ans = 0
    while a <= n:
        if check(n, a):
            ans += 1
        a += 7
    return ans

print(foo(int(input())))
