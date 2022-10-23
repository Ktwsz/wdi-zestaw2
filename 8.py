def gen():
    sum = [0, 1]
    a, b = 1, 1
    while b < 1000000:
        sum.append(sum[-1]+b)
        a, b = b, a+b
    
    return sum


def foo(n, tab):

    a, b, m = 0, len(tab), 0
    while b-a > 1:
        m = (a+b)//2
        if tab[m] < n:
            a = m
        else:
            b = m

    a = 0
    r_lim = b
    while b-a > 1:
        m = (a+b)//2
        if tab[r_lim]-tab[m] < n:
            b = m
        else:
            a = m


    return tab[r_lim] - tab[a] == n

n = int(input())+1
tab = gen()

while foo(n, tab):
    #print(n)
    n += 1

print(n)
