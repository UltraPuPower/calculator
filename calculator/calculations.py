import math #NOTE: math is not directly used in the code, but it is used after replacing with the convertMath function
import re

from variables import valAnsView
from variables import storeA, storeB, storeC, storeD, storeE, storeF, storeG, storeH, storeI, storeJ, storeK, storeL, storeM, storeN, storeO, storeP, storeQ, storeR, storeS, storeT, storeU, storeV, storeW, storeX, storeY, storeZ

from variables import debugger

def mathReplacer(input):

    savedInput = input

    def constantReplacer(line, target, replacement):
        cleanTarget = re.escape(target)
        line = re.sub(rf'(^|[\+\-\*/\(]){cleanTarget}([\+\-\*/\)\(]|$)', rf'\1{replacement}\2', line)
        return line
    
    #operators
    for filter in [{"t": '×', "r": '*'}, {"t": '^', "r": '**'}, {"t": '÷', "r": '/'}, {"t": '√', "r": 'math.sqrt'}]:
        input = input.replace(filter["t"], filter["r"])

    #advanced operators
    # add exception for log that allows numbers right after
    for filter in [{"t": 'sin', "r": 'math.sin'}, {"t": 'cos', "r": 'math.cos'}, {"t": 'tan', "r": 'math.tan'},
                   {"t": 'asin', "r": 'math.asin'}, {"t": 'acos', "r": 'math.acos'}, {"t": 'atan', "r": 'math.atan'},
                   {"t": 'asinh', "r": 'math.asinh'}, {"t": 'acosh', "r": 'math.acosh'}, {"t": 'atanh', "r": 'math.atanh'}]:
        input = constantReplacer(input, filter["t"], filter["r"])

    #constants
    for filter in [{"t": 'π', "r": 'math.pi'}, {"t": 'e', "r": 'math.e'}, {"t": 'τ', "r": 'math.tau'}, {"t": 'φ', "r": '((1+math.sqrt(5))/2)'},
                   {"t": 'c', "r": '(2.99792458*10**8)'}, {"t": 'h', "r": '(6.62607015*10**-34)'}, {"t": 'G', "r": '(6.67430*10**-11)'},
                   {"t": 'g', "r": '(9.81)'}, {"t": 'k', "r": '(1.380649*10**-23)'}, {"t": 'Na', "r": '(6.02214076*10**23)'},
                   {"t": 'eV', "r": '(1.602176634*10**-19)'}]:
        input = constantReplacer(input, filter["t"], filter["r"])

    #stored variables
    for filter in [{"t": 'Ans', "r": f'({valAnsView})'},
                {'t': 'A', 'r': str(storeA[0])}, {'t': 'B', 'r': str(storeB[0])}, {'t': 'C', 'r': str(storeC[0])}, {'t': 'D', 'r': str(storeD[0])},
                {'t': 'E', 'r': str(storeE[0])}, {'t': 'F', 'r': str(storeF[0])}, {'t': 'G', 'r': str(storeG[0])}, {'t': 'H', 'r': str(storeH[0])},
                {'t': 'I', 'r': str(storeI[0])}, {'t': 'J', 'r': str(storeJ[0])}, {'t': 'K', 'r': str(storeK[0])}, {'t': 'L', 'r': str(storeL[0])},
                {'t': 'M', 'r': str(storeM[0])}, {'t': 'N', 'r': str(storeN[0])}, {'t': 'O', 'r': str(storeO[0])}, {'t': 'P', 'r': str(storeP[0])},
                {'t': 'Q', 'r': str(storeQ[0])}, {'t': 'R', 'r': str(storeR[0])}, {'t': 'S', 'r': str(storeS[0])}, {'t': 'T', 'r': str(storeT[0])},
                {'t': 'U', 'r': str(storeU[0])}, {'t': 'V', 'r': str(storeV[0])}, {'t': 'W', 'r': str(storeW[0])}, {'t': 'X', 'r': str(storeX[0])}, 
                {'t': 'Y', 'r': str(storeY[0])}, {'t': 'Z', 'r': str(storeZ[0])}]:
        input = input.replace(filter["t"], filter["r"])

    debugger(f"converted {savedInput} into {input}")
    return(input)

def actionCalculate(inputWindow):
    input = mathReplacer(inputWindow.get())
    try:
        n = 0
        outputMath = eval(input)
        output = float(eval(input))
        if abs(output) >= 10000000000:
            while abs(output) > 10:
                n = n+1
                output = output/10
            if not n > 99:
                output = str(output)[:10]
                outputValue = output+"×10^"+str(n)
                errorLog = None
            else:
                errorLog = "number out of range\ntoo large"
        elif abs(output) < 0.0001 and abs(output) > 0:
            while abs(output) < 1:
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
        returnVal = [outputValue, None]
        debugger(f'Calculation successful => Output: {returnVal[0]}')
    else:
        returnVal = ['', errorLog]
        debugger(f'Error in calculation => Error: {returnVal[1]}')
    return returnVal