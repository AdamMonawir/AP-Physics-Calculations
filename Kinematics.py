from vpython import *

A =int(input("Pick which problem you have\n1)Displacement in x direction(with basic units),\n2)Displacement in x direction(with ),\n3)...,\n"))

if A == 1:

  B =int(input("Pick which problem you have\n1)Solving for the final position,\n2)Solving for the starting position,\n3)Solving for the change in time,\n4)Solving for the velocity,\n"))

  if B == 1:
    x = float(input("What is the starting position value (in meters), "))
    t = float(input("What is the change in time (in seconds), "))
    v = float(input("What is the starting velocity value (in meters per second), "))
    a = float(input("What is the acceleration value (in meters per second squared), "))
    f = x + v*t + (1/2*a*t**2)
    print("Final position = ", f,"m")

  elif B == 2:
    f = float(input("What is the final position value (in meters), "))
    t = float(input("What is the change in time (in seconds), "))
    v =float(input("What is the starting velocity value (in meters per second), "))
    a =float(input("What is the acceleration value (in meters per second squared), "))
    x = f - v*t - (1/2*a*t**2)
    print("Starting position = ", x,"m")

  elif B == 3:
    f =float(input("What is the final position value (in meters), "))
    x =float(input("What is the starting position value (in meters), "))
    v =float(input("What is the starting velocity value (in meters per second), "))
    t = (f-x)/v
    print("Change in time = ", t,"s")

  elif B == 4:
    f =float(input("What is the final position value (in meters), "))
    x =float(input("What is the starting position value (in meters), "))
    t =float(input("What is the change in time (in seconds), "))
    v = (f-x)/t
    print("Starting velocity = ", v,"m/s")
  
  elif B == 5:
    f =float(input("What is the final position value (in meters), "))
    x =float(input("What is the starting position value (in meters), "))
    t =float(input("What is the change in time (in seconds), "))
    a = (f-x)/t
    print("Starting velocity = ", a,"m/s\u00b2")

  else:
    print("WHY WOULD YOU DO THIS")

elif A ==2:
  print("Not Yet")

else:
  print("BOO!")