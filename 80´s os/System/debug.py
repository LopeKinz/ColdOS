import sys # Importing the system module
import os # Importing the os module

Version = "1.0.0" # Version of the program
Build = "Stable" # Build of the program
Mode = "Debug" # Mode of the program
Type = "Normal" # Type of the program

print("ColdOS " + Version + " " + Build + " " + Mode + " " + Type) # Printing the version of the program
print("") # Printing a blank line
input("Press Enter to continue...") # Waiting for the user to press enter
os.system("cls") # Clearing the screen
os.system("python System/main_menu.py") # Running the main menu