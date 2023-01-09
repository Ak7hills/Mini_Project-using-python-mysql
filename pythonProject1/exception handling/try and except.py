
try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    c=a/b

except:
    print('some exception occured')
else:
    print(c)
finally:
    print("task completed")