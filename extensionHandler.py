# Script by EfazDev#0220

import os
import subprocess
import json

print("Welcome to Efaz's Extension Handler!")
print("Loading settings.json...")
directory = os.path.dirname(os.path.realpath(__file__))

with open(directory + '\ExtensionHandlerSettings.json', 'r') as f:
    settings = json.load(f)

print("Loaded: Opening extensions")

extensions = settings["extensions"]
order = settings["order"]
openMewt = settings["openMewt"]

if extensions:
    if order == "OnebyOne":
        for x in extensions:
            if x["fileName"].endswith(".py"): 
                subprocess.Popen(['python', x["fileName"]])
                print("Running " + x["fileName"] + " aka " + x["extensionName"])
            if x["fileName"].endswith(".java"): 
                subprocess.Popen(['java', x["fileName"]])
                print("Running " + x["fileName"] + " aka " + x["extensionName"])
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
            if x["fileName"].endswith(".py"): 
                subprocess.Popen(['python', x["fileName"]])
                print("Running " + x["fileName"] + " aka " + x["extensionName"])
            if x["fileName"].endswith(".java"): 
                subprocess.Popen(['java', x["fileName"]])
                print("Running " + x["fileName"] + " aka " + x["extensionName"])
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
            if x["fileName"].endswith(".py"): 
                subprocess.Popen(['python', x["fileName"]])
                print("Running " + x["fileName"] + " aka " + x["extensionName"])
            if x["fileName"].endswith(".java"): 
                subprocess.Popen(['java', x["fileName"]])
                print("Running " + x["fileName"] + " aka " + x["extensionName"])
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
            if x["fileName"].endswith(".py"): 
                subprocess.Popen(['python', x["fileName"]])
                print("Running " + x["fileName"] + " aka " + x["extensionName"])
            if x["fileName"].endswith(".java"): 
                subprocess.Popen(['java', x["fileName"]])
                print("Running " + x["fileName"] + " aka " + x["extensionName"])
        if openMewt == True:
            print("Ran all extensions, opening mewt sniper")
            subprocess.Popen(['python', directory + "\main.py"])
        else:
            print("Ran all extensions, and mewt has not been opened.")
else:
    print("Failed to get extensions. Please make sure you put the JSON in the settings.")