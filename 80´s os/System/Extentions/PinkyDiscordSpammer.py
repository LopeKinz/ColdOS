import sys, threading, discord, requests, ctypes, os, json
from itertools import cycle
from colored import fg, attr
import time
import datetime
import random
from threading import Thread
import platform
from discord.ext import commands
import asyncio

intents = discord.Intents(messages=True, members=True)
client = commands.Bot(command_prefix=commands.when_mentioned_or('+'), intents=intents)

class colors:

    red = fg('#DA2525')
    reset = attr('reset')
    gray = fg('#8D8C8C')





def opt():
    logo = (f"""{colors.reset}
                                [Methods]
                                [1] Mass DM
                                [2] Info                  
    """)
    return logo

async def dmall():
    for guild in client.guilds:
        async for member in guild.fetch_members(limit=None):
            message = input("Enter Message:     ")
            try:
                await member.send(message)
                print(f"Sent {member.name} a DM.")
            except:
                print(f"Couldn't DM {member.name}.")
        print("Sent all the server a DM.")

def info():
    print("Instagram : Pinkyhax\nA Mass DM Bot Script\nSends DM Messages to all users where the bot is on it!")


def token():
    new_func()

def new_func():
    asyncio.create_task(dmall())


@client.event
async def on_ready():
    print("Bot running with:")
    print("Username: ", client.user.name)
    print("User ID: ", client.user.id)
    print(opt())
    choice = input("")
    if choice == "1":
        token()
    elif choice == "2":
        info()

def splash():
    logo = (f"""{colors.reset}
                   
                    _____ _       _            _____  _                       _    _____                                           
                    |  __ (_)     | |          |  __ \(_)                     | |  / ____|                                          
                    | |__) | _ __ | | ___   _  | |  | |_ ___  ___ ___  _ __ __| | | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
                    |  ___/ | '_ \| |/ / | | | | |  | | / __|/ __/ _ \| '__/ _` |  \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
                    | |   | | | | |   <| |_| | | |__| | \__ \ (_| (_) | | | (_| |  ____) | |_) | (_| | | | | | | | | | | |  __/ |   
                    |_|   |_|_| |_|_|\_\\__, | |_____/|_|___/\___\___/|_|  \__,_| |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                        __/ |                                           | |                                        
                                        |___/                                            |_|                                        

                                                            
                                                                      
                                                    Author: Pinkyhax                       
    """)
    return logo

print(splash())
print("Works only For BOTS! Not for Selfbots.")
bot_token = input("Enter Bot Token:    ")
client.run(bot_token)