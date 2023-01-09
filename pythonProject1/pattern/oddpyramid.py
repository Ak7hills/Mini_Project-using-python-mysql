n= int(input("enter the levels:"))
for i in range(n+1):
    if i%2!=0:
      for j in range(n-i):
          print(' ',end=' ')
      for j in range(i):
          print('*  ',end=' ')
      print()