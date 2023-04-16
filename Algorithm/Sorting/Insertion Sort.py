x = [10,9,8,7,6,5,4,3,2,1,0]

for i in range(1,len(x)):
    key = x[i]
    j = i-1
    while((key < x[j]) and (j >= 0)):
        x[j+1] = x[j]
        j = j-1
    x[j+1] = key

print(x)
