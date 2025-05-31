import os

filepath = os.path.dirname(__file__)

valAnsView = ['0']

storeA = ['0']; storeB = ['0']; storeC = ['0']; storeD = ['0']; storeE = ['0']; storeF = ['0']; storeG = ['0']
storeH = ['0']; storeI = ['0']; storeJ = ['0']; storeK = ['0']; storeL = ['0']; storeM = ['0']; storeN = ['0']
storeO = ['0']; storeP = ['0']; storeQ = ['0']; storeR = ['0']; storeS = ['0']; storeT = ['0']; storeU = ['0']
storeV = ['0']; storeW = ['0']; storeX = ['0']; storeY = ['0']; storeZ = ['0']

insertListView = []

debugMode = True

def debugger(message):
    if debugMode == True:
        print(message)

class loginClass:
    def __init__(self, boolean):
        self.language = boolean

    def getState(self):
        return self.language
    
    def setState(self, boolean):
        self.language = boolean
    
    def getUser(self):
        return self.username
    
    def setUser(self, string):
        self.username = string

loggedIn = loginClass(False)

class Language:
    def __init__(self, language):
        self.language = language

    def getLang(self):
        return self.language
    
    def setLang(self, language):
        self.language = language
        debugger(f"Language was changed into {language}")

language = Language("English")

langList = ["English", "Dutch"]