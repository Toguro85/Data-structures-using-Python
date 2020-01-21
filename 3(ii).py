import array as arr
print("enter 2d array size")
size=int(input())
list2=[]
print("enter array")
for i in range(0,size):
    list1=[]
    for j in range(0,size):
        list1.append(int(input()))
    list2.append(list1)
print(list2)
print("array after 90 degrees")
for i in range(0,len(list2)):
    for j in range(0,len(list2)):
        print(list2[j][i],end=" ")
    print("\n")
