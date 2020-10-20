# num = int(input("number of input:"))
# lst = []
# mul = 1
# for i in range(0,num):
#     n = int(input("enter the number:"))
#     lst.append(n)
# print("entered numbers are:", lst)
# for i in lst:
#     mul*=i
# print("sum of all :",mul)


# ..........................................prg 2 = smallest in list....................................................
# num = int(input("number of input:"))
# lst = []
# for i in range(0, num):
#     n = int(input("enter the number:"))
#     lst.append(n)
# for i in range(0,num):
#     for j in range(i+1,num):
#         if lst[i]<lst[j]:
#             small = lst[i]
#         else:
#             small= lst[j]
# print("smallest number is:",small)


# .........prg 3 = to count the number of stringlenght>2 , and display if first annd last char o string is same.........
# lst = ['abca', 'x', 'ac', 'aab', 'ab', 'bbaabbb', 'dd', 'g']
# print("string lwith lenght greater than 2 :")
# for words in lst:
#     if len(words) >= 2:
#         print(words)
# print("\n string with 1st and last char same :")
# for words in lst:
#     x = 0
#     y = len(words) - 1
#     if words[x] == words[y]:
#         print(words)

# ......prg 4 = if lst=[a,b,c] then o/p = [a**1,b**2,c**3].........................................................
# lst = []
# new = []
# num = int(input("enter the number of element you want to enter:"))
# for i in range(0, num):
#     x = int(input("enter the number:"))
#     lst.append(x)
# print("list you entered :", lst)
# j = 1
# for items in lst:
#     nom = items ** j
#     new.append(nom)
#     j += 1
# print("list you desired :", new)
