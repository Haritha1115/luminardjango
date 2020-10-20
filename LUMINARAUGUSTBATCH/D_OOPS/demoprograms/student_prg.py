# to create each line of line as object and to print studnet with >450
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
    total = lines[3]
    obj = student(id, name, course, total)
    lst.append(obj)
for obj in lst:
    # if int(obj.total) > 450:
    #     print(obj)
    # to find student with max mark   NOTE : max value only work in list : so append the marks to the list
    new.append(obj.total)
n = max(new)
print(n)
for obj in lst:
    if obj.total == n:
        print(obj)
