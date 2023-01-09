num=int(input("enter the limit upto you need:"))
for b in range (2, num+1):
    for i in range(1,11):
        sum=i*b
        print(b,'*',i,' =',sum)