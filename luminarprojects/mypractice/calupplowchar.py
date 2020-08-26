word = "AbCdEfGhIjKl"
num = nom = 0
for i in range(0,len(word)):
    if word[i].isupper():
        num += 1
    else:
        nom += 1
print("number of upper case: ", num)
print("number of lower case: ", nom)