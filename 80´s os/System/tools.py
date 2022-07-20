from pick import pick
import os
import webbrowser
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
print(checkhwid())
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
    

title = "ColdOS Extentions List"
options = ["PinkyDiscordSpammer (Free)","Exit"]
selection = pick(options, title, indicator='=>', default_index=0)
assert len(selection) == 1
option, index = selection[0]

if option == "PinkyDiscordSpammer (Free)":
    webbrowser.open("https://github.com/LopeKinz/PinkyDiscordSpammer")
if option == "Exit":
    os.system("python System/main_menu.py")