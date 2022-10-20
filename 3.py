def inverse(n):
    pot = 10
    while n%(pot*10) != n:
        pot *= 10

    n_rev = 0
    while n > 0:
        n_rev += n%10*pot
        pot /= 10
        n //= 10

    return int(n_rev)

def foo(n):
    n_rev = inverse(n)

    while n > 0:
        if n % 10 != n_rev % 10:
            return False
        n //= 10
        n_rev //= 10

    return True

print(foo(int(input())))

#todo binary
