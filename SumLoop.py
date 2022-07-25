import sys
import os
from time import sleep

try:
    num = int(input("Write how many numbers you want to calculate: "))
except:
    print("The input is not valid, please try again")
    sleep(3)
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)  # This restarts the program

i = 0
while i <= num:
    sum = i + (i - 1)
    print(f"Current Number {i} Previous Number {i-1} Sum: {sum}")
    i += 1
