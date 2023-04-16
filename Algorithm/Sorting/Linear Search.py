#Linear search

def linearSearch(arr, x):
    for i in range(len(arr)):
        if (arr[i] == x):
            return i
    return -1

A=[5,3,2,9,7,8]
index=linearSearch(A,7)
print(index)