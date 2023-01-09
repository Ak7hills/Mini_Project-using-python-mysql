str1 = "Cristiano Ronaldo"
freq = {}
for i in str1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Count of all characters in string is :\n "
      + str(freq))