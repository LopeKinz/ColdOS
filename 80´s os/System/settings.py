from pick import pick
import webbrowser
import os

try:
    with open("Strings/user_config.json", "r") as f:
        settings = f.read()
except:
    with open("System/Strings/user_config.json", "r") as f:
        settings = f.read()
        
title = f"Welcome {user} to ColdOS"
options = ["Change Username","Change Password", "Change Email", "Info","Exit"]
selection = pick(options, title, indicator='=>', default_index=0)
assert len(selection) == 1
option, index = selection[0]

if option == "Change Username":
    try:
        with open("Strings/user_config.json", "w") as f:
            name = input("Enter new username: ")
        config["Username"] = name
        json.dump(config,f)
    except:
        with open("System/Strings/user_config.json", "w") as f:
            name = input("Enter new username: ")
        config["Username"] = name
        json.dump(config,f)
elif option == "Change Password":
    try:
        with open("Strings/user_config.json", "w") as f:
            name = input("Enter new Password: ")
        config["Password"] = name
        json.dump(config,f)
    except:
        with open("System/Strings/user_config.json", "w") as f:
            name = input("Enter new Password: ")
        config["Password"] = name
        json.dump(config,f)
elif option == "Change Email":
    try:
        with open("Strings/user_config.json", "w") as f:
            name = input("Enter new Email: ")
        config["Email"] = name
        json.dump(config,f)
    except:
        with open("System/Strings/user_config.json", "w") as f:
            name = input("Enter new Email: ")
        config["Email"] = name
        json.dump(config,f)
elif option == "Info":
    os.system("python System/debug.py")
elif option == "Exit":
    os.system("python System/main_menu.py")
