#With the continue statement we can stop the current iteration, and continue with the next:
# its used to skip one element

i = 0
while i < 10:
  i += 1
  if i == 3 :
    continue
  print(i)