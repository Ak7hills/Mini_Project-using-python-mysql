n=int(input("enter the levels you want:"))
k1=1
ch=chr(64+k1)
for i in range(n+1):
    if i>0:
        for j in range(n-i):
            print(' ',end=' ')
        for k in range(i):
            print(ch,end='   ')
            k1+=1
            ch=chr(64+k1)
        print()
