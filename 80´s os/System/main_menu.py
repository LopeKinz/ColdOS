import os
import sys
from colorama import init, Fore, Back, Style
import time
from pick import pick
import json
import subprocess
import requests

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

try:
    with open("Strings/boot.json", "r") as f:
        settings = json.load(f)
        mode = settings["boot_type"]
except:
    with open("System/Strings/boot.json", "r") as f:
        settings = json.load(f)
        mode = settings["boot_type"]

try:
    try:
        with open("Strings/user_config.json", "r") as f:
            config = json.load(f)
            user = config["Username"]
        if mode == "retail":
            title = f"Welcome {user} to ColdOS"
            options = ["Tools","Extentions", "Settings", "Shutdown"]
            selection = pick(options, title, indicator='=>', default_index=0)
            assert len(selection) == 1
            option, index = selection[0]
            try:
                    if option == "Tools":
                        os.system("python System/tools.py")
                    if option == "Extentions":
                        os.system("python System/extentions.py")
                    if option == "Settings":
                        os.system("python System/settings.py")
                    if option == "Shutdown":
                        os.system("python System/shutdown.py")
            except Exception as e:
                    print(e)
                    input("Press Enter to continue...")
        if mode == "debug":
            title = f"Welcome {user} to ColdOS"
            options = ["Tools","Extentions", "Settings", "Shutdown","Debug"]
            selection = pick(options, title, indicator='=>', default_index=0)
            assert len(selection) == 1
            option, index = selection[0]
            try:
                if option == "Tools":
                    os.system("python System/tools.py")
                if option == "Extentions":
                    os.system("python System/extentions.py")
                if option == "Settings":
                    os.system("python System/settings.py")
                if option == "Shutdown":
                    os.system("python System/shutdown.py")
                if option == "Debug":
                    os.system("python System/debug.py")
            except Exception as e:
                print(e)
                input("Press Enter to continue...")
    except:
        with open("System/Strings/user_config.json", "r") as f:
            config = json.load(f)
            user = config["Username"]
        if mode == "retail":
            title = f"Welcome {user} to ColdOS"
            options = ["Tools","Extentions", "Settings", "Shutdown"]
            selection = pick(options, title, indicator='=>', default_index=0)
            assert len(selection) == 1
            option, index = selection[0]
            try:
                    if option == "Tools":
                        os.system("python System/tools.py")
                    if option == "Extentions":
                        os.system("python System/extentions.py")
                    if option == "Settings":
                        os.system("python System/settings.py")
                    if option == "Shutdown":
                        os.system("python System/shutdown.py")
            except Exception as e:
                    print(e)
                    input("Press Enter to continue...")
        if mode == "debug":
            title = f"Welcome {user} to ColdOS"
            options = ["Tools","Extentions", "Settings", "Shutdown","Debug"]
            selection = pick(options, title, indicator='=>', default_index=0)
            assert len(selection) == 1
            option, index = selection[0]
            try:
                if option == "Tools":
                    os.system("python System/tools.py")
                if option == "Extentions":
                    os.system("python System/extentions.py")
                if option == "Settings":
                    os.system("python System/settings.py")
                if option == "Shutdown":
                    os.system("python System/shutdown.py")
                if option == "Debug":
                    os.system("python System/debug.py")
            except Exception as e:
                print(e)
                input("Press Enter to continue...")
except Exception as e:
    print(e)
    input("Press Enter to continue...")
    