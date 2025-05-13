import math #NOTE: math is not directly used in the code, but it is used after replacing with the convertMath function

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