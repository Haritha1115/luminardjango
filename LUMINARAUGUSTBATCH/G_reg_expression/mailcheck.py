import re

f = open("mailist", "r")
for data in f:
    data = data.rstrip("\n")
    # rule = "[\w]*[@gmail.com]"
    # rule = "[\w]*[@][a-z]*[.][com]"
    match = re.findall(rule, data)
    if match == None:
        pass
    else:
        print(data)
