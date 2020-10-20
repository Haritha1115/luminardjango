# to list emp who desig is trainer             # using list comprehension
# to covert all name to upper
# find total salary of all employee
# to find highest salary of employee
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
maxtot = []
lst = []
for data in f:
    data = data.rstrip("\n").split(",")
    id = data[0]
    name = data[1]
    desig = data[2]
    sal = int(data[3])
    obj = employee(id, name, desig, sal)
    lst.append(obj)
# display name of trainer
res = [obj.name for obj in lst if obj.desig == "trainer"]
print(res)
res1 = [ obj.name.upper() for obj in lst]
print(res1)
res2 = sum([obj.sal for obj in lst])
print(res2)
res3 = max([obj.sal for obj in lst])
print(res3)