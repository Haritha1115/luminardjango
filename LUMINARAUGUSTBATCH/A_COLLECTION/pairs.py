# ar = [1,2,3,4,5]  # to find the total in pairs
# tot = int(input("enter the number:"))
# qn= len(ar) -1
# for i in range(0, qn):
#     for j in range(qn,0,-1):
#         if tot == (i+j):
#             if i != j:
#                 print(i,",",j)


#......................  without using 2 for loop......................................
lst = [1,2,3,4,5,6,7]
element = int(input("enter the element:"))
low = 0
upp = len(lst) - 1
while(low <= upp):
    tot = lst[low] + lst[upp]
    if tot == element:
        print(lst[low],"&",lst[upp])
        break
    elif tot>element:
        upp -= 1
    elif tot<element:
        low += 1