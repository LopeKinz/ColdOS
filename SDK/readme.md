SDK For ColdOS Extentions

What do you need to Run an Extention?


Import Libarys:
```py
import os
```

At the End of Script or If Error:
```py
os.system("python System/main_menu.py")
```

Optional

```py
import requests
import subprocess
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
```

