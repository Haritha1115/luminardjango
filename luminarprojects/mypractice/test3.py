num = int(input(" enter the dividend : "))
div = int(input("enter the divisor :"))
res = 0
for i in range(0, 50):
    for j in range(0, div):
        res = div * i + j
        if num == res:
            print("quotient :", i)
            print("reminder :", j)