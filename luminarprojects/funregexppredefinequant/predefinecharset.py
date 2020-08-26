from re import *

pattern = '[abc]'  # check for each lowercase a,b,c in given string and display location of a,b,c it don't search in
# group ..no c in string so no o/p of c
matcher = finditer(pattern, "abz 123*@ABDF")
count = 0
for match in matcher:
    print(match.start())  # give position of pattern
    print(match.group())  # display corresponding matching element in string as given in pattern
    count += 1
print(" total number of count :", count)

# in place of 3rd line we can use different ways like

# 1. pattern = '[a-z]'  look for every lowercase in given string
# 2. pattern = '[A-Z]'   look for every uppercase in given string
# 3. pattern = '[a-zA-Z]   look for both upper and lower case in given string
# 4. pattern = '[A-z]'  also look for both upper and lower case in given string as third one
# 5. pattern = '[a-kA-Z]'  look for lowercase a-k and look for upper case A-Z
# 6. pattern = '[0-9]'  look for digits 0-9 in string
# 7. pattern = '[^0-9]'  look for every char and symbol except digits
# 8. pattern = '[^a-zA-Z0-9]' guess what it will look for special char in string becoz of ^(except) symbol

# ...................now look at PRE-DEFINE CHARACTER .............reduce form of above version

# 1. pattern = '\s'    will check for space in  given string
# 2. pattern = '\d'    will check for only digits in given string
# 3. pattern = '\D'    this is equal to [^0-9]
# 4. pattern = '\w'    this will look for only words (no digit, no special character)
# 5. pattern = '\W'    this is equal to [^a-zA-Z0-9]

# ...NOTE : ANY DOUBT PUT THESE PATTERN IN LINE 3 AND CHECK OUTPUT ...BAKI IS SAME
