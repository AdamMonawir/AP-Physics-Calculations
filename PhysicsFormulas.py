from vpython import *

A = int(input("Pick which problem you have, "))

if A == 1:
    x = int(input("What is the starting position value (in meters), "))
    t = int(input("What is the change in time (in seconds), "))
    v = int(input("What is the starting velocity value (in meters per second), "))
    f = x + v*t
    print("Final position = ", f,"m")

elif A == 2:
    f = int(input("What is the final position value (in meters), "))
    t = int(input("What is the change in time (in seconds), "))
    v = int(input("What is the starting velocity value (in meters per second), "))
    x = f - v*t
    print("Final position = ", x,"m")

elif A == 3:
    f = int(input("What is the final position value (in meters), "))
    x = int(input("What is the starting position value (in meters), "))
    v = int(input("What is the starting velocity value (in meters per second), "))
    t = (f-x)/v
    print("Final position = ", t,"s")

elif A == 4:
    f = int(input("What is the final position value (in meters), "))
    x = int(input("What is the starting position value (in meters), "))
    t = int(input("What is the change in time (in seconds), "))
    v = (f-x)/t
    print("Final position = ", v,"m/s")

else:
    print("WHY WOULD YOU DO THIS")