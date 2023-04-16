def binarySearch(arr,num):
    left = 0
    right = len(arr)-1

    while(left <= right):
        mid = (left+right)//2
        if(arr[mid] == num):
            return mid
        elif(arr[mid] > num):
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [0,1,2,3,4,5,6,7,8,9,10,20,30,40,50]
num = int(input("Enter the number to searched : "))
index = binarySearch(arr, num)
if(index == -1):
    print("Number not found... ")
else:
    print("Number found at: ",index)