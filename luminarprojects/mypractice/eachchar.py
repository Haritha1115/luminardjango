let = "ABCABCEDGH"
lst = set()
for ch in let:
    if ch not in lst:
        lst.add(ch)
print(lst)