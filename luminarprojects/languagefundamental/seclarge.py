num1 = int(input("enter the first num:"))
num2 = int(input("enter the second num :"))
num3 = int(input("enter the third num :"))
if num1 > num2 > num3:
    print("second largest is ", num2)
elif num2 > num1 > num3:
    print("second largest is", num1)
elif num3 > num1 > num2:
    print("second largest is ,", num1)
elif num1 > num3 > num2:
    print("second largest is ", num3)
elif num2 > num3 > num1:
    print("second largest is ", num3)
elif num3 > num2 > num1:
    print("second largest is ", num2)
