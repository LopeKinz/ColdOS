from pick import pick
import os
from os import listdir
from os.path import isfile, join
import subprocess
import time
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
    title = "ColdOS Extentions"
    try:
        options = [f for f in listdir("System/Extentions/") if isfile(join("System/Extentions/", f))]
    except:
        options = [f for f in listdir("Extentions/") if isfile(join("Extentions/", f))]
    selection = pick(options, title, indicator='=>', default_index=0)
    assert len(selection) == 1
    option, index = selection[0]
    os.system("python System/Extentions/" + option)
except Exception as e:
    print(e)
    input("Press Enter to continue...")
