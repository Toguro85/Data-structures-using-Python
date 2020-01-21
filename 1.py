import array as arr
a=int(input())
list1=[]
arr2=[]
print("list1 is:")
for i in range(0,a):
    a3=int(input())
    list1.append(a3)
arr2=arr.array("i",list1)



print("arr1 is:")
print(arr2)

    
list2=[]
print("list2 is:")
for i in range(0,a):
    b=int(input())
    list2.append(b)
arr4=arr.array("i",list2)
print(arr4)

arr5=arr2+arr4
print(arr5)

print("resultant array is:")
for i in range(0,len(arr5)):
    for j in range(i+1,len(arr5)):
        if (arr5[i]>arr5[j]):
            temp=arr5[i]
            arr5[i]=arr5[j]
            arr5[j]=temp
    print(arr5[i])
