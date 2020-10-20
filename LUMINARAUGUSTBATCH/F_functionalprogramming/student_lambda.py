# to print all studemt name in upper
class student:
    def __init__(self, rol, name, course, total):
        self.rol = rol
        self.name = name
        self.course = course
        self.total = total

    def printvalue(self):
        print("id :", self.name)
        print(" name :", self.name)
        print(" course : ", self.course)
        print("total :", self.total)

    def __str__(self):
        return self.name


f = open("student", "r")
lst = []
new = []
for lines in f:
    lines = lines.rstrip("\n").split(",")
    id = lines[0]
    name = lines[1]
    course = lines[2]
    total = int(lines[3])
    obj = student(id, name, course, total)
    lst.append(obj)
# print(lst)
nam = list(map(lambda obj: obj.name.upper(), lst))
print(nam)
out = list(filter(lambda obj: obj.total > 450, lst))
for d in out:  # uise for loop to avoidthe hexadecimal values
    print(d)
