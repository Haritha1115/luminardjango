word = input("enter a word :")
# print(word.upper())
new = ""
wrd = len(word)-1
for i in range(wrd, -1, -1):
    print(word[i])
    new += word[i]
print("reverse of above letter is : ", new)
if word == new:
    print("entered is a palindrome")
else:
    print("entered is not a palindrome")
