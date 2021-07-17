#!/usr/bin/python3

import sys
import time
from tabulate import tabulate
 
# Defining function 1 (wait, dot, wait, dot, wait)  
def wait_f1():
  time.sleep(1) # Sleep for 1 seconds
  print(".\n")
  time.sleep(1) # Sleep for 1 seconds
  print(".\n")
  time.sleep(1) # Sleep for 1 seconds

# Defining function 2 ( creating empty space )
def border_f2():  
  print("\n" + "\n")

# Create border for bot text  

bot_text_1 = """
Alaya BOT :) ;) :D
"""
table = [[bot_text_1]]
bot_output = tabulate(table, tablefmt='grid')

print(bot_output)  # invoke function border_f2  
   
border_f2()  # invoke function border_f2  
  
time.sleep(1) # Sleep for 1 seconds

print("Hello Alaya's World!")

wait_f1()       # invoke wait_f1 function

color1 = input("What is your favorite color?")

wait_f1()       # invoke wait_f1 function

print("Your favorite color is " + color1)

wait_f1()       # invoke wait_f1 function

color2 = input("What is your second favorite color?")

wait_f1()       # invoke wait_f1 function

print("Your second favorite color is " + color2)

wait_f1()       # invoke wait_f1 function

print("I like "  + color2 + " as well!!!")

wait_f1()       # invoke wait_f1 function

number1 = input("What is your favorite number?")

wait_f1()       # invoke wait_f1 function

print("Your favorite number is " + number1)

wait_f1()       # invoke wait_f1 function

number2 = input("What is your second favorite number?")

wait_f1()       # invoke wait_f1 function

print("Your second favorite number is " + number2)

number3 = int(number1) + int(number2)

wait_f1()       # invoke wait_f1 function

print("I like "  + str(number3) + " !!!")

wait_f1()       # invoke wait_f1 function

print(":)\n" + ";)\n" + ":D\n" + ":)\n" + ";)\n" + ":D")

wait_f1()       # invoke wait_f1 function

print("Byeee!!!!")

border_f2()  # invoke function border_f2 

print(bot_output)  # invoke function border_f2
