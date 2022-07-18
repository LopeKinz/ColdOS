from pick import pick
import os
from os import listdir
from os.path import isfile, join

try:
    title = "ColdOS Extentions"
    try:
        options = [f for f in listdir("System/Extentions/") if isfile(join("System/Extentions/", f))]
    except:
        options = [f for f in listdir("Extentions/") if isfile(join("Extentions/", f))]
    selection = pick(options, title, indicator='=>', default_index=0)
    assert len(selection) == 1
    option, index = selection[0]
    os.system("python Extentions/" + option)
except Exception as e:
    print(e)
    input("Press Enter to continue...")
