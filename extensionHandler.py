# Script by EfazDev#0220
import os
import subprocess
import platform
import time
import json
import sys

LocalMachineOS = platform.system()
pythonVersion = sys.version_info

if LocalMachineOS == "Darwin" or LocalMachineOS == "Linux":
    os.system("clear")
elif LocalMachineOS == "win32" or LocalMachineOS == "win64" or LocalMachineOS == "Windows":
    os.system("cls")
print("Welcome to Efaz's Extension Handler!")
print("")
print("Loading Extension Requirments...")
print("")
directory = os.path.dirname(os.path.realpath(__file__))

LocalAvailableProgramLanguages = [
    [".py", "python"],
    [".java", "java"],
    [".lua", "lua"]
]
if LocalMachineOS == "Darwin":
    print("Detected Local Machine OS: " + LocalMachineOS + " (Apple Unix OS)")
elif LocalMachineOS == "win32":
    print("Detected Local Machine OS: " + LocalMachineOS + " (Windows 32bit)")
elif LocalMachineOS == "win64":
    print("Detected Local Machine OS: " + LocalMachineOS + " (Windows 64bit)")
elif LocalMachineOS == "Windows":
    print("Detected Local Machine OS: " + LocalMachineOS )
elif LocalMachineOS == "Linux":
    print("Detected Local Machine OS: " + LocalMachineOS)
else:
    print("Detected Local Machine OS: " + LocalMachineOS + " (Other OS)")

if pythonVersion.major >= 3:
    print("Python Version: v" + str(pythonVersion.major) + "." + str(pythonVersion.minor) + "." + str(pythonVersion.micro)) 
else:
    print("This version of python is not available incase of errors of the latest packages. Please update to python v3.0.0 or up")
    sys.exit()
print("")

# Checking modules installation

print("Testing for required modules...")

try:
    import discord
    print("Required module (discord) for mewt sniper is installed")
except ModuleNotFoundError:
    print("Required module (discord) for mewt sniper is not installed, installing in 2 seconds.")
    time.sleep(2)
    if LocalMachineOS == "Windows" or LocalMachineOS == "win32" or LocalMachineOS == "win64":
        os.system("pip install discord.py")
    else:
        os.system('pip3 install discord.py')
        os.system("pip install discord.py")

try:
    import requests
    print("Required module (requests) for mewt sniper is installed")
except ModuleNotFoundError:
    print("Required module (requests) for mewt sniper is not installed, installing in 2 seconds.")
    time.sleep(2)
    if LocalMachineOS == "Windows" or LocalMachineOS == "win32" or LocalMachineOS == "win64":
        os.system("pip install requests")
    else:
        os.system('pip3 install requests')
        os.system("pip install requests")

try:
    import colorama
    print("Required module (colorama) for mewt sniper is installed")
except ModuleNotFoundError:
    print("Required module (colorama) for mewt sniper is not installed, installing in 2 seconds.")
    time.sleep(2)
    if LocalMachineOS == "Windows" or LocalMachineOS == "win32" or LocalMachineOS == "win64":
        os.system("pip install colorama")
    else:
        os.system('pip3 install colorama')
        os.system("pip install colorama")

try:
    import socketio
    print("Required module (socketio) for mewt sniper is installed")
except ModuleNotFoundError:
    print("Required module (socketio) for mewt sniper is not installed, installing in 2 seconds.")
    time.sleep(2)
    if LocalMachineOS == "Windows" or LocalMachineOS == "win32" or LocalMachineOS == "win64":
        os.system('pip install python-socketio[client]')
    else:
        os.system('pip3 install python-socketio[client]')
        os.system('pip install python-socketio[client]')

try:
    import rgbprint
    print("Required module (rgbprint) for mewt sniper is installed")
except ModuleNotFoundError:
    print("Required module (rgbprint) for mewt sniper is not installed, installing in 2 seconds.")
    time.sleep(2)
    if LocalMachineOS == "Windows" or LocalMachineOS == "win32" or LocalMachineOS == "win64":
        os.system('pip install rgbprint')
    else:
        os.system('pip3 install rgbprint')
        os.system('pip install rgbprint')
    
print("Finished checking for module installation")
print("Loading Extension Settings...")

print("")

