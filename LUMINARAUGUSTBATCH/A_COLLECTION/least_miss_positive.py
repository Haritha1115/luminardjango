lst = [-1, 3,0,1,2]
lst.sort()
print(lst)
n = len(lst) - 1
for i in range(1, lst[n]):
    if i not in lst:
        print(i)
        break
else:
    # print("no least number in given ")
    print(lst[n] + 1)