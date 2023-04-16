def karatsuba(x,y):
    if(x<10 or y<10):
        return x*y
    m = max(len(str(x)),len(str(y)))

    if m%2!=0:
        m-=1
    a,b = divmod(x,10**(int(m/2)))
    c,d = divmod(y,10**(int(m/2)))

    ac = karatsuba(a,c)
    bd = karatsuba(b,d)

    ab_cd = karatsuba((a+b),(c+d)) - ac - bd

    return (ac*(10**m)) + ((ab_cd)*(10**int(m/2)))+bd

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))

mul = karatsuba(x, y)
print(mul)

