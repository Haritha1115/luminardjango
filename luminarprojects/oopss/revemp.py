f = open("edetails", "r")
lst = list()
tst = list()
for info in f:
    lst.append(info.rstrip("\n").split(","))
print(lst)
for lines in lst:
    eid = lines[0]
    name = lines[1]
    desg = lines[2]
    sal = lines[3]
    print(" eid :", eid)
    print("name :", name)
    print("desg :", desg)
    print("sal :",sal)
