# n=(input("enter a number:"))
# print("reversed number:",n[::-1])

n=int(input("enter a  number:"))
reversed_num=0
while n!=0:
    digit=n%10
    reversed_num=reversed_num*10+digit
    n=n//10
print("reversed number:",reversed_num)