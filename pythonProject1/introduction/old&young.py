a=int(input("enter the age of first person :"))
b=int(input("enter the age of second person :"))
c=int(input("enter the age of third person :"))
if a>b and a>c :
    print("a is the oldest among all")
    if b>c:
        print("c is the youngest among all")
    else:
        print("b is the youngest among all")
elif b>a and b>c:
    print("b is the oldest among all")
    if a>c:
        print("c is the youngest among all")
    else:
        print("a is the youngest among all")
else:
    print("c is the oldest among all")
    if a>b:
        print("b is the youngest among all")
    else:
        print("a is the youngest among all")