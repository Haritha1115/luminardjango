import re
# rule = "[9][\d]{9}"  #  check for mno with 9
rule = '(91)?\d{10}'  # ? means 91 is optional there  means 6238201504 is valid
mno = input("enter mobile number: ")
matcher = re.fullmatch(rule,mno)
if matcher == None:
    print("invalid")
else:
    print("valid")