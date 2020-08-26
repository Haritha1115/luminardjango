num = int(input("enter the number :"))
i = 0
mul = 0
while num > 0:
    digit = num % 10
    mul += digit ** 3
    num = num//10
print("sum of cube of each digit :", mul)
