# counting sorting
# char converts string to ascii value

def countingsort(A):
  count = [0 for i in range(256)]
  for i in range(len(A)):
    count[ord(A[i])]+=1
  output = ""
  for i in range(256):
    output = output + (count[i]*chr(i))
  return output

A = "ASDGJDFS12345678asdfgh"
out = countingsort(A)
print(out)
