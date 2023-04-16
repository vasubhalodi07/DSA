#Rabin-Karp Approach

string="python"
pattern="th"

X=len(string)
Y=len(pattern)
r=127 

#hashcode for pattern
sumP=0
for i in range(Y):
    sumP=sumP+ord(pattern[i])*(r**(Y-1-i))
    
#hashcode for string
sumS=0
for i in range(Y):
    sumS=sumS+ord(string[i])*(r**(Y-1-i))  #Hashcode for number of characters in pattern
    flag=0                                 
    if(sumP==sumS):
        for j in range(Y):
            if(pattern[j]!=string[j]):
                flag=1
                break
        if(flag==0):
            print("Pattern is found")
        

#Rolling hash function
for i in range(Y,X):
    sumS=(sumS-(ord(string[i-Y])*(r**(Y-1))))*r+ord(string[i])
    flag=0

    if(sumS==sumP):
        for j in range(Y):
            if(pattern[j]!=string[i+1-Y+j]):
                flag=1
                break
        if(flag==0):
            print("Pattern is found")
