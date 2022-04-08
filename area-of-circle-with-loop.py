import math
#implement a catch system for area calculator using while loop and try
while True:
    try:
        r = float(input("What's r? "))
        pi = math.pi
        r2 = pow (r, 2)
        pir2 = pi * r2
    except ValueError:
        print("r is not a number. Try again ")
    else:
        break
print (f"The area of the circle is: {pir2}")
