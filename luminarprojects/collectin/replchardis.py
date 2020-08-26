pat = "ABABDSDHBABDF"
dct = {}
lst = []
for letters in pat:
    lst.append(letters)
print(lst)
for word in lst:
    if word not in dct:
        dct[word] = 1
    else:
        #dct[word] += 1
        print("first recursive word", word)
        break
#for k,v in dct.items():  #to print in different lines
#    print(k)