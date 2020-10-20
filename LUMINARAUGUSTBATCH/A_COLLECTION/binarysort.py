ar = [1, 2, 3, 4, 5, 6, 7,8]
element = int(input("enter the element fot searching :"))
ar.sort()
print("sorted array:", ar)
low = 0
upp = len(ar)-1
flag = 0
while low <= upp:
    mid = (low + upp) // 2  # 4//2 = 2 give quiotent & 4%2 will give reminder
    if element > ar[mid]:
        low = mid + 1
    elif element < ar[mid]:
        upp = mid - 1
    elif element == ar[mid]:
        flag = 1
        print("element  found")
        break
else :
    #element != ar[mid]:
        print("not  found")


res = 4%2
print(res)