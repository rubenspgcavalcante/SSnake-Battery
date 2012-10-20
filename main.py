#!/usr/bin/python
# -*- coding: utf-8 -*-

import android
import time
import os
from random import random

droid = android.Android()

def baseUrl():
    return "file://" + os.getcwd()[len("/mnt"):] + "/scripts/"

def dataDir():
    return os.getcwd() + "/scripts/projetos/snake_battery/data/"

def speak(say):
    if say != None:
        result = droid.ttsSpeak(say)
        print result
        return result.error is None
    else:
        return None

def generateIndex():
    print os.getcwd()
    template = open(dataDir() + "html/template.html", "r")

    index = template.read()
    template.close()

    indexFile = open(os.getcwd() + "/scripts/index.html", "w")
    ram = int(random() * 1000)
    indexFile.write(index.replace("%(version)s", str(ram)))


droid.addOptionsMenuItem('Quit', 'menu-quit', None, "ic_lock_power_off")
generateIndex()
droid.webViewShow(baseUrl() + "index.html")
droid.batteryStartMonitoring()

while True:
    time.sleep(1)
    eventResult = droid.eventWait(10000).result
        
    if eventResult == None:
        continue

    elif eventResult["name"] == "documentReady":
        result = droid.batteryGetLevel().result
        droid.eventPost('batteryLevel', str(result))
    
    elif eventResult["name"] == "say":
        speak(eventResult["data"])

    elif eventResult["name"] == "log":
        print eventResult["data"];

    elif eventResult["name"] == "menu-quit":
        droid.batteryStopMonitoring()
        break