# Bubble sorting

def Bubble(A):
  for i in range(len(A)):
    swap=False
    for j in range(len(A) - i -1):
      if(A[j] > A[j+1]):
       A[j],A[j+1]=A[j+1],A[j]
       swap = True
    if(swap==False):
      return A
  return A

A = [3,2,5,7,8,9,1]
Bubble(A)
print(A)

