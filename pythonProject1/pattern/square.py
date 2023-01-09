# word = str(input("enter anything: "))
# length = len(word)
# for i in range(0,length):
#     if i == 0 or i == length -1:
#         print(length * (word[i]+ ' '))
#     else:
#         print(word[i] +((length -2)*"  ")+' '+ word[i])

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        ch=chr(64+i)

        if(i==1 or i==n or j==1 or j==n):
            print(ch,end = " ")
        else:
            print(' ',end=' ')
    print(' ')


