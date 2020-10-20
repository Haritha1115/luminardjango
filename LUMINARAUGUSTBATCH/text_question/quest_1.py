# create a function which accept lower and a upper limit and have to print all prime number between them]
def prime(low, upp):
    n = low + 1
    while n < upp:
        i, flag = 1, 0
        while i <= n:
            if n % i == 0:
                flag += 1
            i += 1
        if flag <= 2:
            print("prime numbers are :", n)
        n = n+1


l = int(input(" enter lower limit :"))
u = int(input(" enter upper limit :"))
prime(l, u)
