# to count/quantity
import re

pattern = 'a{2,3}'
# pattern = 'a?'
# pattern = 'a+'  # look for a,aa,aaa,aaaa,aaaaa,aaaaaaa, like that
count = 0
matches = re.finditer(pattern, "abaabaaaabaababababbbaaaaa")
for match in matches:
    print(match.start())  # shows starting postion of match found
    print(match.group())  # display what matches it found within thw pattern
    count += 1
print(" total number of count : ", count)

# ........ some other pattern.................

# 1. pattern = 'a*'  # it will display each place of a,aa,aaa,aaaa,
# aaaaa etc it will print all place but in group() only display the matching element in string with pattern

# 2. pattern = 'a?'  #it will check for single a and display all the position of a and non a ; and in group() display
# matchinmg elements

# 3. pattern = 'a{2}' # aa vala  place check karega
# 4. pattern = 'a{2,3}'  3 check and diplay min 2 a(aa) and max 3 a(aaa)
