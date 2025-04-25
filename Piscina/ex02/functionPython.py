x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
print()

def myfunc2():
  global y
  y = "Hudson"

myfunc2()

print("Python is " + y)
print()

xy = "Hudson2"

def myfunc():
  global xy
  xy = "Mateque"

myfunc()

print("Python is " + xy)
