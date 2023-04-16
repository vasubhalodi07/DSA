def ExponenDC(x, n):
    ans = 1
    for i in range(n):  
        ans = ans * x
    return ans

print(ExponenDC(2, 3))
