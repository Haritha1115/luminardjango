letter = input("enter our string :")
res = ""
ln = len(letter) -1
while ln >= 0:
    res += letter[ln]
    ln -= 1
print(res)
if letter == res:
    print("entered string is palindrome")
else:
    print("entered is not palindrome")


# program to check a number as palindrome

#num = int(input("enter your number :"))
#temp=num
#res = 0
#tum = 0
#while num > 0:
 #   tum = num % 10
 #   res = res * 10 + tum
 #   num = num // 10
#print("reverse number is :", res)
#if temp==res:
#    print("number is palindrome")
#else:
#    print(" number is not palindrome")
