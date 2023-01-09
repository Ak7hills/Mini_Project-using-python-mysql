levels=int(input("enter the number: "))
for i in range(levels +1,0,-1):
    for j in range(i-1,0,-1):
        print(j, end=' ')
    print()