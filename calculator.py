import math #NOTE: math is not directly used in the code, but it is used after replacing with the convertMath function
import tkinter
import tkinter.ttk
import tkinter.messagebox
import re

print('Calculator running')

users = [
    {'userName': 'Admin', 'userPassword': 'P@$$w0rd'},
    {'userName': 'User1', 'userPassword': 'password'}
]


def saveUser(username, password):
    with open("accounts.json") as f:
        userData= f.read()
        userData = userData[0:-18]
        userData += '\n        },\n        {'
        userData += f'\n        "name": "{username}",\n        "password": "{password}"'
        userData += '\n        }\n    ]\n}'
        with open('accounts.json', 'w') as file:
            file.write(userData)

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

def screenLoginDef():

    screenLogin = tkinter.Tk()
    screenLogin.title("Login")
    screenLogin.geometry("200x145+550+200")

    labelUsername = tkinter.ttk.Label(screenLogin, text="Username").place(x=10, y=10)
    usernameEntry = tkinter.Entry(screenLogin, width=29)
    usernameEntry.place(x=10, y=35)
    usernameEntry.focus()

    labelPassword = tkinter.ttk.Label(screenLogin, text="Password").place(x=10, y=60)
    passwordEntry = tkinter.Entry(screenLogin, width=29, show="•")
    passwordEntry.place(x=10, y=85)
    
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

