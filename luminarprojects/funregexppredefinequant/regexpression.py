# for pattern matching
# step 1 : import re module
import re

pattern = re.finditer("ab", "abababhanbababa")
count = 0
for match in pattern:
    print(match.start())
    # it will show the place where ab is found NOTE: it will show the value of a becx ab is called as one object
    print(match.group())
    # it will show the group that is matched ab is matched with ab /;make it run and see
    count += 1
print(count)
