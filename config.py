from singleton import Singleton
import os
import json

@Singleton
class Config(object):
    data = None

    def __init__(self):
        
        confFile = open(self.getAppPath() + "config.json")
        jsonConf = confFile.read()
        confFile.close()

        self.data = json.loads(jsonConf)

    def dataUrl(self):
        return self.baseUrl() + self.data["projectRelativePath"] + "data/"
        
    def baseUrl(self):
        return "file://" + os.getcwd()[len("/mnt"):] + "/scripts/"

    def getAppPath(self):
        lastSlash = __file__.rfind("/")

        return __file__[:lastSlash + 1]


CONFIG = Config.Instance()