if LocalMachineOS == "Windows" or LocalMachineOS == "win32" or LocalMachineOS == "win64":
    with open(directory + '\ExtensionHandlerSettings.json', 'r') as f:
        settings = json.load(f)

    print("Loaded: Opening extensions")
    print("")

    extensions = settings["extensions"]
    order = settings["order"]
    openMewt = settings["openMewt"]

    if extensions:
        if order == "OnebyOne":
            for x in extensions:
                for y in LocalAvailableProgramLanguages:
                    if x["fileName"].endswith(y[0]): 
                        subprocess.Popen([y[1], x["fileName"]])
                        print("Running " + x["fileName"] + " aka " + x["extensionName"] + " using language: " + y[1])
            if openMewt == True:
                print("Ran all extensions, opening mewt sniper")
                subprocess.Popen(['python', directory + "\main.py"])
            else:
                print("Ran all extensions, and mewt has not been opened.")
        elif order == "FileName":
            def getSecondVariable(extenlist):
                return extenlist.fileName
            extensions.sort(key=getSecondVariable)
            for x in extensions:
                for y in LocalAvailableProgramLanguages:
                    if x["fileName"].endswith(y[0]): 
                        subprocess.Popen([y[1], x["fileName"]])
                        print("Running " + x["fileName"] + " aka " + x["extensionName"] + " using language: " + y[1])
            if openMewt == True:
                print("Ran all extensions, opening mewt sniper")
                subprocess.Popen(['python', directory + "\main.py"])
            else:
                print("Ran all extensions, and mewt has not been opened.")
        elif order == "ExtensionName":
            def getSecondVariable(extenlist):
               return extenlist.extensionName
            extensions.sort(key=getSecondVariable)
            for x in extensions:
                for y in LocalAvailableProgramLanguages:
                    if x["fileName"].endswith(y[0]): 
                        subprocess.Popen([y[1], x["fileName"]])
                        print("Running " + x["fileName"] + " aka " + x["extensionName"] + " using language: " + y[1])
            if openMewt == True:
                print("Ran all extensions, opening mewt sniper")
                subprocess.Popen(['python', directory + "\main.py"])
            else:
                print("Ran all extensions, and mewt has not been opened.")
        else:
            def getSecondVariable(extenlist):
                return extenlist["orderInList"]
            extensions.sort(key=getSecondVariable)
            for x in extensions:
                for y in LocalAvailableProgramLanguages:
                    if x["fileName"].endswith(y[0]): 
                        subprocess.Popen([y[1], x["fileName"]])
                        print("Running " + x["fileName"] + " aka " + x["extensionName"] + " using language: " + y[1])
            if openMewt == True:
                print("")
                print("Ran all extensions, opening mewt sniper")
                subprocess.Popen(['python', directory + "\main.py"])
            else:
                print("")
                print("Ran all extensions, and mewt has not been opened.")
    else:
        print("Failed to get extensions. Please make sure you put the JSON in the settings.")
        sys.exit()
else:
    with open(directory + '/ExtensionHandlerSettings.json', 'r') as f:
        settings = json.load(f)

    LocalAvailableProgramLanguages[0][1] = "python3"

    print("Loaded: Opening extensions")
    print("")

    extensions = settings["extensions"]
    order = settings["order"]
    openMewt = settings["openMewt"]

    if extensions:
        if order == "OnebyOne":
            for x in extensions:
                for y in LocalAvailableProgramLanguages:
                    if x["fileName"].endswith(y[0]): 
                        subprocess.Popen([y[1], x["fileName"]])
                        print("Running " + x["fileName"] + " aka " + x["extensionName"] + " using language: " + y[1])
            if openMewt == True:
                print("Ran all extensions, opening mewt sniper")
                subprocess.Popen(['python3', directory + "/main.py"])
            else:
                print("Ran all extensions, and mewt has not been opened.")
        elif order == "FileName":
            def getSecondVariable(extenlist):
                return extenlist.fileName
            extensions.sort(key=getSecondVariable)
            for x in extensions:
                for y in LocalAvailableProgramLanguages:
                    if x["fileName"].endswith(y[0]): 
                        subprocess.Popen([y[1], x["fileName"]])
                        print("Running " + x["fileName"] + " aka " + x["extensionName"] + " using language: " + y[1])
            if openMewt == True:
                print("Ran all extensions, opening mewt sniper")
                subprocess.Popen(['python3', directory + "/main.py"])
            else:
                print("Ran all extensions, and mewt has not been opened.")
        elif order == "ExtensionName":
            def getSecondVariable(extenlist):
               return extenlist.extensionName
            extensions.sort(key=getSecondVariable)
            for x in extensions:
                for y in LocalAvailableProgramLanguages:
                    if x["fileName"].endswith(y[0]): 
                        subprocess.Popen([y[1], x["fileName"]])
                        print("Running " + x["fileName"] + " aka " + x["extensionName"] + " using language: " + y[1])
            if openMewt == True:
                print("Ran all extensions, opening mewt sniper")
                subprocess.Popen(['python3', directory + "/main.py"])
            else:
                print("Ran all extensions, and mewt has not been opened.")
        else:
            def getSecondVariable(extenlist):
                return extenlist["orderInList"]
            extensions.sort(key=getSecondVariable)
            for x in extensions:
                for y in LocalAvailableProgramLanguages:
                    if x["fileName"].endswith(y[0]): 
                        subprocess.Popen([y[1], x["fileName"]])
                        print("Running " + x["fileName"] + " aka " + x["extensionName"] + " using language: " + y[1])
            if openMewt == True:
                print("")
                print("Ran all extensions, opening mewt sniper")
                subprocess.Popen(['python3', directory + "/main.py"])
            else:
                print("")
                print("Ran all extensions, and mewt has not been opened.")
    else:
        print("Failed to get extensions. Please make sure you put the JSON in the settings.")  
        sys.exit()