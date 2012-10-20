#!/usr/bin/python
# -*- coding: utf-8 -*-

import android
import time
import os
import sys
from random import random

from config import *

droid = android.Android()

def dataDir():
    return CONFIG.getAppPath() + "data/"

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
    ran = int(random() * 1000)
    index = index.replace("%(version)s", str(ran))

    version =  str(CONFIG.data["version"])
    index = index.replace("%(appVersion)s", version)

    path = CONFIG.data["projectRelativePath"]
    index = index.replace("%(projectRelPath)s", path)

    indexFile.write(index)
    indexFile.close()



droid.addOptionsMenuItem('Sobre', 'app-about', None, "ic_menu_info_details")
droid.addOptionsMenuItem('Sair', 'app-quit', None, "ic_lock_power_off")

generateIndex()
droid.webViewShow(CONFIG.baseUrl() + "index.html")
droid.batteryStartMonitoring()

if __name__ == '__main__':
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

            elif eventResult["name"] == "app-about":
                droid.dialogCreateAlert("Sobre", CONFIG.data["about"])
                droid.dialogSetPositiveButtonText("sim")
                droid.dialogShow()

        except Exception as e:
            print e
            droid.log(str(e))
            pass