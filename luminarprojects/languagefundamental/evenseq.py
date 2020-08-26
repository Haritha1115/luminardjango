limit = int(input("enter the limit :"))
i=0
sum=0
while i<=limit:
    if i%2==0:
        print(i,end="\t")
        sum+=i
    i+=1
print("\n","sum of all even number :",sum)
