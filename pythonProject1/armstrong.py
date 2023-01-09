n=(input("enter the number:"))
l=len(n)
num=int(n)
armstrong=0
while num!=0:
    digit=num%10
    armstrong=armstrong+digit**l
    num=num//10
if armstrong==int(n):
    print("armstrong")
else:
    print("not armstrong")
