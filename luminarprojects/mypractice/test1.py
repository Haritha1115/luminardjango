ch = "ABABACAA"
ln = len(ch)
lst = []
di = {}
for let in ch:
        lst.append(let)
print(lst)
for word in lst:
    if word not in di:
        di[word] = 1
    else:
        print("most frequent :", word)
        break