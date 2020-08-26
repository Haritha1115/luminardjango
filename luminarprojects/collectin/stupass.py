# ....................reading first file...................................`
from typing import Set

f = open("students", "r")
lst = set()
lst1 = set()
fail = set()
for names in f:
    "ritu, akshay, joseph, arun nair, anadhu k, lijo, sam, xender, ben, olivia, walter, peter, astrid"
    print(names)
    name = names.rstrip("\n").split(",")
    for na in name:
        lst.add(na)
j = open("passed","r")
for names in j:
    "ritu, akshay, joseph, arun nair, anadhu k, lijo, sam, xender, ben, olivia, walter, peter, astrid"
    print(names)
    name = names.rstrip("\n").split(",")
    for na in name:
        lst1.add(na)
fail = lst-lst1
print(fail)



#     lst.append(names)
# stu = set(lst)  # declaring the student list to set
# print("name of students :", stu)
# # ....................reading the second file...............................
# q = open("passed", "r")
# for name in q:
#     lst1.append(name)
# pas = set(lst1)  # declaring the passed student to set
# print("name of passed student:", pas)
# # ......................reading failed students name........................
# fail = stu.difference(pas)
# print("student who failed :", fail)
