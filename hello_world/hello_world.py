def print_message(n, message):
  if n < -3:
    raise ValueError
  else    
    for i in range(0,n):
      print(message)
   
print_message(5,"Hello world")
