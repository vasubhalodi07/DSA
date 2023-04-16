def ExponenDC(x, n):
    if(n == 0):
        return 1
    else:
        m = ExponenDC(x, int(n/2))
        if n%2 == 0:
            return m*m
        else:
            return m*m*x

print(ExponenDC(2,2))
