def prm(num):
    t = 0
    for i in range(1, num + 1):  # here num is input so we have to divide 1 to num to check the factor
        if num % i == 0:  # so here num is prime then it will only go in 2 table (1,itself) so
            t += 1  # here num%i ==0 and if t>2 it is not prime number, t is just given
    if t == 2:  # to check no.of time it is completly divisible by its factors
        print("entered number is prime")
    else:
        print("entered number is not prime number")


num = int(input("enter the number you want to check :"))
prm(num)
# or using flag
# inside for loop
# for i in range of (i,num+1)
#   if(num%i==0)
#       flag=1
#       break
#   else:
#       flag=0
# if(flg==0):
#   print(" number is prime no.")
# else
#   print("number is not primr number")
