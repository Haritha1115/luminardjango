from re import *
f = open("vehicleregistration","r")
rule = '[kK][lL]\d{2}\w{2}\d{4}'
new = []
for data in f:
    data = data.rstrip("\n")
    matcher = fullmatch(rule,data)
    if matcher != None:
       new.append(data)
       # print("VALID REGISTER NUMBER IN KERALA")
   # else:
        #print("INVALID REGISTER NUMBER IN KERALA")
print("VALID NUMBER FROM FILES ARE : ",new )