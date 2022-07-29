import sys
import os
from time import sleep
import random
from termcolor import colored  # colors

print(colored("\nYour options:", "red"))
print("[0] Rock\n[1] Paper\n[2] Scissors")

# Validation
try:
    opt = int(input(colored("Choose your option: ", "blue")))
    if opt != 0 and opt != 1 and opt != 2:
        print("Invalid Number: Check the options list for the acceptable numbers.\nRestarting...")
        sleep(3)
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)  # Restarts the program
except:
    print("Invalid Character: Only the numbers at the options list are accepted.\nRestarting...")
    sleep(3)
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

# Computer choice
bot = random.randrange(0, 2)
print(f"Coputer chose {bot}")

if (opt == 0 and bot == 2) or (opt == 1 and bot == 0) or (opt == 2 and bot == 1):
    print(colored("Congratulations! You won!", "green"))
else:
    print(colored("You lost! Better luck next time...", "red"))

# Play again
choice = input("Want to play again? (Y / N): ")
low = choice.lower()  # This way it's possible to write "Y" and "y"

if low == "y":
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
elif low == "n":
    print("\nGoodbye! Thank you for playing...")
    sleep(2)
    sys.exit(0)
