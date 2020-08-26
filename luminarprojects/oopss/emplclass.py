f = open("edetails", "r")
import functools


class employee:
    def __init__(self, eid, name, desig, salary):
        self.eid = eid
        self.ename = name
        self.sal = salary
        self.desg = desig

    def printval(self):
        print("employee id :", self.eid)
        print("employee name :", self.ename)
        print("employee designation :", self.desg)
        print("employee salary :", self.sal)

    def __str__(self):
        return str(self.ename)


emplst = []
for data in f:  # har line ko object me karna ko
    values = data.rstrip("\n").split(",")
    id = values[0]
    names = values[1]
    desig = values[2]
    salary = values[3]
    obj = employee(id, names, desig, salary)
    # obj.printval() #pribnt everything
    # print(obj)  # just print name
    emplst.append(obj)

for emp in emplst:
    s1 = list(map(lambda emp: emp.ename.upper(), emplst))
    s2 = list(filter(lambda emp: int(emp.sal) > 25000, emplst))
    s3 = list(map(lambda emp: int(emp.sal) + 5000, emplst))
    s4 = functools.reduce(lambda sal1, sal2: sal1 if sal1 > sal2 else sal2, list(map(lambda emp: emp.sal, emplst)))
    s5 = functools.reduce(lambda sal1, sal2:sal1 if sal1 == sal2, list(map(lambda emp: emp.sal, emplst)))
print("employee names in upper :", s1)
print("person with salary >2500")
for i in s2:
    print(i)
print("salary incremented ", s3)
print("person  max salaries: ", s4)
print("person with same slaray :", s5)

