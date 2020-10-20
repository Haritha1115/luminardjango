# to list emp who desig is trainer          PENDING
# to covert all name to upper
# find total salary of all employee
# to find highest salary of employee
from functools import *

f = open("emp_detail", "r")
dict = {}
sala = []
names = []
for data in f:
    data = data.rstrip("\n").split(",")
    id = data[0]
    name = data[1]
    desig = data[2]
    salary = data[3]
    dict[id] = {"name": name, "desig": desig, "sal": salary}
    # names.append(name)
    # sal.append(salary)
print(dict)
for k in dict:
    names.append(dict[k]["name"])
    sala.append(dict[k]["sal"])

caps = list(map(lambda name: name.upper(), names))  # all in upp
print(caps)
tot = reduce(lambda sa1, sa2: int(sa1) + int(sa2), sala)
print(tot)
maxsal = reduce(lambda sa1, sa2: max(sa1, sa2), sala)
print(maxsal)

# for k in dict:
#     if dict[k]["desig"] == "trainer":
#         ans1.append(dict[k]["name"])
# print(ans1)

ans = list(filter(lambda dict: dict[k]["name"] if dict[k]["desig"] == "trainer" else print("not found"), dict))
print(ans)



 # ans1 = list(filter(lambda dict[name]["desig"]:dict[name]["name"] if dict[name]["desig"] == "trainer", dict))
# print(ans1)




