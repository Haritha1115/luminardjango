student ={"rno" : 1,"name":"varun","total":350, "caste" : "human"}
print(student)

# to print name
print(student["name"])

# to check if clg key is there or not
print("clg" in student)

# to  add a key
student["clg"]="VISAT"
print(student)

# to update total as 400
student["total"] += 50

# or student["total"] = 400
print(student)

#to iter the dict
for key in student:
    print(key,",",student[key])
for k,v in student.items():
    print(k,v)

# to delete a key in dict
del(student["caste"])
print(student)