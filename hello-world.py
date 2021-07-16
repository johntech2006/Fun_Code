#!/usr/bin/python3

import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("Hello Alaya's World!")

print("Your favorite color is", sys.argv[1], "!!!")

text = input("What is your second favorite color?")

print("Your second favorite color is", text)
print("I like", text, "as well!!! ;)")
