def print_message(n, message):
  if n < 0:
    raise ValueError
  else:
    for i in range(0,n):
      print(message)
   
print_message(5,"Hello world")
