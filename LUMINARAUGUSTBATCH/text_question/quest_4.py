# to print HEY as HEEYYY
str = "HEY"
cnt = 1
char = "" # empmty string
for ch in str:
    char += ch*cnt
    cnt +=1
print(char)