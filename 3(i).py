#rotate an array

import array as arr
print("enter size")
a=int(input())
list1=[]
print("enter elements")
for i in range(0,a):
    list1.append(int(input()))
arr1=arr.array("i",list1)
print(arr1)
print("enter total times of rotation")
m=int(input())


list1=(list1[-m:]+list1[:-m])
arr2=arr.array("i",list1)


print("array after rotation:")
print(arr2)

for i in arr2:
    print(i,end=" ")
