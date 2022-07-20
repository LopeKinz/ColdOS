from pick import pick
import webbrowser
import os
import subprocess
import requests
import time

def getLisencekey():
    if os.name == 'nt':
        hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        return hwid
    else:
        return("Error while getting Windows HWID")
    
def checkhwid():
        res = requests.get('https://pastebin.com/raw/sZ123VPy')
        hwid = getLisencekey()
        if hwid in res.text:
            return True
        else:
            return False

uuid = getLisencekey()
checkhwid()

if checkhwid() == True:
    pass
elif checkhwid() == False:
    print("You are not licensed to use this software")
    print("Please buy a license from https://developing.sellix.io/")
    print("Your HWID is: " + uuid)
    print("After Purshase, Create a ticket on https://discord.gg/8gSPukwg6C")
    time.sleep(99999)
else:
    print("Error while checking HWID")
    time.sleep(99999)

def pick_os():
    title = f"ColdOS Settings"
    options = ["Change Username","Change Password", "Change Email", "Info","Exit"]
    selection = pick(options, title, indicator='=>', default_index=0)
    assert len(selection) == 1
    option, index = selection[0]
    return option

option = pick_os()
if option == "Change Username":
    try:
        with open("Strings/user_config.json", "w") as f:
            name = input("Enter new username: ")
        config["Username"] = name
        json.dump(config,f)
        pick_os()
    except:
        with open("System/Strings/user_config.json", "w") as f:
            name = input("Enter new username: ")
        config["Username"] = name
        json.dump(config,f)
        pick_os()
elif option == "Change Password":
    try:
        with open("Strings/user_config.json", "w") as f:
            name = input("Enter new Password: ")
        config["Password"] = name
        json.dump(config,f)
        pick_os()
    except:
        with open("System/Strings/user_config.json", "w") as f:
            name = input("Enter new Password: ")
        config["Password"] = name
        json.dump(config,f)
        pick_os()
elif option == "Change Email":
    try:
        with open("Strings/user_config.json", "w") as f:
            name = input("Enter new Email: ")
        config["Email"] = name
        json.dump(config,f)
        pick_os()
    except:
        with open("System/Strings/user_config.json", "w") as f:
            name = input("Enter new Email: ")
        config["Email"] = name
        json.dump(config,f)
        pick_os()
elif option == "Info":
    os.system("python System/debug.py")
elif option == "Exit":
    os.system("python System/main_menu.py")
