f = open("empl_detail","r")
name = []
salary = []
for data in f:  # first step = 1001,ajay,23000 \ n   second step = 1002, harsha,43000\n
    data = data.rstrip("\n").split(",")  # 1001,ajay,23000= data[0],data[1],data[2]
    name.append(data[1]) # name = ajay
    salary.append(data[2])  # salary = 23000
print("emp_name : ",name)
print("salary :",salary)