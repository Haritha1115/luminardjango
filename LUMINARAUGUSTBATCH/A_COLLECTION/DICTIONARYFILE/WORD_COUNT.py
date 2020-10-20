txt = "hello hai how hai bye wifi hello bye"
dict = {}
words = txt.split(" ")  # o/p as list
print(words)
for word in words:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1
print(dict)