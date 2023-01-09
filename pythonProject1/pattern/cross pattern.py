n=int(input("enter the levels you want:"))
count=1
for i in range(n,1,-1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(i):
        if k==0 or k==i-1:
            print(count,end='   ')
        else:
            print(" ",end='   ')
    count+=1
    print()
count1=5
for i in range(n+1):
    if i>0:
        for j in range(1,n-i+1):
            print(' ',end=' ')
        for k in range(0,i+1):
            if k==0 or k==i-1:
                print(count1,end='   ')
            else:
                print(" ",end='   ')
        count1-=1
        print()