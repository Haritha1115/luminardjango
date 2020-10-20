# three different ways   to get yr with max no.of movies
f = open("movies.csv", "r")
dict = {}
# for data in f:                                             # 1. easy one with just one line 13
#     data = data.rstrip("\n").split(",")
#     name = data[1]
#     yr =  data[2]
#     rate = data[3]
#     dura = data[4]
#     if yr not in dict:
#         dict[yr] = 1
#     else:
#         dict[yr] += 1
# maxval = max(dict,key=dict.get)
# print(dict)
# print(" yr with max movie :",maxval)

# using list
# lst = []
# for data in f:
#     data = data.rstrip("\n").split(",") # 2. appending just values to lst finding max anf the displayig corresponding key
#     name = data[1]
#     yr = data[2]
#     rate = data[3]
#     dura = data[4]
#     if yr not in dict:
#         dict[yr] = 1
#     else:
#         dict[yr] += 1
#     for key in dict.items():
#         lst.append(dict[key])
#     num = max(lst)
#     for k, v in dict.items():
#         if v == num:
#             print("yr with max no of movies:", k)

#lst = [(10,1),(7,2),(8,3),(4,5)]
#sortlst = sorted(lst) # o/p = (4,5),(7,2),(8,3),(10,1)  it sort acc to first digit in aascending
# to reverse
#sortlst = sorted(lst,reverse=True) #o/p = (10,1),(8,3),(7,2),(4,5)
 # using  sort to find max no.if movies
lst = []
for data in f:
    data = data.rstrip("\n").split(",")        # sorted in reverse order and printed the first one
    name = data[1]
    yr =  data[2]
    rate = data[3]
    dura = data[4]
    if yr not in dict:
        dict[yr] = 1
    else:
        dict[yr] += 1
    for k,v in dict.items():
        #lst.append((k,v))     # o/p= (yr,no.of movies) but here we need max no.of movie so we append as v,k
        lst.append((v,k))
sortlst = sorted(lst,reverse=True)
#to get only the ye with max value
print(sortlst[0])


