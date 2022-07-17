import os
import sys
from colorama import init, Fore, Back, Style
import time
from pick import pick
import json
try:
    with open("Strings/user_config.json", "r") as f:
        config = json.load(f)
        user = config["Username"]
    title = f"Welcome {user} to ColdOS"
    options = ["Tools","Extentions", "Settings", "Shutdown"]
    selection = pick(options, title, indicator='=>', default_index=0)
    assert len(selection) == 1
    option, index = selection[0]
    try:
        if option == "Tools":
            os.system("python tools.py")
        if option == "Extentions":
            os.system("python extentions.py")
        if option == "Settings":
            os.system("python settings.py")
        if option == "Shutdown":
            os.system("python shutdown.py")
    except Exception as e:
        print(e)
        input("Press Enter to continue...")
except Exception as e:
    print(e)
    input("Press Enter to continue...")