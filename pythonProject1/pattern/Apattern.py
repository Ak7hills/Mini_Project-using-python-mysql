for i in range(5):
    for j in range(5):
        if i==0 or (j==0 or j==4) and i>0 or i==2 and( j>0 or j<4):
          print('a', end=' ')
        else :
            print(' ',end=' ')

    print("")