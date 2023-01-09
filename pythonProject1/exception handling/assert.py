try:
  x = 1
  y = 0
  assert y != 0 , "Division by zero not possible!"
  print(x / y)
except for AssertionError as msg:
  print(msg)  # error message given by user gets printed

print("The rest of the program still runs!")