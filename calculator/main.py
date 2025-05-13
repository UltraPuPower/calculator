from screenWelcome import screenWelcomeDef
from screenCalculator import screenCalculatorDef

from variables import insertListView, insertListMath

debug = True

def debugger(message):
    if debug == True:
        print(message)

def actionBaseDef(viewInput, viewLength, mathInput, mathLength, windowView, windowMath):
    windowView.insert("end", viewInput)
    windowMath.insert("end", mathInput)
    insertListView.append(viewLength)
    insertListMath.append(mathLength)
    debugger(f'View:{insertListView}')
    debugger(f'Math:{insertListMath}')

screenCalculatorDef()

#screenWelcomeDef(screenCalculatorDef) #NOTE: Admin password is 'password'