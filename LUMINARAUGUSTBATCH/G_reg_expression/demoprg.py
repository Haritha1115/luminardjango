# pattern matching
# import  re              -> first step
# matcher=re.finditer(pattern,string)   # to print pattern
# cnt = 0
# for match in matcher:
#     print(match.start())   reurn  starting position
#
#     cnt +=1
# print(cnt)

import re

string = "ABAAABAABABBBBABABAAAB"
matcher = re.finditer("AB", string)
cnt = 0
for match in matcher:
    print(match.start())  #print("starting position of ab")
    print(match.group())  # print the pattern matching
    cnt += 1
print("cnt:", cnt)
