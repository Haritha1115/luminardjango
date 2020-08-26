from re import *

rule = '[kK][Ll]\d{2}\w{2}\d{4}'
vno = input("enter the vehicle number :")
matcher = fullmatch(rule, vno)
if matcher != None:
    print("VALID KERALA VEHICLE REGISTRATION ")
else:
    print("INVALID KERALA VEHICLE REGISTRATION")
