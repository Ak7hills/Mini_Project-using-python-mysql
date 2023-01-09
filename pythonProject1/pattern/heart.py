n= int(input("enter the levels:"))
for i in range(n+1):
    if i%2!=0:
      for j in range(n-i):
          print(' ',end=' ')
      for j in range(i):
          print('*  ',end=' ')
      for j in range(2*(n-i-1)):
          print(' ',end=' ')
      for j in range(i):
          print('*  ',end=' ')
      print()
for count in range(n+1):
    num=2*count-1
for i in range(num+1,0,-1):
    if i%2!=0:
        for j in range(num-i):
            print(' ',end=' ')
        for j in range(i):
            print('*  ',end=' ')
        print()


