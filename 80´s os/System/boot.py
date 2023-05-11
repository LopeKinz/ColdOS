import colorama
import sys
import os
from slowprint.slowprint import *
import time
import psutil
import json
import subprocess
import requests

def clr():
    os.system("cls" if os.name == "nt" else "clear")
    
def getLisencekey():
    if os.name == 'nt':
        return (
            subprocess.check_output('wmic csproduct get uuid')
            .decode()
            .split('\n')[1]
            .strip()
        )
    else:
        return("Error while getting Windows HWID")
    
def checkhwid():
    res = requests.get('https://pastebin.com/raw/sZ123VPy')
    hwid = getLisencekey()
    return hwid in res.text

uuid = getLisencekey()
checkhwid()

if checkhwid() == True:
    pass
elif checkhwid() == False:
    print("You are not licensed to use this software")
    print("Please buy a license from https://developing.sellix.io/")
    print(f"Your HWID is: {uuid}")
    print("After Purshase, Create a ticket on https://discord.gg/8gSPukwg6C")
    time.sleep(99999)
else:
    print("Error while checking HWID")
    time.sleep(99999)

slowprint("Booting ColdOS...", 0.05)
time.sleep(0.5)
slowprint(f"Ram = {psutil.virtual_memory()}", 0.05)
slowprint("Starting Up...", 0.05)
time.sleep(5)
clr()
try:
    try:
        with open("System/Strings/boot.json", "r") as f:
            config = json.load(f)
        if config["First_Start"] == "0":
            slowprint("Welcome to ColdOS!", 0.05)
            time.sleep(0.5)
            slowprint("Please enter your username:", 0.05)
            username = input()
            slowprint(f"Welcome {username}!", 0.05)
            time.sleep(0.5)
            slowprint("Please enter your password:", 0.05)
            password = input()
            slowprint("Please enter your password again:", 0.05)
            password_again = input()
            if password == password_again:
                slowprint("Password accepted!", 0.05)
                time.sleep(0.5)
                slowprint("Please enter your email:", 0.05)
                email = input()
                slowprint("Please enter your email again:", 0.05)
                email_again = input()
                if email == email_again:
                    slowprint("Email accepted!", 0.05)
                    time.sleep(0.5)
                    try:
                        with open("System/Strings/boot.json", "w") as f:
                            config["First_Start"] = "1"
                            json.dump(config, f)
                        with open("System/Strings/user_config.json", "w") as f:
                            config["Username"] = username
                            config["Password"] = password
                            config["Email"] = email
                            json.dump(config, f)
                    except:
                        with open("Strings/boot.json", "w") as f:
                            config["First_Start"] = "1"
                            json.dump(config, f)
                        with open("Strings/user_config.json", "w") as f:
                            config["Username"] = username
                            config["Password"] = password
                            config["Email"] = email
                            json.dump(config, f)            
        if config["First_Start"] == "1":
            try:
                with open("System/Strings/user_config.json", "r") as f:
                    config = json.load(f)
                    slowprint("Welcome back!", 0.05)
                    time.sleep(0.5)
                    slowprint("Please enter your password:", 0.05)
                    password = input()
                    if password == config["Password"]:
                        slowprint("Password accepted!", 0.05)
                        time.sleep(0.5)
                        slowprint("Starting in Retail Mode...", 0.05)
                        try:
                            os.system("python System/main_menu.py")
                        except Exception as e:
                            print(e)
                            input("Press Enter to continue...")
            except:
                    with open("Strings/user_config.json", "r") as f:
                        config = json.load(f)
                    slowprint("Welcome back!", 0.05)
                    time.sleep(0.5)
                    slowprint("Please enter your password:", 0.05)
                    password = input()
                    if password == config["Password"]:
                        slowprint("Password accepted!", 0.05)
                        time.sleep(0.5)
                        slowprint("Starting in Retail Mode...", 0.05)
                        try:
                            os.system("python System/main_menu.py")
                        except Exception as e:
                            print(e)
                            input("Press Enter to continue...")
    except:
        with open("Strings/boot.json", "r") as f:
            config = json.load(f)
        if config["First_Start"] == "0":
            slowprint("Welcome to ColdOS!", 0.05)
            time.sleep(0.5)
            slowprint("Please enter your username:", 0.05)
            username = input()
            slowprint(f"Welcome {username}!", 0.05)
            time.sleep(0.5)
            slowprint("Please enter your password:", 0.05)
            password = input()
            slowprint("Please enter your password again:", 0.05)
            password_again = input()
            if password == password_again:
                slowprint("Password accepted!", 0.05)
                time.sleep(0.5)
                slowprint("Please enter your email:", 0.05)
                email = input()
                slowprint("Please enter your email again:", 0.05)
                email_again = input()
                if email == email_again:
                    slowprint("Email accepted!", 0.05)
                    time.sleep(0.5)
                    try:
                        with open("System/Strings/boot.json", "w") as f:
                            config["First_Start"] = "1"
                            json.dump(config, f)
                        with open("System/Strings/user_config.json", "w") as f:
                            config["Username"] = username
                            config["Password"] = password
                            config["Email"] = email
                            json.dump(config, f)
                    except:
                        with open("Strings/boot.json", "w") as f:
                            config["First_Start"] = "1"
                            json.dump(config, f)
                        with open("Strings/user_config.json", "w") as f:
                            config["Username"] = username
                            config["Password"] = password
                            config["Email"] = email
                            json.dump(config, f)            
        if config["First_Start"] == "1":
            try:
                with open("System/Strings/user_config.json", "r") as f:
                    config = json.load(f)
                    slowprint("Welcome back!", 0.05)
                    time.sleep(0.5)
                    slowprint("Please enter your password:", 0.05)
                    password = input()
                    if password == config["Password"]:
                        slowprint("Password accepted!", 0.05)
                        time.sleep(0.5)
                        slowprint("Starting in Retail Mode...", 0.05)
                        try:
                            os.system("python System/main_menu.py")
                        except Exception as e:
                            print(e)
                            input("Press Enter to continue...")
            except:
                    with open("Strings/user_config.json", "r") as f:
                        config = json.load(f)
                    slowprint("Welcome back!", 0.05)
                    time.sleep(0.5)
                    slowprint("Please enter your password:", 0.05)
                    password = input()
                    if password == config["Password"]:
                        slowprint("Password accepted!", 0.05)
                        time.sleep(0.5)
                        slowprint("Starting in Retail Mode...", 0.05)
                        try:
                            os.system("python System/main_menu.py")
                        except Exception as e:
                            print(e)
                            input("Press Enter to continue...")
except Exception as e:
    print(e)
    input("Press Enter to continue...")
    


