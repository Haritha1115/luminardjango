import re

f = open("prg1_text", "r")
lst = []
for line in f:
    line = re.split('[\W]', line) # \W means special chr
    for words in line:
        if words.isalpha():
            lst.append(words)
print(lst)
dict = {}
for words in lst:
    words = words.lower()  # to calculayte the At and at as one without this conversion to lower At = 1; at= 1
    if words not in dict:
        dict[words] = 1
    else:
        dict[words] += 1
print("\n ....................word count.........................")
print(dict)
print("\n .......................max word occoured in para...............")
top = max(dict, key=dict.get) # it will gwt the max value and print corresponding key
# The key parameter takes a function, and for each entry in the iterable,
# it'll find the one for which the key function returns the highest value.
print(top)



