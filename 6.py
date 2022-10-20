def foo(n):
    i = 2
    ans, m = 1, n-1
    while i*i <= n:
        if n % i == 0:
            if abs(i-n/i) < m:
                ans, m = i, abs(i-n/i)
        i += 1
    return ans

n = int(input())
a = foo(n)
print(a, n//a)
