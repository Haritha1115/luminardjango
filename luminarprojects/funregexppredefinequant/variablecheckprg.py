# first rule: 1st char is alpha and must be within a-k
# 2nd rule : second character must be digit and divisible by 3
# third rule : and then any number of character
from re import *

rule = '[a-k][3,6,9][a-zA-Z0-9]*'
letter = input("enter the letter : ")
matcher = fullmatch(rule, letter)
if matcher != None:
    print("VALID NAME")
else:
    print("INVALID NAME")
