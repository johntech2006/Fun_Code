#!/usr/bin/python3

import sys
 
# total arguments
#n = len(sys.argv)
#print("Total arguments passed:", n)
 
# Arguments passed
#print("\nName of Python script:", sys.argv[0])

color1 = str(sys.argv[1])

print("Hello Alaya's World!")

print("Your favorite color is " + color1)

color2 = input("What is your second favorite color?")
color3 = str(color2)
print("Your second favorite color is " + color3)

print("I like "  + color3 + " as well!!! ;)")
