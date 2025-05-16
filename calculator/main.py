from screenWelcome import screenWelcomeDef
from screenCalculator import screenCalculatorDef

from variables import debug

if debug == True:
    screenCalculatorDef()
else:
    screenWelcomeDef(screenCalculatorDef) #NOTE: Admin password is 'password'