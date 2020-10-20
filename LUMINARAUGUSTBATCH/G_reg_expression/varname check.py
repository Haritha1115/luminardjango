# variable name rules it should be alphabet a-z
# any number of character


# EXAMPLE

# first char should me a-k
# second char should me number / by 3
# following by any words
import re

rule = "[a-k][369][\w]*"  # without * we can only enter 3 char like a61 :: with star a61jjdfj will be valid
# rule = "[a-k][369][a-z0-9]*"  # [a-z0-9]* means any number of a-z and any number of 0-9
pattern = input(" enter pattern : ")
match = re.fullmatch(rule, pattern)
if match == None:
    print("invalid ")
else:
    print("valid")
