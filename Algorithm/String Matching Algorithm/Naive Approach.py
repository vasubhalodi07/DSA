string = "python"
pattern = "th"

print("A: ",string)
print("B: ",pattern)

x = len(string)
y = len(pattern)
flag = 0

for i in range(x-y+1):
    t = 0
    flag = 0
    
    for j in range(i,i+y):
        if(string[j] == pattern[t]):
            flag = flag+1
            t = t + 1
    if(flag == len(pattern)):
        print("Pattern Found...")
        break
if(flag == 0):
    print("Pattern Not Found...")