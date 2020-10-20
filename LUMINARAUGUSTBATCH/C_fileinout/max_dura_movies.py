# max rated movie
f = open("movies.csv", "r")
dict = {}
lst = []
for data in f:
    data = data.rstrip("\n").split(",")
    name = data[1]
    dura = data[4]
    dict[name] = dura
print(dict)
for k, v in dict.items():
    lst.append((v,k))
sortlst = sorted(lst,reverse=True)
#to get only the ye with max value
print(sortlst[0])


# maxlst = max(dict,key =dict.get)
# print("\n",maxlst)
