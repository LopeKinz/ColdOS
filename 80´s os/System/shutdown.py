import os
from slowprint.slowprint import *
import sys

slowprint("Do you really want to Shut Down this OS?", 0.5)
choice = input("(y/n) ")
if choice == "y":
    slowprint("Shutting Down...", 0.5)
    time.sleep(1)
    sys.exit()
elif choice == "n":
    os.system("python System/main_menu.py")