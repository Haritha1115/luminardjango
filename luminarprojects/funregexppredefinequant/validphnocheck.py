from re import *
rule = '\d{10}'
phno = input("enter phone number : ")
matcher = fullmatch(rule,phno)
if matcher != None:
    print("VALID PHONE NUMBER")
else:
    print("INVALID PHONE NUMBER ")