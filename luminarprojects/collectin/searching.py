num = int(input("enter the number you want to search :"))
lst = []
for i in range(1, 101):
    lst.append(i)
tot = len(lst)
for i in range(0,tot):
    if num == lst[i]:
        flag = 1
        break
    else:
        flag = 0
if flag == 1:
    print("found it")
else:
    print("didnt find")
