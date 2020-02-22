def insertionSort(arr):
    for i in range(1,len(arr)):
        currentvalue=arr[i]
        position=i
        while(position>0 and arr[position-1]>currentvalue):
            arr[position]=arr[position-1]
            position=position-1
        arr[position]=currentvalue
        

arr=[12,2,1,31,12]
print("original array")
for i in range(0,len(arr)):
    print(arr[i],end=" ")


print("\n")
insertionSort(arr)
print("sorted array")
for i in range(0,len(arr)):
    print(arr[i],end=" ")

