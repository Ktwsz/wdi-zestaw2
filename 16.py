def p(n):
    i = 2
    ans = 0
    while n > 1:
        if n % i == 0:
            i_sum = sum(i)
            while n % i == 0:
                ans += i_sum
                n //= i
        i += 1
    return ans

def sum(n):
    ans = 0
    while n > 0:
        ans += n%10
        n //= 10
    return ans

for i in range(1000000):
    #print(i)
    if sum(i) == p(i): print(i)

