# to list emp who desig is trainer          PENDING
# to covert all name to upper
# find total salary of all employee
# to find highest salary of employee
from functools import *


class employee:
    cname = "luminar"

    def __init__(self, empid, name, desig, sal):
        self.id = empid
        self.name = name
        self.desig = desig
        self.sal = sal

    def printVal(self):
        print(" id :", self.id)
        print(" name :", self.name)
        print(" desig :", self.desig)
        print(" salary :", self.sal)

    def __str__(self):
        return self.name


f = open("emp_detail", "r")
# maxtot = []
lst = []
for data in f:
    data = data.rstrip("\n").split(",")
    id = data[0]
    name = data[1]
    desig = data[2]
    sal = int(data[3])
    obj = employee(id, name, desig, sal)
    lst.append(obj)

# to print name in caps
name = list(map(lambda obj: obj.name.upper(), lst))
print(name)

# to print max sal
# maxtot.append(obj.sal)
# maxsal = reduce(lambda num1, num2: num1 if num1 > num2 else num2, maxtot)
maxsal = reduce(lambda num1, num2: num1 if num1 > num2 else num2, list(map(lambda obj: obj.sal, lst)))
print(maxsal)

# to print total sal
# totsal = reduce(lambda num1, num2: num1 + num2, maxtot)
totsal = reduce(lambda num1, num2: num1 + num2, list(map(lambda obj: obj.sal, lst)))
print(totsal)

# to print trainers name
# ans = list(filter(lambda obj: obj.desig == "trainer", list(map(lambda obj: obj.desig, lst))))
ans = list(filter(lambda obj: obj.desig == "trainer", lst))
for d in ans:
    print(d, "trainer")
