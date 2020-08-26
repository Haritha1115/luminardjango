# from re import *
#
# #rule = '\w*\d*[@]\w*[.]com'
# rule = '\w*\d*[@]gmail[.]com'
# f = open("mailist","r")
# g = open("validlist from mailist","w")  # opening the new list in write mode
# for data in f:
#     data = data.rstrip("\n")
#     matcher = fullmatch(rule,data)
#     if matcher != None:
#         g.write(data)  # writing new data to new file


#....... using list..........

from re import *

# rule = '\w*\d*[@]\w*[.]com'
rule = '\w*\d*[@]gmail[.]com'
f = open("mailist", "r")
new = []
for data in f:
    data = data.rstrip("\n")
    matcher = fullmatch(rule, data)
    if matcher != None:
        new.append(data)
print("VALID MAIL-ID FROM GIVEN LIST : ", new)

