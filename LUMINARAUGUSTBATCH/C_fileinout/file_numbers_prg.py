# to read the number text and to store in a list
f = open("numbers", "r")
lst = []
for lines in f:
    # lst.append(lines.rstrip("\n")) here output will be string and to do math operation convert to int
    lst.append(int(lines.rstrip("\n")))
print(lst)
print("sum = ", sum(lst))
print("max= ", max(lst))
print("min= ", min(lst))

# always remember that FILE(.TXT)  only  have string values . values are either read or written as string
