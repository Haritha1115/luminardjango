mrk1=int(input("enter the mark1 :"))
mrk2=int(input("enter the mark2 :"))
mrk3=int(input("enter mark 3 :"))
total = mrk1+mrk2+mrk3
print("total marked obtained is :",total)
if total>145:
    print(" grade A+")
elif 140<total<=145:
    print(" grade A")
elif 135<total<=140:
    print(" grade B+")
elif 130<total<=135:
    print(" grade B")
elif total<=130:
    print(" you failed ")