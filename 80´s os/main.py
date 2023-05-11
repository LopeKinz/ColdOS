import os
import time
import subprocess
import requests

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
    os.system("python System/boot.py")
elif checkhwid() == False:
    print("You are not licensed to use this software")
    print("Please buy a license from https://developing.sellix.io/")
    print(f"Your HWID is: {uuid}")
    print("After Purshase, Create a ticket on https://discord.gg/8gSPukwg6C")
    time.sleep(99999)
else:
    print("Error while checking HWID")
    time.sleep(99999)
    

