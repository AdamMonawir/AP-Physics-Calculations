from vpython import *

A = int(input("Pick which problem you have, "))

if A == 1:
    x = int(input("What is starting position value (in meters), "))
    t = int(input("What is starting time value (in seconds), "))
    v = int(input("What is starting velocity value (in meters per second), "))

    f = x + v*t
    print("Final position = ", f,"m")
elif A > 1:
    print("Why would I do this?")
else:
    print("HOW!!")