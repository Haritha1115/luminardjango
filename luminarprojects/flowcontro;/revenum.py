num = int(input("enter the number :"))
i = 0
while num > 0:
    digit = num % 10
    print(digit,end="")
    num = num // 10
