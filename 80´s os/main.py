import os
import time
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
    os.system("python System/boot.py")
elif checkhwid() == False:
    print("You are not licensed to use this software")
    print("Please buy a license from https://developing.sellix.io/")
    print("Your HWID is: " + uuid)
    print("After Purshase, Create a ticket on https://discord.gg/8gSPukwg6C")
    time.sleep(99999)
else:
    print("Error while checking HWID")
    time.sleep(99999)
    

