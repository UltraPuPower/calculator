import math #NOTE: math is not directly used in the code, but it is used after replacing with the convertMath function

from variables import storeA, storeB, storeC, storeD, storeE, storeF, storeG, storeH, storeI, storeJ, storeK, storeL, storeM, storeN, storeO, storeP, storeQ, storeR, storeS, storeT, storeU, storeV, storeW, storeX, storeY, storeZ
from variables import valAnsView, valAnsMath

def convertMath(inputString):
    print('------======------')
    text = f'Converted {inputString} to '

    for code in [{'mesh': 'log','new': 'math.log'}, {'mesh': 'sin', 'new': 'math.sin'}, {'mesh': 'cos', 'new': 'math.cos'}, {'mesh': 'tan', 'new': 'math.tan'},
                {'mesh': '^', 'new': '**'}, {'mesh': '×10^', 'new': '*10**'}, {'mesh': 'Ans', 'new': f'{valAnsMath[0]}'}, {'mesh': 'π', 'new': f'math.pi'},
                {'mesh': '√', 'new': f'math.sqrt'}, {'mesh': 'e', 'new': f'math.e'}, {'mesh': 'τ', 'new': f'math.tau'}, {'mesh': 'φ', 'new': f'((1+math.sqrt(5))/2)'},
                {'mesh': 'ϲ', 'new': f'(2.99792458*10**8)'}, {'mesh': 'Ꮒ', 'new': f'(6.62607015*10**-34)'}, {'mesh': 'Ꮐ', 'new': f'(6.67430*10**-11)'},
                {'mesh': 'ց', 'new': f'(9.81)'}, {'mesh': 'Ｎ', 'new': f'(6.02214076*10**23)'}, {'mesh': 'k', 'new': f'(1.380649*10**-23)'},
                {'mesh': 'ҽ', 'new': f'(1.602176634*10**-19)'}]:
        inputString = inputString.replace(code['mesh'], code['new'])

    for code in [{'mesh': 'A', 'new': str(storeA[1])}, {'mesh': 'B', 'new': str(storeB[1])}, {'mesh': 'C', 'new': str(storeC[1])}, {'mesh': 'D', 'new': str(storeD[1])},
                    {'mesh': 'E', 'new': str(storeE[1])}, {'mesh': 'F', 'new': str(storeF[1])}, {'mesh': 'G', 'new': str(storeG[1])}, {'mesh': 'H', 'new': str(storeH[1])},
                    {'mesh': 'I', 'new': str(storeI[1])}, {'mesh': 'J', 'new': str(storeJ[1])}, {'mesh': 'K', 'new': str(storeK[1])}, {'mesh': 'L', 'new': str(storeL[1])},
                    {'mesh': 'M', 'new': str(storeM[1])}, {'mesh': 'N', 'new': str(storeN[1])}, {'mesh': 'O', 'new': str(storeO[1])}, {'mesh': 'P', 'new': str(storeP[1])},
                    {'mesh': 'Q', 'new': str(storeQ[1])}, {'mesh': 'R', 'new': str(storeR[1])}, {'mesh': 'S', 'new': str(storeS[1])}, {'mesh': 'T', 'new': str(storeT[1])},
                    {'mesh': 'U', 'new': str(storeU[1])}, {'mesh': 'V', 'new': str(storeV[1])}, {'mesh': 'W', 'new': str(storeW[1])}, {'mesh': 'X', 'new': str(storeX[1])}, 
                    {'mesh': 'Y', 'new': str(storeY[1])}, {'mesh': 'Z', 'new': str(storeZ[1])}]:
        inputString = inputString.replace(code['mesh'], code['new'])
    
    print(f'{text}{inputString}')
    return inputString

def actionCalculate(inputWindow):
    input = inputWindow.get()
    try:
        n = 0
        outputMath = eval(input)
        output = float(eval(input))
        if abs(output) >= 10000000000:
            while output > 10:
                n = n+1
                output = output/10
            if not n > 99:
                output = str(output)[:10]
                outputValue = output+"×10^"+str(n)
                errorLog = None
            else:
                errorLog = "number out of range\ntoo large"
        elif abs(output) < 0.0001 and abs(output) > 0:
            while output < 1:
                n = n-1
                output = output*10
            if not n < -99:
                output = str(output)[:10]
                outputValue = output+"×10^"+str(n)
                errorLog = None
            else:
                errorLog = "number out of range\ntoo small"
        else:
            outputValue = outputMath
            errorLog = None
    except:
        errorLog = "invalid input\ndid you properly use parentheses?"
        outputMath = 0

    if errorLog == None:
        print("Calculation successful")
        returnVal = [outputValue, outputMath, None]
        print(f'Calculation => Output: {returnVal[0]}, Math: {returnVal[1]}')
    else:
        print("Error in calculation")
        returnVal = ['', '', errorLog]
        print(f'Calculation => Error: {returnVal[2]}')
    return returnVal