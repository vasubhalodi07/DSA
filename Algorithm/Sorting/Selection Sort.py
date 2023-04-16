def selectionSort(a):
    min_index = 0
    for i in range(len(a)):
        min_index = i
        for j in range(i+1,len(a)):
            if(a[min_index] > a[j]):
                min_index = j
        a[min_index],a[i] = a[i],a[min_index]

arr = [5,4,3,2,1]
selectionSort(arr)
print(arr)
