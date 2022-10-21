def foo():
    a1 = int(input())
    if a1 != 0:
        return
    print(2)
    a2 = int(input())
    if a2 != 1:
        return
    b = 0
    while True:
        b += 2*a2
        print(b)
        t = a1
        a1 = a2
        a2 = a1-b*t
        i = int(input())
        if a2 != i:
            return

foo()
    
