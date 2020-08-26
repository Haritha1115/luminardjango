f = open("stu", "r")
stu = set()
pas = set()
fail = set()
for names in f:
    names = names.rstrip("\n").strip(",")
    stu.add(names)
print("total students :", stu)
g = open("pas","r")
for name in g:
    name = name.rstrip("\n").strip(",")
    pas.add(name)
print("passes student list :",pas)
fail = stu - pas
print("list of fail students :",fail)
