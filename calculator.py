import math #NOTE: math is not directly used in the code, but it is used after replacing with the convertMath function
import tkinter
import tkinter.ttk
import tkinter.messagebox
import re

print('Calculator running')

def screenLoginDef():

    screenLogin = tkinter.Tk()
    screenLogin.title("Login")
    screenLogin.geometry("200x145+550+200")

    tkinter.ttk.Label(screenLogin, text="Username").place(x=10, y=10)
    usernameEntry = tkinter.Entry(screenLogin, width=29).place(x=10, y=35)
    usernameEntry.focus()

    tkinter.ttk.Label(screenLogin, text="Password").place(x=10, y=60)
    passwordEntry = tkinter.Entry(screenLogin, width=29, show="•").place(x=10, y=85)

    def loadUser(username, password):
        loginFound = False

        with open("accounts.json", 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            userNameLine = re.search(r'\s*"name": "(.*)".*', line)
            if userNameLine:
                compareName = userNameLine.group(1).strip()
                userKeyLine = re.search(r'\s*"password": "(.*)".*', lines[i+1])
                compareKey = userKeyLine.group(1).strip()
                if compareName == username and compareKey == password:
                    loginFound = True

        return loginFound
    
    def validateLogin():    
        attemptUsername = usernameEntry.get()
        attemptPassword = passwordEntry.get()

        if loadUser(attemptUsername, attemptPassword):
            tkinter.messagebox.showinfo(title="Beware", message="Calculator not fully operational, there may be bugs.")
            screenLogin.destroy()
            screenCalculatorDef()
        else:
            tkinter.messagebox.showerror(title="Error", message="Username and password did not match.")
            usernameEntry.delete("0", "end")
            passwordEntry.delete("0", "end")
    buttonLogin = tkinter.ttk.Button(screenLogin, text="Log in", command=validateLogin, width=10).place(x=120, y=110)

    def actionRegister():
        screenLogin.destroy()
        screenRegisterDef()
    buttonRegister = tkinter.ttk.Button(screenLogin, text="Register", command=actionRegister, width=10).place(x=10, y=110)

    screenLogin.mainloop()

def screenRegisterDef():

    screenRegister = tkinter.Tk()
    screenRegister.title("Register")
    screenRegister.geometry("200x195+550+200")

    tkinter.ttk.Label(screenRegister, text="Username").place(x=10, y=10)
    usernameEntry = tkinter.Entry(screenRegister, width=29).place(x=10, y=35)
    usernameEntry.focus()

    tkinter.ttk.Label(screenRegister, text="Password").place(x=10, y=60)
    passwordEntry1 = tkinter.Entry(screenRegister, width=29, show="•").place(x=10, y=85)

    labelPassword2 = tkinter.ttk.Label(screenRegister, text="Repeat Password").place(x=10, y=110)
    passwordEntry2 = tkinter.Entry(screenRegister, width=29, show="•").place(x=10, y=135)

    def saveUser(username, password):
        with open("accounts.json") as f:
            userData= f.read()
            userData = userData[0:-18]
            userData += '\n        },\n        {'
            userData += f'\n        "name": "{username}",\n        "password": "{password}"'
            userData += '\n        }\n    ]\n}'
            with open('accounts.json', 'w') as file:
                file.write(userData)

    def checkUserName(username):
        taken = False
        with open("accounts.json", 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            userNameLine = re.search(r'\s*"name": "(.*)".*', line)
            if userNameLine:
                compareName = userNameLine.group(1).strip()
                if compareName == username:
                    taken = True
        return taken
    
    def validateRegistry():
        attemptUsername = usernameEntry.get()
        attemptPassword1 = passwordEntry1.get()
        attemptPassword2 = passwordEntry2.get()
        if not attemptPassword1 == attemptPassword2:
            tkinter.messagebox.showerror(title="Error", message="Passwords are not identical.")
            usernameEntry.delete("0", "end")
            passwordEntry1.delete("0", "end")
            passwordEntry2.delete("0", "end")
            return
        if checkUserName(attemptUsername):
            tkinter.messagebox.showerror(title="Error", message="Username is already taken.")
            usernameEntry.delete("0", "end")
            passwordEntry1.delete("0", "end")
            passwordEntry2.delete("0", "end")
            return
        saveUser(attemptUsername, attemptPassword1)
        tkinter.messagebox.showinfo(title="Success", message="You have registered successfully.\nSending you back to the login screen.")
        screenRegister.destroy()
        screenLoginDef()
    buttonRegister = tkinter.ttk.Button(screenRegister, text="Register", command=validateRegistry, width=10).place(x=120, y=160)

def screenCalculatorDef():

    valAnsPrint = [0]; valAnsMath = [0]

    storeA = ['', '']; storeB = ['', '']; storeC = ['', '']; storeD = ['', '']; storeE = ['', '']; storeF = ['', '']; storeG = ['', '']
    storeH = ['', '']; storeI = ['', '']; storeJ = ['', '']; storeK = ['', '']; storeL = ['', '']; storeM = ['', '']; storeN = ['', '']
    storeO = ['', '']; storeP = ['', '']; storeQ = ['', '']; storeR = ['', '']; storeS = ['', '']; storeT = ['', '']; storeU = ['', '']
    storeV = ['', '']; storeW = ['', '']; storeX = ['', '']; storeY = ['', '']; storeZ = ['', '']

    screenCalculator = tkinter.Tk()
    screenCalculator.title("Calculator")
    screenCalculator.geometry("465x595+550+200")

    helperLines = False
    if helperLines:
        helperLinesHori = False
        helperLinesVert = True
        i = 1
        if helperLinesHori:
            while i <= 119:
                tkinter.ttk.Separator(screenCalculator, orient=tkinter.HORIZONTAL).place(x=0, y=i*5, height=5, width=465)
                i = i + 1
        if helperLinesVert:
            while i <= 93:
                tkinter.ttk.Separator(screenCalculator, orient=tkinter.VERTICAL).place(x=i*5, y=0, height=595, width=5)
                i = i + 1

    windowInputCalculator=tkinter.Entry(screenCalculator, width=29)
    windowInputCalculator.place(x=10, y=10)
    tkinter.ttk.Label(screenCalculator, text="Calculator by UltraPuPower1\ninspired by:\nCalculator by 刘键明", font=["Verdana", "9"]).place(x=200, y=8)
    tkinter.ttk.Label(screenCalculator, text="Answers might not be correct.\nUse at your own risk.\nV0.1", font=["Verdana", "7"]).place(x=0, y=550)
    tkinter.ttk.Separator(screenCalculator, orient=tkinter.VERTICAL).place(x=195, y=65, height=110, width=5)
    tkinter.ttk.Separator(screenCalculator, orient=tkinter.HORIZONTAL).place(x=0, y=175, height=5, width=195)
    tkinter.ttk.Separator(screenCalculator, orient=tkinter.HORIZONTAL).place(x=0, y=65, height=5, width=195)

    windowOutputCalculator=tkinter.ttk.Label(screenCalculator, text = "")
    windowOutputCalculator.place(x=10, y=30)

    def actionCalculatorClose():
        screenCalculator.destroy()
    buttonCalculatorClose=tkinter.ttk.Button(screenCalculator, text="Close", command=actionCalculatorClose, width=5).place(x=250, y=0)

    def getTextScreenCalculator():
        text = windowInputCalculator.get()
        return text
    
    def convertMath(inputString):
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

    def actionOne(): windowInputCalculator.insert("end","1")
    buttonOne=tkinter.ttk.Button(screenCalculator, text="1", command=actionOne, width=3).place(x=10, y=120)
    
    def actionTwo(): windowInputCalculator.insert("end","2")
    buttonTwo=tkinter.ttk.Button(screenCalculator, text="2", command=actionTwo, width=3).place(x=35, y=120)

    def actionThree(): windowInputCalculator.insert("end","3")
    buttonThree=tkinter.ttk.Button(screenCalculator, text="3", command=actionThree, width=3).place(x=60, y=120)

    def actionFour(): windowInputCalculator.insert("end","4")
    buttonFour=tkinter.ttk.Button(screenCalculator, text="4", command=actionFour, width=3).place(x=10, y=95)

    def actionFive(): windowInputCalculator.insert("end","5")
    buttonFive=tkinter.ttk.Button(screenCalculator, text="5", command=actionFive, width=3).place(x=35, y=95)

    def actionSix(): windowInputCalculator.insert("end","6")
    buttonSix=tkinter.ttk.Button(screenCalculator, text="6", command=actionSix, width=3).place(x=60, y=95)

    def actionSeven(): windowInputCalculator.insert("end","7")
    buttonSeven=tkinter.ttk.Button(screenCalculator, text="7", command=actionSeven, width=3).place(x=10, y=70)

    def actionEight(): windowInputCalculator.insert("end","8")
    buttonEight=tkinter.ttk.Button(screenCalculator, text="8", command=actionEight, width=3).place(x=35, y=70)

    def actionNine(): windowInputCalculator.insert("end","9")
    buttonNine=tkinter.ttk.Button(screenCalculator, text="9", command=actionNine, width=3).place(x=60, y=70)

    def actionZero(): windowInputCalculator.insert("end","0")
    buttonZero=tkinter.ttk.Button(screenCalculator, text="0", command=actionZero, width=7).place(x=10, y=145)

    def actionAdd(): windowInputCalculator.insert("end","+")
    buttonAdd = tkinter.ttk.Button(screenCalculator, text="+", command=actionAdd, width=3).place(x=85, y=120)

    def actionSubtract(): windowInputCalculator.insert("end","-")
    buttonSubtract = tkinter.ttk.Button(screenCalculator, text="-", command=actionSubtract, width=3).place(x=110, y=120)

    def actionMultiply(): windowInputCalculator.insert("end","*")
    buttonMultiply = tkinter.ttk.Button(screenCalculator, text="*", command=actionMultiply, width=3).place(x=85, y=95)

    def actionDivide(): windowInputCalculator.insert("end","/")
    buttonDivide = tkinter.ttk.Button(screenCalculator, text="/", command=actionDivide, width=3).place(x=110, y=95)

    def actionClear(): windowInputCalculator.delete("0", "end"); windowOutputCalculator.config(text = "")
    buttonClear=tkinter.ttk.Button(screenCalculator, text="C", command=actionClear, width=3).place(x=85, y=70)

    def actionDot(): windowInputCalculator.insert("end", ".")
    buttonDot=tkinter.ttk.Button(screenCalculator, text=".", command=actionDot, width=3).place(x=60, y=145)

    def actionOpenParenthesis(): windowInputCalculator.insert("end", "(")
    buttonOpenParenthesis=tkinter.ttk.Button(screenCalculator, text="(", command=actionOpenParenthesis, width=3).place(x=135, y=70)

    def actionCloseParenthesis(): windowInputCalculator.insert("end", ")")
    buttonCloseParenthesis=tkinter.ttk.Button(screenCalculator, text=")", command=actionCloseParenthesis, width=3).place(x=160, y=70)

    def actionPower(): windowInputCalculator.insert("end", "^")
    buttonPower=tkinter.ttk.Button(screenCalculator, text="^", command=actionPower, width=3).place(x=135, y=95)

    def actionLog(): windowInputCalculator.insert("end", "log10(")
    buttonLog=tkinter.ttk.Button(screenCalculator, text="log", command=actionLog, width=3).place(x=160, y=95)

    def actionSine(): windowInputCalculator.insert("end", "sin(")
    buttonSine=tkinter.ttk.Button(screenCalculator, text="sin", command=actionSine, width=3).place(x=135, y=120)

    def actionCosine(): windowInputCalculator.insert("end", "cos(")
    buttonCosine=tkinter.ttk.Button(screenCalculator, text="cos", command=actionCosine, width=3).place(x=160, y=120)

    def actionTangent(): windowInputCalculator.insert("end", "tan(")
    buttonTangent=tkinter.ttk.Button(screenCalculator, text="tan", command=actionTangent, width=3).place(x=160, y=145)
    
    def actionBackspace():
        inhoud_windowInputCalculator = windowInputCalculator.get()
        inhoud_windowInputCalculator = inhoud_windowInputCalculator[:-1]
        windowInputCalculator.delete("0", "end")
        windowInputCalculator.insert("end", inhoud_windowInputCalculator)
        windowOutputCalculator.config(text = "")
    buttonBackspace=tkinter.ttk.Button(screenCalculator, text="del", command=actionBackspace, width=3).place(x=110, y=70)

    def storeAns(valPrint, valMath):
        valAnsPrint.clear()
        valAnsPrint.insert(0, valPrint)
        valAnsMath.clear()
        valAnsMath.insert(1, valMath)

    def actionCalculate():
        input = convertMath(getTextScreenCalculator())
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

    def actionDisplayCalculation():
        result = actionCalculate()
        outputValue = result[0]
        outputMath = result[1]
        errorLog = result[2]
        if errorLog == None:
            print("printing output")
            windowOutputCalculator.config(text = "")
            windowOutputCalculator.config(text = "= "+str(outputValue))
            storeAns(outputValue, outputMath)
        else:
            print("printing error")
            windowOutputCalculator.config(text = "")
            tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            storeAns('', '')
    buttonCalculate=tkinter.ttk.Button(screenCalculator, text="=", command=actionDisplayCalculation, width=7).place(x=85, y=145)

    def actionAns(): windowInputCalculator.insert("end", "Ans")
    buttonAns=tkinter.ttk.Button(screenCalculator, text="ans", command=actionAns, width=3).place(x=135, y=145)

    def screenVariablesDef():
        screenVariables = tkinter.Tk()
        screenVariables.title("Variables")
        screenVariables.geometry("250x665+1065+200")

        def actionScreenVariablesExit():
            screenVariables.destroy()
        buttonScreenVariablesExit=tkinter.ttk.Button(screenVariables, text="Exit", command=actionScreenVariablesExit, width=5).place(x=200, y=0)

        textShowA = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowA.place(x=85, y=15)
        def actionStoreA():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeA.clear()
            if errorLog == None:
                storeA.insert(0, outputValue); storeA.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowA.config(text = ""); textShowA.config(text = "= "+str(storeA[0]))
        buttonStoreA=tkinter.ttk.Button(screenVariables, text="Ans=A", command=actionStoreA, width=7).place(x=10, y=10)
        def actionTypeA():windowInputCalculator.insert("end", "A")
        buttonTypeA=tkinter.ttk.Button(screenVariables, text="A", command=actionTypeA, width=2).place(x=60, y=10)

        textShowB = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowB.place(x=85, y=40)
        def actionStoreB():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeB.clear()
            if errorLog == None:
                storeB.insert(0, outputValue); storeB.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowB.config(text = ""); textShowB.config(text = "= "+str(storeB[0]))
        buttonStoreB=tkinter.ttk.Button(screenVariables, text="Ans=B", command=actionStoreB, width=7).place(x=10, y=35)
        def actionTypeB():windowInputCalculator.insert("end", "B")
        buttonTypeB=tkinter.ttk.Button(screenVariables, text="B", command=actionTypeB, width=2).place(x=60, y=35)

        textShowC = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowC.place(x=85, y=65)
        def actionStoreC():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeC.clear()
            if errorLog == None:
                storeC.insert(0, outputValue); storeC.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowC.config(text = ""); textShowC.config(text = "= "+str(storeC[0]))
        buttonStoreC=tkinter.ttk.Button(screenVariables, text="Ans=C", command=actionStoreC, width=7).place(x=10, y=60)
        def actionTypeC():windowInputCalculator.insert("end", "C")
        buttonTypeC=tkinter.ttk.Button(screenVariables, text="C", command=actionTypeC, width=2).place(x=60, y=60)

        textShowD = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowD.place(x=85, y=90)
        def actionStoreD():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeD.clear()
            if errorLog == None:
                storeD.insert(0, outputValue); storeD.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowD.config(text = ""); textShowD.config(text = "= "+str(storeD[0]))
        buttonStoreD=tkinter.ttk.Button(screenVariables, text="Ans=D", command=actionStoreD, width=7).place(x=10, y=85)
        def actionTypeD():windowInputCalculator.insert("end", "D")
        buttonTypeD=tkinter.ttk.Button(screenVariables, text="D", command=actionTypeD, width=2).place(x=60, y=85)

        textShowE = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowE.place(x=85, y=115)
        def actionStoreE():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeE.clear()
            if errorLog == None:
                storeE.insert(0, outputValue); storeE.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowE.config(text = ""); textShowE.config(text = "= "+str(storeE[0]))
        buttonStoreE=tkinter.ttk.Button(screenVariables, text="Ans=E", command=actionStoreE, width=7).place(x=10, y=110)
        def actionTypeE():windowInputCalculator.insert("end", "E")
        buttonTypeE=tkinter.ttk.Button(screenVariables, text="E", command=actionTypeE, width=2).place(x=60, y=110)

        textShowF = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowF.place(x=85, y=140)
        def actionStoreF():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeF.clear()
            if errorLog == None:
                storeF.insert(0, outputValue); storeF.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowF.config(text = ""); textShowF.config(text = "= "+str(storeF[0]))
        buttonStoreF=tkinter.ttk.Button(screenVariables, text="Ans=F", command=actionStoreF, width=7).place(x=10, y=135)
        def actionTypeF():windowInputCalculator.insert("end", "F")
        buttonTypeF=tkinter.ttk.Button(screenVariables, text="F", command=actionTypeF, width=2).place(x=60, y=135)

        textShowG = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowG.place(x=85, y=165)
        def actionStoreG():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeG.clear()
            if errorLog == None:
                storeG.insert(0, outputValue); storeG.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowG.config(text = ""); textShowG.config(text = "= "+str(storeG[0]))
        buttonStoreG=tkinter.ttk.Button(screenVariables, text="Ans=G", command=actionStoreG, width=7).place(x=10, y=160)
        def actionTypeG():windowInputCalculator.insert("end", "G")
        buttonTypeG=tkinter.ttk.Button(screenVariables, text="G", command=actionTypeG, width=2).place(x=60, y=160)

        textShowH = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowH.place(x=85, y=190)
        def actionStoreH():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeH.clear()
            if errorLog == None:
                storeH.insert(0, outputValue); storeH.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowH.config(text = ""); textShowH.config(text = "= "+str(storeH[0]))
        buttonStoreH=tkinter.ttk.Button(screenVariables, text="Ans=H", command=actionStoreH, width=7).place(x=10, y=185)
        def actionTypeH():windowInputCalculator.insert("end", "H")
        buttonTypeH=tkinter.ttk.Button(screenVariables, text="H", command=actionTypeH, width=2).place(x=60, y=185)

        textShowI = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowI.place(x=85, y=215)
        def actionStoreI():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeI.clear()
            if errorLog == None:
                storeI.insert(0, outputValue); storeI.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowI.config(text = ""); textShowI.config(text = "= "+str(storeI[0]))
        buttonStoreI=tkinter.ttk.Button(screenVariables, text="Ans=I", command=actionStoreI, width=7).place(x=10, y=210)
        def actionTypeI():windowInputCalculator.insert("end", "I")
        buttonTypeI=tkinter.ttk.Button(screenVariables, text="I", command=actionTypeI, width=2).place(x=60, y=210)

        textShowJ = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowJ.place(x=85, y=240)
        def actionStoreJ():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeJ.clear()
            if errorLog == None:
                storeJ.insert(0, outputValue); storeJ.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowJ.config(text = ""); textShowJ.config(text = "= "+str(storeJ[0]))
        buttonStoreJ=tkinter.ttk.Button(screenVariables, text="Ans=J", command=actionStoreJ, width=7).place(x=10, y=235)
        def actionTypeJ():windowInputCalculator.insert("end", "J")
        buttonTypeJ=tkinter.ttk.Button(screenVariables, text="J", command=actionTypeJ, width=2).place(x=60, y=235)

        textShowK = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowK.place(x=85, y=265)
        def actionStoreK():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeK.clear()
            if errorLog == None:
                storeK.insert(0, outputValue); storeK.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowK.config(text = ""); textShowK.config(text = "= "+str(storeK[0]))
        buttonStoreK=tkinter.ttk.Button(screenVariables, text="Ans=K", command=actionStoreK, width=7).place(x=10, y=260)
        def actionTypeK():windowInputCalculator.insert("end", "K")
        buttonTypeK=tkinter.ttk.Button(screenVariables, text="K", command=actionTypeK, width=2).place(x=60, y=260)

        textShowL = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowL.place(x=85, y=290)
        def actionStoreL():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeL.clear()
            if errorLog == None:
                storeL.insert(0, outputValue); storeL.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowL.config(text = ""); textShowL.config(text = "= "+str(storeL[0]))
        buttonStoreL=tkinter.ttk.Button(screenVariables, text="Ans=L", command=actionStoreL, width=7).place(x=10, y=285)
        def actionTypeL():windowInputCalculator.insert("end", "L")
        buttonTypeL=tkinter.ttk.Button(screenVariables, text="L", command=actionTypeL, width=2).place(x=60, y=285)

        textShowM = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowM.place(x=85, y=315)
        def actionStoreM():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeM.clear()
            if errorLog == None:
                storeM.insert(0, outputValue); storeM.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowM.config(text = ""); textShowM.config(text = "= "+str(storeM[0]))
        buttonStoreM=tkinter.ttk.Button(screenVariables, text="Ans=M", command=actionStoreM, width=7).place(x=10, y=310)
        def actionTypeM():windowInputCalculator.insert("end", "M")
        buttonTypeM=tkinter.ttk.Button(screenVariables, text="M", command=actionTypeM, width=2).place(x=60, y=310)

        textShowN = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowN.place(x=85, y=340)
        def actionStoreN():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeN.clear()
            if errorLog == None:
                storeN.insert(0, outputValue); storeN.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowN.config(text = ""); textShowN.config(text = "= "+str(storeN[0]))
        buttonStoreN=tkinter.ttk.Button(screenVariables, text="Ans=N", command=actionStoreN, width=7).place(x=10, y=335)
        def actionTypeN():windowInputCalculator.insert("end", "N")
        buttonTypeN=tkinter.ttk.Button(screenVariables, text="N", command=actionTypeN, width=2).place(x=60, y=335)

        textShowO = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowO.place(x=85, y=365)
        def actionStoreO():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeO.clear()
            if errorLog == None:
                storeO.insert(0, outputValue); storeO.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowO.config(text = ""); textShowO.config(text = "= "+str(storeO[0]))
        buttonStoreO=tkinter.ttk.Button(screenVariables, text="Ans=O", command=actionStoreO, width=7).place(x=10, y=360)
        def actionTypeO():windowInputCalculator.insert("end", "O")
        buttonTypeO=tkinter.ttk.Button(screenVariables, text="O", command=actionTypeO, width=2).place(x=60, y=360)

        textShowP = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowP.place(x=85, y=390)
        def actionStoreP():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeP.clear()
            if errorLog == None:
                storeP.insert(0, outputValue); storeP.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowP.config(text = ""); textShowP.config(text = "= "+str(storeP[0]))
        buttonStoreP=tkinter.ttk.Button(screenVariables, text="Ans=P", command=actionStoreP, width=7).place(x=10, y=385)
        def actionTypeP():windowInputCalculator.insert("end", "P")
        buttonTypeP=tkinter.ttk.Button(screenVariables, text="P", command=actionTypeP, width=2).place(x=60, y=385)

        textShowQ = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowQ.place(x=85, y=415)
        def actionStoreQ():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeQ.clear()
            if errorLog == None:
                storeQ.insert(0, outputValue); storeQ.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowQ.config(text = ""); textShowQ.config(text = "= "+str(storeQ[0]))
        buttonStoreQ=tkinter.ttk.Button(screenVariables, text="Ans=Q", command=actionStoreQ, width=7).place(x=10, y=410)
        def actionTypeQ():windowInputCalculator.insert("end", "Q")
        buttonTypeQ=tkinter.ttk.Button(screenVariables, text="Q", command=actionTypeQ, width=2).place(x=60, y=410)

        textShowR = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowR.place(x=85, y=440)
        def actionStoreR():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeR.clear()
            if errorLog == None:
                storeR.insert(0, outputValue); storeR.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowR.config(text = ""); textShowR.config(text = "= "+str(storeR[0]))
        buttonStoreR=tkinter.ttk.Button(screenVariables, text="Ans=R", command=actionStoreR, width=7).place(x=10, y=435)
        def actionTypeR():windowInputCalculator.insert("end", "R")
        buttonTypeR=tkinter.ttk.Button(screenVariables, text="R", command=actionTypeR, width=2).place(x=60, y=435)

        textShowS = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowS.place(x=85, y=465)
        def actionStoreS():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeS.clear()
            if errorLog == None:
                storeS.insert(0, outputValue); storeS.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowS.config(text = ""); textShowS.config(text = "= "+str(storeS[0]))
        buttonStoreS=tkinter.ttk.Button(screenVariables, text="Ans=S", command=actionStoreS, width=7).place(x=10, y=460)
        def actionTypeS():windowInputCalculator.insert("end", "S")
        buttonTypeS=tkinter.ttk.Button(screenVariables, text="S", command=actionTypeS, width=2).place(x=60, y=460)

        textShowT = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowT.place(x=85, y=490)
        def actionStoreT():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeT.clear()
            if errorLog == None:
                storeT.insert(0, outputValue); storeT.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowT.config(text = ""); textShowT.config(text = "= "+str(storeT[0]))
        buttonStoreT=tkinter.ttk.Button(screenVariables, text="Ans=T", command=actionStoreT, width=7).place(x=10, y=485)
        def actionTypeT():windowInputCalculator.insert("end", "T")
        buttonTypeT=tkinter.ttk.Button(screenVariables, text="T", command=actionTypeT, width=2).place(x=60, y=485)

        textShowU = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowU.place(x=85, y=515)
        def actionStoreU():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeU.clear()
            if errorLog == None:
                storeU.insert(0, outputValue); storeU.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowU.config(text = ""); textShowU.config(text = "= "+str(storeU[0]))
        buttonStoreU=tkinter.ttk.Button(screenVariables, text="Ans=U", command=actionStoreU, width=7).place(x=10, y=510)
        def actionTypeU():windowInputCalculator.insert("end", "U")
        buttonTypeU=tkinter.ttk.Button(screenVariables, text="U", command=actionTypeU, width=2).place(x=60, y=510)

        textShowV = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowV.place(x=85, y=540)
        def actionStoreV():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeV.clear()
            if errorLog == None:
                storeV.insert(0, outputValue); storeV.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowV.config(text = ""); textShowV.config(text = "= "+str(storeV[0]))
        buttonStoreV=tkinter.ttk.Button(screenVariables, text="Ans=V", command=actionStoreV, width=7).place(x=10, y=535)
        def actionTypeV():windowInputCalculator.insert("end", "V")
        buttonTypeV=tkinter.ttk.Button(screenVariables, text="V", command=actionTypeV, width=2).place(x=60, y=535)

        textShowW = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowW.place(x=85, y=565)
        def actionStoreW():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeW.clear()
            if errorLog == None:
                storeW.insert(0, outputValue); storeW.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowW.config(text = ""); textShowW.config(text = "= "+str(storeW[0]))
        buttonStoreW=tkinter.ttk.Button(screenVariables, text="Ans=W", command=actionStoreW, width=7).place(x=10, y=560)
        def actionTypeW():windowInputCalculator.insert("end", "W")
        buttonTypeW=tkinter.ttk.Button(screenVariables, text="W", command=actionTypeW, width=2).place(x=60, y=560)

        textShowX = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowX.place(x=85, y=590)
        def actionStoreX():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeX.clear()
            if errorLog == None:
                storeX.insert(0, outputValue); storeX.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowX.config(text = ""); textShowX.config(text = "= "+str(storeX[0]))
        buttonStoreX=tkinter.ttk.Button(screenVariables, text="Ans=X", command=actionStoreX, width=7).place(x=10, y=585)
        def actionTypeX():windowInputCalculator.insert("end", "X")
        buttonTypeX=tkinter.ttk.Button(screenVariables, text="X", command=actionTypeX, width=2).place(x=60, y=585)

        textShowY = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowY.place(x=85, y=615)
        def actionStoreY():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeY.clear()
            if errorLog == None:
                storeY.insert(0, outputValue); storeY.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowY.config(text = ""); textShowY.config(text = "= "+str(storeY[0]))
        buttonStoreY=tkinter.ttk.Button(screenVariables, text="Ans=Y", command=actionStoreY, width=7).place(x=10, y=610)
        def actionTypeY():windowInputCalculator.insert("end", "Y")
        buttonTypeY=tkinter.ttk.Button(screenVariables, text="Y", command=actionTypeY, width=2).place(x=60, y=610)

        textShowZ = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
        textShowZ.place(x=85, y=640)
        def actionStoreZ():
            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeZ.clear()
            if errorLog == None:
                storeZ.insert(0, outputValue); storeZ.insert(1, outputMath)
            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowZ.config(text = ""); textShowZ.config(text = "= "+str(storeZ[0]))
        buttonStoreZ=tkinter.ttk.Button(screenVariables, text="Ans=Z", command=actionStoreZ, width=7).place(x=10, y=635)
        def actionTypeZ():windowInputCalculator.insert("end", "Z")
        buttonTypeZ=tkinter.ttk.Button(screenVariables, text="Z", command=actionTypeZ, width=2).place(x=60, y=635)
        screenVariables.mainloop()
    buttonVariables=tkinter.ttk.Button(screenCalculator, text="Variables", command=screenVariablesDef, width=15).place(x=200, y=70)
    
    def screenFunctionsDef():
        screenFunctions = tkinter.Tk()
        screenFunctions.title("Functions")
        screenFunctions.geometry("300x665+150+200")

        tkinter.ttk.Label(screenFunctions, text="Mathematical functions").place(x=5, y=5)
        def actionScreenFunctionsExit():
            screenFunctions.destroy()
        buttonScreenFunctionsExit=tkinter.ttk.Button(screenFunctions, text="Exit", command=actionScreenFunctionsExit, width=5).place(x=250, y=0)

        def actionSquareroot(): windowInputCalculator.insert("end", "√(")
        buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="√", command=actionSquareroot, width=3).place(x=5, y=20)

        screenFunctions.mainloop()
    buttonFunctions=tkinter.ttk.Button(screenCalculator, text="Functions", command=screenFunctionsDef, width=15).place(x=200, y=95)
    
    def screenConstantsDef():

        def actionPhysicsWarning():
            tkinter.messagebox.showinfo(title="Beware", message="Physics constants use unconventional symbols.\nThis means that you won't be able to type them with your keyboard.\nYou can use the buttons to insert them into the calculator.")
        actionPhysicsWarning()

        screenConstants = tkinter.Tk()
        screenConstants.title("Constants")
        screenConstants.geometry("300x665+1365+200")

        buttonPhysicsWarning=tkinter.ttk.Button(screenConstants, text="?", command=actionPhysicsWarning, width=1).place(x=105, y=45)

        tkinter.ttk.Label(screenConstants, text="Mathematical constants").place(x=5, y=5)
        def actionScreenConstantsExit():
            screenConstants.destroy()
        buttonScreenConstantsExit=tkinter.ttk.Button(screenConstants, text="Exit", command=actionScreenConstantsExit, width=5).place(x=250, y=0)

        def actionPi(): windowInputCalculator.insert("end", "π")
        buttonPi=tkinter.ttk.Button(screenConstants, text="π", command=actionPi, width=3).place(x=5, y=20)

        def actionEuler(): windowInputCalculator.insert("end", "e")
        buttonEuler=tkinter.ttk.Button(screenConstants, text="e", command=actionEuler, width=3).place(x=35, y=20)

        def actionTau(): windowInputCalculator.insert("end", "τ")
        buttonTau=tkinter.ttk.Button(screenConstants, text="τ", command=actionTau, width=3).place(x=65, y=20)

        def actionPhi(): windowInputCalculator.insert("end", "φ")
        buttonPhi=tkinter.ttk.Button(screenConstants, text="φ", command=actionPhi, width=3).place(x=95, y=20)

        tkinter.ttk.Label(screenConstants, text="Physics constants").place(x=5, y=45)

        def actionLight(): windowInputCalculator.insert("end", "ϲ")
        buttonLight=tkinter.ttk.Button(screenConstants, text="ϲ", command=actionLight, width=3).place(x=5, y=65)
        tkinter.ttk.Label(screenConstants, text="Speed of Light").place(x=30, y=70)

        def actionPlanck(): windowInputCalculator.insert("end", "Ꮒ")
        buttonPlanck=tkinter.ttk.Button(screenConstants, text="Ꮒ", command=actionPlanck, width=3).place(x=5, y=90)
        tkinter.ttk.Label(screenConstants, text="Planck Constant").place(x=30, y=95)

        def actionGravityConst(): windowInputCalculator.insert("end", "Ꮐ")
        buttonGravityConst=tkinter.ttk.Button(screenConstants, text="Ꮐ", command=actionGravityConst, width=3).place(x=5, y=115)
        tkinter.ttk.Label(screenConstants, text="Gravitation Constant").place(x=30, y=120)

        def actionGravity(): windowInputCalculator.insert("end", "ց")
        buttonGravity=tkinter.ttk.Button(screenConstants, text="ց", command=actionGravity, width=3).place(x=5, y=140)
        tkinter.ttk.Label(screenConstants, text="Gravitational Acceleration (NL)").place(x=30, y=145)

        def actionBoltzmann(): windowInputCalculator.insert("end", "k")
        buttonBoltzmann=tkinter.ttk.Button(screenConstants, text="k", command=actionBoltzmann, width=3).place(x=5, y=165)
        tkinter.ttk.Label(screenConstants, text="Boltzmann Constant").place(x=30, y=170)

        def actionAvogadro(): windowInputCalculator.insert("end", "Ｎ")
        buttonAvogadro=tkinter.ttk.Button(screenConstants, text="Ｎ", command=actionAvogadro, width=3).place(x=5, y=190)
        tkinter.ttk.Label(screenConstants, text="Avogadro Constant").place(x=30, y=195)

        def actionElementalChargeQuantum(): windowInputCalculator.insert("end", "ҽ")
        buttonElementalChargeQuantum=tkinter.ttk.Button(screenConstants, text="ҽ", command=actionElementalChargeQuantum, width=3).place(x=5, y=215)
        tkinter.ttk.Label(screenConstants, text="Elementary Charge").place(x=30, y=220)

        screenConstants.mainloop()
    buttonConstants=tkinter.ttk.Button(screenCalculator, text="Constants", command=screenConstantsDef, width=15).place(x=200, y=120)
    
    screenCalculator.mainloop()

screenCalculatorDef()