def screenRegisterDef():

    screenRegister = tkinter.Tk()
    screenRegister.title("Register")
    screenRegister.geometry("200x195+550+200")

    labelUsername = tkinter.ttk.Label(screenRegister, text="Username").place(x=10, y=10)
    usernameEntry = tkinter.Entry(screenRegister, width=29)
    usernameEntry.place(x=10, y=35)
    usernameEntry.focus()

    labelPassword1 = tkinter.ttk.Label(screenRegister, text="Password").place(x=10, y=60)
    passwordEntry1 = tkinter.Entry(screenRegister, width=29, show="•")
    passwordEntry1.place(x=10, y=85)

    labelPassword2 = tkinter.ttk.Label(screenRegister, text="Repeat Password").place(x=10, y=110)
    passwordEntry2 = tkinter.Entry(screenRegister, width=29, show="•")
    passwordEntry2.place(x=10, y=135)
    
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
        for user in users:
            if attemptUsername == user['userName']:
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

    A = [0, 0]; B = [0, 0]; C = [0, 0]; D = [0, 0]; E = [0, 0]; F = [0, 0]; G = [0, 0]
    H = [0, 0]; I = [0, 0]; J = [0, 0]; K = [0, 0]; L = [0, 0]; M = [0, 0]; N = [0, 0]
    O = [0, 0]; P = [0, 0]; Q = [0, 0]; R = [0, 0]; S = [0, 0]; T = [0, 0]; U = [0, 0]
    V = [0, 0]; W = [0, 0]; X = [0, 0]; Y = [0, 0]; Z = [0, 0]

    screenCalculator = tkinter.Tk()
    screenCalculator.title("Calculator")
    screenCalculator.geometry("465x595+550+200")
    windowInputCalculator=tkinter.Entry(screenCalculator, width=29)
    windowInputCalculator.place(x=10, y=10)
    tkinter.ttk.Label(screenCalculator, text="Calculator by UltraPuPower1\ninspired by:\nCalculator by 刘键明", font=["Verdana", "9"]).place(x=200, y=8)
    tkinter.ttk.Label(screenCalculator, text="Answers might not be correct.\nUse at your own risk.\nV0.1", font=["Verdana", "7"]).place(x=0, y=550)
    tkinter.ttk.Separator(screenCalculator, orient=tkinter.VERTICAL).place(x=195, y=65, height=110, width=5)
    tkinter.ttk.Separator(screenCalculator, orient=tkinter.HORIZONTAL).place(x=0, y=175, height=5, width=195)
    tkinter.ttk.Separator(screenCalculator, orient=tkinter.HORIZONTAL).place(x=0, y=65, height=5, width=195)

    windowOutputCalculator=tkinter.ttk.Label(screenCalculator, text = "")
    windowOutputCalculator.place(x=10, y=30)

    def getTextScreenCalculator():
        text = windowInputCalculator.get()
        return text
    
    def convertMath(inputString):
        text = f'Converted {inputString} to '
        
        for code in [{'mesh': 'log','new': 'math.log'}, {'mesh': 'sin', 'new': 'math.sin'}, {'mesh': 'cos', 'new': 'math.cos'}, {'mesh': 'tan', 'new': 'math.tan'},
                    {'mesh': '^', 'new': '**'}, {'mesh': '×10^', 'new': '*10**'}, {'mesh': 'Ans', 'new': f'{valAnsMath[0]}'}]:
            inputString = inputString.replace(code['mesh'], code['new'])

        for code in [{'mesh': 'A', 'new': str(A[1])}, {'mesh': 'B', 'new': str(B[1])}, {'mesh': 'C', 'new': str(C[1])}, {'mesh': 'D', 'new': str(D[1])},
                     {'mesh': 'E', 'new': str(E[1])}, {'mesh': 'F', 'new': str(F[1])}, {'mesh': 'G', 'new': str(G[1])}, {'mesh': 'H', 'new': str(H[1])},
                     {'mesh': 'I', 'new': str(I[1])}, {'mesh': 'J', 'new': str(J[1])}, {'mesh': 'K', 'new': str(K[1])}, {'mesh': 'L', 'new': str(L[1])},
                     {'mesh': 'M', 'new': str(M[1])}, {'mesh': 'N', 'new': str(N[1])}, {'mesh': 'O', 'new': str(O[1])}, {'mesh': 'P', 'new': str(P[1])},
                     {'mesh': 'Q', 'new': str(Q[1])}, {'mesh': 'R', 'new': str(R[1])}, {'mesh': 'S', 'new': str(S[1])}, {'mesh': 'T', 'new': str(T[1])},
                     {'mesh': 'U', 'new': str(U[1])}, {'mesh': 'V', 'new': str(V[1])}, {'mesh': 'W', 'new': str(W[1])}, {'mesh': 'X', 'new': str(X[1])}, 
                     {'mesh': 'Y', 'new': str(Y[1])}, {'mesh': 'Z', 'new': str(Z[1])}]:
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
            returnVal = [0, 0, errorLog]
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
            storeAns(0, 0)
    buttonCalculate=tkinter.ttk.Button(screenCalculator, text="=", command=actionDisplayCalculation, width=7).place(x=85, y=145)

    def actionAns(): windowInputCalculator.insert("end", "Ans")
    buttonAns=tkinter.ttk.Button(screenCalculator, text="ans", command=actionAns, width=3).place(x=135, y=145)

    def storeVarGenerator(varSymbol):
        def storeVar():
            result = actionCalculate()
            outputValue = result[0]
            outputMath = result[1]
            errorLog = result[2]
            varSymbol.clear()
            if errorLog == None:
                varSymbol.insert(0, outputValue)
                varSymbol.insert(1, outputMath)
            else:
                tkinter.messagebox.showerror(title="Error", message=str(errorLog))
            textShowA.config(text = "")
            textShowA.config(text = "A = "+str(A[0]))
        return storeVar

    textShowA = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowA.place(x=85, y=215)
    def actionStoreA(): storeVarGenerator(A)()
    buttonStoreA=tkinter.ttk.Button(screenCalculator, text="Ans=A", command=actionStoreA, width=7).place(x=10, y=210)
    def actionTypeA():windowInputCalculator.insert("end", "A")
    buttonTypeA=tkinter.ttk.Button(screenCalculator, text="A", command=actionTypeA, width=2).place(x=60, y=210)

    textShowB = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowB.place(x=85, y=240)
    def actionStoreB(): storeVarGenerator(B)()
    buttonStoreB=tkinter.ttk.Button(screenCalculator, text="Ans=B", command=actionStoreB, width=7).place(x=10, y=235)
    def actionTypeB():windowInputCalculator.insert("end", "B")
    buttonTypeB=tkinter.ttk.Button(screenCalculator, text="B", command=actionTypeB, width=2).place(x=60, y=235)
    
    textShowC = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowC.place(x=85, y=265)
    def actionStoreC(): storeVarGenerator(C)()
    buttonStoreC=tkinter.ttk.Button(screenCalculator, text="Ans=C", command=actionStoreC, width=7).place(x=10, y=260)
    def actionTypeC():windowInputCalculator.insert("end", "C")
    buttonTypeC=tkinter.ttk.Button(screenCalculator, text="C", command=actionTypeC, width=2).place(x=60, y=260)

    textShowD = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowD.place(x=85, y=290)
    def actionStoreD(): storeVarGenerator(D)()
    buttonStoreD=tkinter.ttk.Button(screenCalculator, text="Ans=D", command=actionStoreD, width=7).place(x=10, y=285)
    def actionTypeD():windowInputCalculator.insert("end", "D")
    buttonTypeD=tkinter.ttk.Button(screenCalculator, text="D", command=actionTypeD, width=2).place(x=60, y=285)

    textShowE = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowE.place(x=85, y=315)
    def actionStoreE(): storeVarGenerator(E)()
    buttonStoreE=tkinter.ttk.Button(screenCalculator, text="Ans=E", command=actionStoreE, width=7).place(x=10, y=310)
    def actionTypeE():windowInputCalculator.insert("end", "E")
    buttonTypeE=tkinter.ttk.Button(screenCalculator, text="E", command=actionTypeE, width=2).place(x=60, y=310)

    textShowF = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowF.place(x=85, y=340)
    def actionStoreF(): storeVarGenerator(F)()
    buttonStoreF=tkinter.ttk.Button(screenCalculator, text="Ans=F", command=actionStoreF, width=7).place(x=10, y=335)
    def actionTypeF():windowInputCalculator.insert("end", "F")
    buttonTypeF=tkinter.ttk.Button(screenCalculator, text="F", command=actionTypeF, width=2).place(x=60, y=335)

    textShowG = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowG.place(x=85, y=365)
    def actionStoreG(): storeVarGenerator(G)()
    buttonStoreG=tkinter.ttk.Button(screenCalculator, text="Ans=G", command=actionStoreG, width=7).place(x=10, y=360)
    def actionTypeG():windowInputCalculator.insert("end", "G")
    buttonTypeG=tkinter.ttk.Button(screenCalculator, text="G", command=actionTypeG, width=2).place(x=60, y=360)

    textShowH = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowH.place(x=85, y=390)
    def actionStoreH(): storeVarGenerator(H)()
    buttonStoreH=tkinter.ttk.Button(screenCalculator, text="Ans=H", command=actionStoreH, width=7).place(x=10, y=385)
    def actionTypeH():windowInputCalculator.insert("end", "H")
    buttonTypeH=tkinter.ttk.Button(screenCalculator, text="H", command=actionTypeH, width=2).place(x=60, y=385)

    textShowI = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowI.place(x=85, y=415)
    def actionStoreI(): storeVarGenerator(I)()
    buttonStoreI=tkinter.ttk.Button(screenCalculator, text="Ans=I", command=actionStoreI, width=7).place(x=10, y=410)
    def actionTypeI():windowInputCalculator.insert("end", "I")
    buttonTypeI=tkinter.ttk.Button(screenCalculator, text="I", command=actionTypeI, width=2).place(x=60, y=410)

    textShowJ = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowJ.place(x=85, y=440)
    def actionStoreJ(): storeVarGenerator(J)()
    buttonStoreJ=tkinter.ttk.Button(screenCalculator, text="Ans=J", command=actionStoreJ, width=7).place(x=10, y=435)
    def actionTypeJ():windowInputCalculator.insert("end", "J")
    buttonTypeJ=tkinter.ttk.Button(screenCalculator, text="J", command=actionTypeJ, width=2).place(x=60, y=435)

    textShowK = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowK.place(x=85, y=465)
    def actionStoreK(): storeVarGenerator(K)()
    buttonStoreK=tkinter.ttk.Button(screenCalculator, text="Ans=K", command=actionStoreK, width=7).place(x=10, y=460)
    def actionTypeK():windowInputCalculator.insert("end", "K")
    buttonTypeK=tkinter.ttk.Button(screenCalculator, text="K", command=actionTypeK, width=2).place(x=60, y=460)

    textShowL = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowL.place(x=85, y=490)
    def actionStoreL(): storeVarGenerator(L)()
    buttonStoreL=tkinter.ttk.Button(screenCalculator, text="Ans=L", command=actionStoreL, width=7).place(x=10, y=485)
    def actionTypeL():windowInputCalculator.insert("end", "L")
    buttonTypeL=tkinter.ttk.Button(screenCalculator, text="L", command=actionTypeL, width=2).place(x=60, y=485)

    textShowM = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowM.place(x=85, y=515)
    def actionStoreM(): storeVarGenerator(M)()
    buttonStoreM=tkinter.ttk.Button(screenCalculator, text="Ans=M", command=actionStoreM, width=7).place(x=10, y=510)
    def actionTypeM():windowInputCalculator.insert("end", "M")
    buttonTypeM=tkinter.ttk.Button(screenCalculator, text="M", command=actionTypeM, width=2).place(x=60, y=510)

    textShowN = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowN.place(x=275, y=215)
    def actionStoreN(): storeVarGenerator(N)()
    buttonStoreN=tkinter.ttk.Button(screenCalculator, text="Ans=N", command=actionStoreN, width=7).place(x=200, y=210)
    def actionTypeN():windowInputCalculator.insert("end", "N")
    buttonTypeN=tkinter.ttk.Button(screenCalculator, text="N", command=actionTypeN, width=2).place(x=250, y=210)

    textShowO = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowO.place(x=275, y=240)
    def actionStoreO(): storeVarGenerator(O)()
    buttonStoreO=tkinter.ttk.Button(screenCalculator, text="Ans=O", command=actionStoreO, width=7).place(x=200, y=235)
    def actionTypeO():windowInputCalculator.insert("end", "O")
    buttonTypeO=tkinter.ttk.Button(screenCalculator, text="O", command=actionTypeO, width=2).place(x=250, y=235)

    textShowP = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowP.place(x=275, y=265)
    def actionStoreP(): storeVarGenerator(P)()
    buttonStoreP=tkinter.ttk.Button(screenCalculator, text="Ans=P", command=actionStoreP, width=7).place(x=200, y=260)
    def actionTypeP():windowInputCalculator.insert("end", "P")
    buttonTypeP=tkinter.ttk.Button(screenCalculator, text="P", command=actionTypeP, width=2).place(x=250, y=260)

    textShowQ = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowQ.place(x=275, y=290)
    def actionStoreQ(): storeVarGenerator(Q)()
    buttonStoreQ=tkinter.ttk.Button(screenCalculator, text="Ans=Q", command=actionStoreQ, width=7).place(x=200, y=285)
    def actionTypeQ():windowInputCalculator.insert("end", "Q")
    buttonTypeQ=tkinter.ttk.Button(screenCalculator, text="Q", command=actionTypeQ, width=2).place(x=250, y=285)

    textShowR = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowR.place(x=275, y=315)
    def actionStoreR(): storeVarGenerator(R)()
    buttonStoreR=tkinter.ttk.Button(screenCalculator, text="Ans=R", command=actionStoreR, width=7).place(x=200, y=310)
    def actionTypeR():windowInputCalculator.insert("end", "R")
    buttonTypeR=tkinter.ttk.Button(screenCalculator, text="R", command=actionTypeR, width=2).place(x=250, y=310)

    textShowS = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowS.place(x=275, y=340)
    def actionStoreS(): storeVarGenerator(S)()
    buttonStoreS=tkinter.ttk.Button(screenCalculator, text="Ans=S", command=actionStoreS, width=7).place(x=200, y=335)
    def actionTypeS():windowInputCalculator.insert("end", "S")
    buttonTypeS=tkinter.ttk.Button(screenCalculator, text="S", command=actionTypeS, width=2).place(x=250, y=335)

    textShowT = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowT.place(x=275, y=365)
    def actionStoreT(): storeVarGenerator(T)()
    buttonStoreT=tkinter.ttk.Button(screenCalculator, text="Ans=T", command=actionStoreT, width=7).place(x=200, y=360)
    def actionTypeT():windowInputCalculator.insert("end", "T")
    buttonTypeT=tkinter.ttk.Button(screenCalculator, text="T", command=actionTypeT, width=2).place(x=250, y=360)

    textShowU = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowU.place(x=275, y=390)
    def actionStoreU(): storeVarGenerator(U)()
    buttonStoreU=tkinter.ttk.Button(screenCalculator, text="Ans=U", command=actionStoreU, width=7).place(x=200, y=385)
    def actionTypeU():windowInputCalculator.insert("end", "U")
    buttonTypeU=tkinter.ttk.Button(screenCalculator, text="U", command=actionTypeU, width=2).place(x=250, y=385)

    textShowV = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowV.place(x=275, y=415)
    def actionStoreV(): storeVarGenerator(V)()
    buttonStoreV=tkinter.ttk.Button(screenCalculator, text="Ans=V", command=actionStoreV, width=7).place(x=200, y=410)
    def actionTypeV():windowInputCalculator.insert("end", "V")
    buttonTypeV=tkinter.ttk.Button(screenCalculator, text="V", command=actionTypeV, width=2).place(x=250, y=410)

    textShowW = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowW.place(x=275, y=440)
    def actionStoreW(): storeVarGenerator(W)()
    buttonStoreW=tkinter.ttk.Button(screenCalculator, text="Ans=W", command=actionStoreW, width=7).place(x=200, y=435)
    def actionTypeW():windowInputCalculator.insert("end", "W")
    buttonTypeW=tkinter.ttk.Button(screenCalculator, text="W", command=actionTypeW, width=2).place(x=250, y=435)

    textShowX = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowX.place(x=275, y=465)
    def actionStoreX(): storeVarGenerator(X)()
    buttonStoreX=tkinter.ttk.Button(screenCalculator, text="Ans=X", command=actionStoreX, width=7).place(x=200, y=460)
    def actionTypeX():windowInputCalculator.insert("end", "X")
    buttonTypeX=tkinter.ttk.Button(screenCalculator, text="X", command=actionTypeX, width=2).place(x=250, y=460)

    textShowY = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowY.place(x=275, y=490)
    def actionStoreY(): storeVarGenerator(Y)()
    buttonStoreY=tkinter.ttk.Button(screenCalculator, text="Ans=Y", command=actionStoreY, width=7).place(x=200, y=485)
    def actionTypeY():windowInputCalculator.insert("end", "Y")
    buttonTypeY=tkinter.ttk.Button(screenCalculator, text="Y", command=actionTypeY, width=2).place(x=250, y=485)

    textShowZ = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])
    textShowZ.place(x=275, y=515)
    def actionStoreZ(): storeVarGenerator(Z)()
    buttonStoreZ=tkinter.ttk.Button(screenCalculator, text="Ans=Z", command=actionStoreZ, width=7).place(x=200, y=510)
    def actionTypeZ():windowInputCalculator.insert("end", "Z")
    buttonTypeZ=tkinter.ttk.Button(screenCalculator, text="Z", command=actionTypeZ, width=2).place(x=250, y=510)
    
    screenCalculator.mainloop()

screenCalculatorDef()