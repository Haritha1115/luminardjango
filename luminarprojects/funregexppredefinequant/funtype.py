def add(**args):
    sm = 0
    print(args)  # shows how it is stored in dictionary
    for k, v in args.items():
        sm += v  # addition of values
    print(sm)


add(num1=10, num2=20, num3=30, num4=40)
# here we can pass unlimited arguments in **args and it is stored as dictionary
