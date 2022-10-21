def foo(k, n):
    x = (k-1)/n
    ans = 0
    for i in range(n):
        m = 1 + (k-1)/(2*n)
        ans += x*1/(m+i*x)
    return ans


print(foo(int(input()), 1000000))

