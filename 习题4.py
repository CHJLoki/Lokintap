def square_root_1():
    c = 64
    g = c/2
    i = 0
    while abs(g**3 - c) > 0.00000000001:
        g = (2*g)/3 + c/(3*(g**2))
        i = i + 1
        print("%d: % .13f" % (i,g))
square_root_1()
