from screenWelcome import screenWelcomeDef
from screenCalculator import screenCalculatorDef

from variables import debugMode, loggedIn

from langControl import setLangPref

def mainCalculator():
    if debugMode == True:
        loggedIn.setState(True)
        loggedIn.setUser('Admin')
        setLangPref()
        screenCalculatorDef()
    else:
        screenWelcomeDef(screenCalculatorDef) #NOTE: Admin password is 'password'

mainCalculator()