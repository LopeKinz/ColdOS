from pick import pick
import os
import webbrowser


title = "ColdOS Extentions List"
options = ["PinkyDiscordSpammer (Free)","Exit"]
selection = pick(options, title, indicator='=>', default_index=0)
assert len(selection) == 1
option, index = selection[0]

if option == "PinkyDiscordSpammer (Free)":
    webbrowser.open("https://github.com/LopeKinz/PinkyDiscordSpammer")
if option == "Exit":
    os.system("python main_menu.py")