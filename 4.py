from math import log2
def foo(n):
    i = int(log2(n))

    ans = 0

    for j in range(i+1):
        for k in range(i+1):
            for z in range(i+1):
                if 2**j*3**k*5**z <= n:
                    ans += 1

    return ans

print(foo(int(input())))

