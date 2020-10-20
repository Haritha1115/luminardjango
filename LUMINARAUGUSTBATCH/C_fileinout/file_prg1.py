# step1:
# make a refer
# reference=(copy path_or_write name,mode of operation)
# u CAN COPY The path by right clicking on file if thet txt or file is out of the current directory


# #f = open("C:\\Users\\hkkt1\\PycharmProjects\\LUMINARAUGUSTBATCH\\C_fileinout","r")
from typing import List

f= open("prg1_text","r")
# for lines in f:
#     print(lines)

#to store each word in lst
# lst = []
# for lines in f:
#     line  = lines.rstrip("\n").split(" ")
#     lst.append(line)
# print(lst)

# isme  string ke sath pecial char and list ke andhar list tah isliye to remove both and to get only string in list
import re
lst1 = []
for lines in f:
    line  = lines.rstrip("\n").split(" ")
    new = re.split(r"[\W]", lines)  #  it will split all special char
    for words in new:
        print(words)
        if words.isalpha():
            lst1.append(words)
print(lst1)

#  have a look aaaaaat retry prg
