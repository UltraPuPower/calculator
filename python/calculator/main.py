from screenWelcome import screenWelcomeDef
from screenCalculator import screenCalculatorDef

from variables import debugMode, loggedIn

def mainCalculator():
    if debugMode == True:
        loggedIn.setState(True)
        loggedIn.setUser('Admin')
        screenCalculatorDef()
    else:
        screenWelcomeDef(screenCalculatorDef) #NOTE: Admin password is 'password'

mainCalculator()