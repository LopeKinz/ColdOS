import os

print("Welcome to ColdOS Setup")
print("This program will help you setup your ColdOS")
print("Installing Python independentcys...")
try:
    os.system("pip install colorama pick slowprint psutil")
except Exception as e:
    print(e)
    input("Press Enter to continue...")