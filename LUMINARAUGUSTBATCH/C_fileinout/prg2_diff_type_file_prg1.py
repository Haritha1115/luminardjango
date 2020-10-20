f = open("prg2_nospecial","r")
# lst =[]
# for lines in f:
#     line = lines.rstrip("\n").split(" ")
#     for j in line:
#         lst.append(j)
# print(lst)

# to show call in upper
lst =[]
for lines in f:
    line = lines.rstrip("\n").split(" ")
    # o/p - In a crime that has left Bhopalis horror-struck, a two-day-old girl child was stabbed over 100 times
    for j in line:  # at first in ,then a, then crime ... will be chaged to upper
        lst.append(j.upper())  # just convert it to upper and append
print(lst)
