import re

pattern = input("enter the vechile number : ")
rule = "[klKL][\d]{2}[a-z]{2}[\d]{4}"
match = re.findall(rule, pattern)
if match == None:
    print(" invalid")
else:
    print("valid")
