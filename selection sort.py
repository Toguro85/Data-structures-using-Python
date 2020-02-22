def selectionSort(arr):
    for i in range(len(arr)):
        min_value=i
        for j in range(i+1,len(arr)):
            if (arr[min_value]>arr[j]):
                min_value=j
                
        arr[i],arr[min_value]=arr[min_value],arr[i]




arr=[12,3,1,32,4,2,3,5,7,4]
print("original array")
for i in range(len(arr)):
    print(arr[i],end=" ")
print("\n")
selectionSort(arr)
print("sorted array")
for i in range(len(arr)):
    print(arr[i],end=" ")
