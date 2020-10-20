import re

# predefined character sets
xam = "[abc]"  # check fpr a or b or c
matcher = re.finditer(xam, "ab23 @cdfg")
for match in matcher:  # 0a1b6c
    print(match.start())
    print(match.group())

# xam = "[0-9]"  # check all digit separately
# xam = "[a-z]"  #a to z all char will be matched separately
# xam = "[^a-z0-9A-Z]"   # check for special character

# predefined character
# x = "\s"    # check for space
# x = "\d"    # look for digits
# x = "\D"    # except digit
# x = "\w"    # all words and digit except  special char
# x = "\W"    # except words only special char
