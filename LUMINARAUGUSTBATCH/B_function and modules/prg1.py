# def add(num1,num2):
#     return num1 +num2
#
# add(10,20,30) # show error becoz of argument lenght

# .... using *args.................
# def add(*number):
#     print(sum(number))
#
#
# add(10, 20, 30, 40, 50)

# when we pass argument as (ajay,kakannad,trivandrum,35000) we cant connect them so we use kwargs**
def add(**args):
    tot = 0
    for values in args:
        tot += args[values]
    print(tot)

add(num1=23,num2=34,num3=45)