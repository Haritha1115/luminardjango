lst = [10, 20, 30, 30, 20, 40, 15, 35, 40, 10]
# ln = len(lst) - 1
# for i in range(0, ln+1):
#     for j in range(ln, 0, -1):
#         if lst[i] == lst[j]:
#             lst.remove(lst[j])
#             print(lst[i])
#         else:
#             print(lst[j])
lst1=[]
for number in lst:
    print(number)
    if number in lst1:
        pass
    else:
        lst1.append(number)

print(lst1)