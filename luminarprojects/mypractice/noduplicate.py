lst = [1, 2, 3, 4, 5, 3, 2, 5, 6, 7, 89]
new = []
old = []
ln = len(lst)
for i in range(0, ln):
    if lst[i] not in new:
        new.append(lst[i])
    else:
        old.append(lst[i])
print("new list with delete dupli :", new)
print("duplicate elements :", old)

