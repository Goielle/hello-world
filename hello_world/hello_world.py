def print_message(n, message):
  if n < 0:
    raise ValueError("Argument must be >=1")
  else:
    for i in range(0,n):
      print(message)
   
print_message(5,"Hello world")
