from re import *

rule = '\w*\d*[@]\w*[.]com'  # to check all other unspecified mail id note: .com is same for all
#rule = '\w*\d*[@]gmail[.]com'  # to check for only gmail
mid = input("enter the mail id : ")
matcher = fullmatch(rule,mid)
if matcher != None:
    print("VALID MAIL ID")
else:
    print("INVALID MAIL ID")