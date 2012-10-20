#!/usr/bin/python
# -*- coding: utf-8 -*-

import android
import time
import os
import sys
from random import random

droid = android.Android()

def baseUrl():
    return "file://" + os.getcwd()[len("/mnt"):] + "/scripts/"

def dataDir():
    return os.getcwd() + "/scripts/projetos/snake_battery/data/"

def speak(say):
    if say != None:
        result = droid.ttsSpeak(say)
        return result.error is None
    else:
        return None

def generateIndex():
    template = open(dataDir() + "html/template.html", "r")

    index = template.read()
    template.close()

    indexFile = open(os.getcwd() + "/scripts/index.html", "w")
    ram = int(random() * 1000)
    indexFile.write(index.replace("%(version)s", str(ram)))


droid.addOptionsMenuItem('Quit', 'app-quit', None, "ic_lock_power_off")
generateIndex()
droid.webViewShow(baseUrl() + "index.html")
droid.batteryStartMonitoring()

while True:
    try:
        time.sleep(1)
        eventResult = droid.eventWait(10000).result
            
        if eventResult == None:
            continue

        elif eventResult["name"] == "documentReady":
            result = droid.batteryGetLevel().result
            droid.eventPost('batteryLevel', str(result))
        
        elif eventResult["name"] == "say":
            result = droid.batteryGetLevel().result
            speak(str(result)+"%");

        elif eventResult["name"] == "log":
            print eventResult["data"]
            droid.log(eventResult["data"])

        elif eventResult["name"] == "app-quit":
            droid.dialogCreateAlert("Sair", "Sair da aplicação?")
            droid.dialogSetPositiveButtonText("sim")
            droid.dialogSetNegativeButtonText("não")
            droid.dialogShow()
            response = droid.dialogGetResponse().result
            
            if response['which'] == 'positive':
                droid.batteryStopMonitoring()
                break
    except Exception as e:
        print e
        droid.log(str(e))
        pass