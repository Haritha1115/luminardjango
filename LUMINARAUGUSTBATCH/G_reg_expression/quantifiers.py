import re

pattern = "aaaabbaaaaaaabbabbababaa"
# x = "a+"  # check for a,aa,aaa,aaaa,aaaaa,aaaaaa + here it wont check position of other alphs
# but not display that alpha

# x = "a*"  # check for a,aa,aaa,aaaa,aaaaa,aaaaaa + here it will check
# position of other  alphs but not display that alpha

x = "a?"  # check for single a and display its podition + also display
# position of other char but not display that alpha

# x = "^a"  # out as 0 a        check
# x = "a$"  # out as 25 a       check

# x = "a{2}"  # check for 2 no. of a and its position
# x = "a{2,3}"  # for minimum 2 max 3a


matcher = re.finditer(x, pattern)
for match in matcher:
    print(match.start())
    print(match.group())
# to get exczat match we use fullmatch
