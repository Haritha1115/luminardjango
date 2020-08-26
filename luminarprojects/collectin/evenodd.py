# prg to enter list by user
# limit = int(input("enter the limit :"))
# lst = list()
# for i in range(0, limit):
#    element = int(input("enter the no."))
#    lst.append(element)
# print(lst)


even = list()
odd = list()
for i in range(0, 501):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("even list is :", even)
print("odd list is :", odd)
