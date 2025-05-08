# importeren
import math
import tkinter
import tkinter.ttk
import tkinter.messagebox
from tkinter import *
import random

# extra functies plus:
## inlogscherm met gebruikersnaam en wachtwoord [voltooid]
## variabelen met letter (naast ans) [voltooid]
## getallen e, pi en tau. [gepland]
## ln, arccos, arcsin en arctan [gepland]
## formulekaart [gepland]

# variabelen
ans_var = []
A = []
B = []
C = []
D = []
E = []
F = []
P = []
Q = []
R = []
X = []
Y = []
Z = []

print('Calculator running')

users = [
    {'userName': 'Admin', 'userPassword': 'P@$$w0rd'},
    {'userName': 'User1', 'userPassword': 'password'}
]

def loginCheck(givenName, givenKey):
    loginValid = False
    for user in users:
        if givenName in user['userName'] and givenKey in user['userPassword']:
            loginValid = True
    if loginValid:
        return True
    else:
        return False

# inloggen
def Login():
    
    def validateLogin():    
        attemptUsername = usernameEntry.get()
        attemptPassword = passwordEntry.get()

        if loginCheck(attemptUsername, attemptPassword):
            tkinter.messagebox.showinfo(title="Beware", message="Calculator not fully operational, there may be bugs.")
            screenLogin.destroy()
            calculator()
        else:
            tkinter.messagebox.showerror(title="Error", message="Username and password did not match.")
            usernameEntry.delete("0", "end")
            passwordEntry.delete("0", "end")

    screenLogin = Tk()
    screenLogin.title("Login")
    screenLogin.geometry("200x145+550+200")
    label_gebruikersnaam=tkinter.ttk.Label(screenLogin, text="Username").place(x=10, y=10)
    usernameEntry=tkinter.Entry(screenLogin, width=29)
    usernameEntry.place(x=10, y=35)
    textPassword=tkinter.ttk.Label(screenLogin, text="Password").place(x=10, y=60)
    passwordEntry=tkinter.Entry(screenLogin, width=29, show="•")
    passwordEntry.place(x=10, y=85)
    buttonLogin=tkinter.ttk.Button(screenLogin, text="Log in", command=validateLogin, width=10).place(x=120, y=110)

# rekenmachine
def calculator(): #Organise def()'s to be with respective buttons

    screenCalculator = Tk()
    screenCalculator.title("Rekenmachine")
    screenCalculator.geometry("195x510+550+200")
    windowInputCalculator=tkinter.Entry(screenCalculator, width=29)
    windowInputCalculator.place(x=10, y=10)
    tkinter.ttk.Label(screenCalculator, text="Calculator of UltraPuPower1, inspired by the calculator from 刘键明").place(x=300, y=500)
    tkinter.ttk.Label(screenCalculator, text="Answers might not be correct.\nUse at your own risk.\nV0.1", font=["Verdana", "7"]).place(x=0, y=550)
    tkinter.ttk.Separator(screenCalculator, orient=VERTICAL).place(x=195, y=55, height=110, width=5)
    tkinter.ttk.Separator(screenCalculator, orient=HORIZONTAL).place(x=0, y=165, height=5, width=195)
    tkinter.ttk.Separator(screenCalculator, orient=HORIZONTAL).place(x=0, y=55, height=5, width=195)

    def actionOne(): windowInputCalculator.insert("end","1")
    buttonOne=tkinter.ttk.Button(screenCalculator, text="1", command=actionOne, width=3).place(x=10, y=110)
    
    def actionTwo(): windowInputCalculator.insert("end","2")
    buttonTwo=tkinter.ttk.Button(screenCalculator, text="2", command=actionTwo, width=3).place(x=35, y=110)

    def actionThree(): windowInputCalculator.insert("end","3")
    buttonThree=tkinter.ttk.Button(screenCalculator, text="3", command=actionThree, width=3).place(x=60, y=110)

    def actionFour(): windowInputCalculator.insert("end","4")
    buttonFour=tkinter.ttk.Button(screenCalculator, text="4", command=actionFour, width=3).place(x=10, y=85)

    def actionFive(): windowInputCalculator.insert("end","5")
    buttonFive=tkinter.ttk.Button(screenCalculator, text="5", command=actionFive, width=3).place(x=35, y=85)

    def actionSix(): windowInputCalculator.insert("end","6")
    buttonSix=tkinter.ttk.Button(screenCalculator, text="6", command=actionSix, width=3).place(x=60, y=85)

    def actionSeven(): windowInputCalculator.insert("end","7")
    buttonSeven=tkinter.ttk.Button(screenCalculator, text="7", command=actionSeven, width=3).place(x=10, y=60)

    def actionEight(): windowInputCalculator.insert("end","8")
    buttonEight=tkinter.ttk.Button(screenCalculator, text="8", command=actionEight, width=3).place(x=35, y=60)

    def actionNine(): windowInputCalculator.insert("end","9")
    buttonNine=tkinter.ttk.Button(screenCalculator, text="9", command=actionNine, width=3).place(x=60, y=60)

    def actionZero(): windowInputCalculator.insert("end","0")
    buttonZero=tkinter.ttk.Button(screenCalculator, text="0", command=actionZero, width=7).place(x=10, y=135)

    def actionAdd(): windowInputCalculator.insert("end","+")
    buttonAdd = tkinter.ttk.Button(screenCalculator, text="+", command=actionAdd, width=3).place(x=85, y=110)

    def actionSubtract(): windowInputCalculator.insert("end","-")
    buttonSubtract = tkinter.ttk.Button(screenCalculator, text="-", command=actionSubtract, width=3).place(x=110, y=110)

    def actionMultiply(): windowInputCalculator.insert("end","*")
    buttonMultiply = tkinter.ttk.Button(screenCalculator, text="*", command=actionMultiply, width=3).place(x=85, y=85)

    def actionDivide(): windowInputCalculator.insert("end","/")
    buttonDivide = tkinter.ttk.Button(screenCalculator, text="/", command=actionDivide, width=3).place(x=110, y=85)

    def actionClear(): windowInputCalculator.delete("0", "end")
    buttonClear=tkinter.ttk.Button(screenCalculator, text="C", command=actionClear, width=3).place(x=85, y=60)

    def actionDot(): windowInputCalculator.insert("end", ".")
    buttonDot=tkinter.ttk.Button(screenCalculator, text=".", command=actionDot, width=3).place(x=60, y=135)

    def actionOpenParenthesis(): windowInputCalculator.insert("end", "(")
    buttonOpenParenthesis=tkinter.ttk.Button(screenCalculator, text="(", command=actionOpenParenthesis, width=3).place(x=135, y=60)

    def actionCloseParenthesis(): windowInputCalculator.insert("end", ")")
    buttonCloseParenthesis=tkinter.ttk.Button(screenCalculator, text=")", command=actionCloseParenthesis, width=3).place(x=160, y=60)

    def actionPower(): windowInputCalculator.insert("end", "**")
    buttonPower=tkinter.ttk.Button(screenCalculator, text="^", command=actionPower, width=3).place(x=135, y=85)

    def actionLog(): windowInputCalculator.insert("end", "math.log10(")
    buttonLog=tkinter.ttk.Button(screenCalculator, text="log", command=actionLog, width=3).place(x=160, y=85)

    def actionSine(): windowInputCalculator.insert("end", "math.sin(")
    buttonSine=tkinter.ttk.Button(screenCalculator, text="sin", command=actionSine, width=3).place(x=135, y=110)

    def actionCosine(): windowInputCalculator.insert("end", "math.cos(")
    buttonCosine=tkinter.ttk.Button(screenCalculator, text="cos", command=actionCosine, width=3).place(x=160, y=110)

    def actionTangent(): windowInputCalculator.insert("end", "math.tan(")
    buttonTangent=tkinter.ttk.Button(screenCalculator, text="tan", command=actionTangent, width=3).place(x=160, y=135)
    
    def actionBackspace():
        inhoud_windowInputCalculator = windowInputCalculator.get()
        inhoud_windowInputCalculator = inhoud_windowInputCalculator[:-1]
        windowInputCalculator.delete("0", "end")
        windowInputCalculator.insert("end", inhoud_windowInputCalculator)
    buttonBackspace=tkinter.ttk.Button(screenCalculator, text="del", command=actionBackspace, width=3).place(x=110, y=60)

    def berekenen():
        input=windowInputCalculator.get()
        try:
            ans_output = eval(input)
            output = float(eval(input))
            if output >= 10000000000: # NOTE: should be adjusted for negative range as well
                n = 0
                while output > 10:
                    n = n+1
                    output = output/10
                output = str(output)
                output = output[:10]
                # Alleen eerste n karakters: variabele_naam[:n]
                # Alle karakters behalve de laatste n karakters: variabele_naam[:-n]
                # Alleen laatste n karakters: variabele_naam[-n:]
                if n > 99:
                    b = "Error: te groot getal"
                else:
                    n = str(n)
                    a = output+"×10^"+n
                    b = "= "+a
            elif output < 0.0001 and output > 0: # NOTE: can be unified with below
                n = 0
                while output < 1:
                    n = n-1
                    output = output*10
                output = str(output)
                output = output[:10]
                if n < -99:
                    b = "Error: te klein getal"
                else:
                    n = str(n)
                    a = output+"×10^"+n
                    b = "= "+a
            elif output > -0.0001 and output < 0:
                n = 0
                while output > -1:
                    n = n-1
                    output = output*10
                output = str(output)
                output = output[:10]
                if n < -99:
                    b = "Error: te klein getal"
                else:
                    n = str(n)
                    a = output+"×10^"+n
                    b = "= "+a
            else:
                a = str(output)
                b = "= "+a
        except:
            b = "Error"
            ans_output = 0
        scherm2=tkinter.ttk.Label(screenCalculator, text=b+"                                               ")
        scherm2.place(x=10, y=35)
        if b != "Error" or b!= "Error: te klein getal" or b!= "Error, te groot getal":
            ans_var.clear()
            ans_var.insert(0, ans_output)
    buttonCalculate=tkinter.ttk.Button(screenCalculator, text="=", command=berekenen, width=7).place(x=85, y=135)

    def ans():
        windowInputCalculator.insert("end", ans_var)
    buttonAns=tkinter.ttk.Button(screenCalculator, text="ans", command=ans, width=3).place(x=135, y=135)

    def anstoA():
        ans_output2 = eval(windowInputCalculator.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            A.clear()
            A.insert(0, "0")
        else:
            A.clear()
            A.insert(0, ans_output2)
##        toon_A=tkinter.ttk.Label(screenCalculator, text=["A", "=", A], font=["Verdana", "11"]).place(x=85, y=200)
    def anstoB():
        ans_output2 = eval(windowInputCalculator.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            B.clear()
            B.insert(0, "0")
        else:
            B.clear()
            B.insert(0, ans_output2)
##        toon_B=tkinter.ttk.Label(screenCalculator, text=["B", "=", B], font=["Verdana", "11"]).place(x=85, y=225)
    def anstoC():
        ans_output2 = eval(windowInputCalculator.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            C.clear()
            C.insert(0, "0")
        else:
            C.clear()
            C.insert(0, ans_output2)
##        toon_C=tkinter.ttk.Label(screenCalculator, text=["C", "=", C], font=["Verdana", "11"]).place(x=85, y=250)
    def anstoD():
        ans_output2 = eval(windowInputCalculator.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            D.clear()
            D.insert(0, "0")
        else:
            D.clear()
            D.insert(0, ans_output2)
##        toon_D=tkinter.ttk.Label(screenCalculator, text=["D", "=", D], font=["Verdana", "11"]).place(x=85, y=275)
    def anstoE():
        ans_output2 = eval(windowInputCalculator.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            E.clear()
            E.insert(0, "0")
        else:
            E.clear()
            E.insert(0, ans_output2)
##        toon_E=tkinter.ttk.Label(screenCalculator, text=["E", "=", E], font=["Verdana", "11"]).place(x=85, y=300)
    def anstoF():
        ans_output2 = eval(windowInputCalculator.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            F.clear()
            F.insert(0, "0")
        else:
            F.clear()
            F.insert(0, ans_output2)
##        toon_F=tkinter.ttk.Label(screenCalculator, text=["F", "=", F], font=["Verdana", "11"]).place(x=85, y=325)
    def anstoP():
        ans_output2 = eval(windowInputCalculator.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            P.clear()
            P.insert(0, "0")
        else:
            P.clear()
            P.insert(0, ans_output2)
##        toon_P=tkinter.ttk.Label(screenCalculator, text=["P", "=", P], font=["Verdana", "11"]).place(x=85, y=350)
    def anstoQ():
        ans_output2 = eval(windowInputCalculator.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            Q.clear()
            Q.insert(0, "0")
        else:
            Q.clear()
            Q.insert(0, ans_output2)
##        toon_Q=tkinter.ttk.Label(screenCalculator, text=["Q", "=", Q], font=["Verdana", "11"]).place(x=85, y=375)
    def anstoR():
        ans_output2 = eval(windowInputCalculator.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            R.clear()
            R.insert(0, "0")
        else:
            R.clear()
            R.insert(0, ans_output2)
##        toon_R=tkinter.ttk.Label(screenCalculator, text=["R", "=", R], font=["Verdana", "11"]).place(x=85, y=400)
    def anstoX():
        ans_output2 = eval(windowInputCalculator.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            X.clear()
            X.insert(0, "0")
        else:
            X.clear()
            X.insert(0, ans_output2)
##        toon_X=tkinter.ttk.Label(screenCalculator, text=["X", "=", X], font=["Verdana", "11"]).place(x=85, y=425)
    def anstoY():
        ans_output2 = eval(windowInputCalculator.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            Y.clear()
            Y.insert(0, "0")
        else:
            Y.clear()
            Y.insert(0, ans_output2)
##        toon_Y=tkinter.ttk.Label(screenCalculator, text=["Y", "=", Y], font=["Verdana", "11"]).place(x=85, y=450)
    def anstoZ():
        ans_output2 = eval(windowInputCalculator.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            Z.clear()
            Z.insert(0, "0")
        else:
            Z.clear()
            Z.insert(0, ans_output2)
##        toon_Z=tkinter.ttk.Label(screenCalculator, text=["Z", "=", Z], font=["Verdana", "11"]).place(x=85, y=475)

    tkinter.ttk.Label(screenCalculator, text="Variabelen", font=["Arial", "12"]).place(x=10, y=175)
    knop_anstoA=tkinter.ttk.Button(screenCalculator, text="Ans=A", command=anstoA, width=7).place(x=10, y=200)
    knop_anstoB=tkinter.ttk.Button(screenCalculator, text="Ans=B", command=anstoB, width=7).place(x=10, y=225)
    knop_anstoC=tkinter.ttk.Button(screenCalculator, text="Ans=C", command=anstoC, width=7).place(x=10, y=250)
    knop_anstoD=tkinter.ttk.Button(screenCalculator, text="Ans=D", command=anstoD, width=7).place(x=10, y=275)
    knop_anstoE=tkinter.ttk.Button(screenCalculator, text="Ans=E", command=anstoE, width=7).place(x=10, y=300)
    knop_anstoF=tkinter.ttk.Button(screenCalculator, text="Ans=F", command=anstoF, width=7).place(x=10, y=325)
    knop_anstoP=tkinter.ttk.Button(screenCalculator, text="Ans=P", command=anstoP, width=7).place(x=10, y=350)
    knop_anstoQ=tkinter.ttk.Button(screenCalculator, text="Ans=Q", command=anstoQ, width=7).place(x=10, y=375)
    knop_anstoR=tkinter.ttk.Button(screenCalculator, text="Ans=R", command=anstoR, width=7).place(x=10, y=400)
    knop_anstoX=tkinter.ttk.Button(screenCalculator, text="Ans=X", command=anstoX, width=7).place(x=10, y=425)
    knop_anstoY=tkinter.ttk.Button(screenCalculator, text="Ans=Y", command=anstoY, width=7).place(x=10, y=450)
    knop_anstoZ=tkinter.ttk.Button(screenCalculator, text="Ans=Z", command=anstoZ, width=7).place(x=10, y=475)

    def A_ins():
        windowInputCalculator.insert("end", A)
    def B_ins():
        windowInputCalculator.insert("end", B)
    def C_ins():
        windowInputCalculator.insert("end", C)
    def D_ins():
        windowInputCalculator.insert("end", D)
    def E_ins():
        windowInputCalculator.insert("end", E)
    def F_ins():
        windowInputCalculator.insert("end", F)
    def P_ins():
        windowInputCalculator.insert("end", P)
    def Q_ins():
        windowInputCalculator.insert("end", Q)
    def R_ins():
        windowInputCalculator.insert("end", R)
    def X_ins():
        windowInputCalculator.insert("end", X)
    def Y_ins():
        windowInputCalculator.insert("end", Y)
    def Z_ins():
        windowInputCalculator.insert("end", Z)

    knop_A=tkinter.ttk.Button(screenCalculator, text="A", command=A_ins, width=2).place(x=60, y=200)
    knop_B=tkinter.ttk.Button(screenCalculator, text="B", command=B_ins, width=2).place(x=60, y=225)
    knop_C=tkinter.ttk.Button(screenCalculator, text="C", command=C_ins, width=2).place(x=60, y=250)
    knop_D=tkinter.ttk.Button(screenCalculator, text="D", command=D_ins, width=2).place(x=60, y=275)
    knop_E=tkinter.ttk.Button(screenCalculator, text="E", command=E_ins, width=2).place(x=60, y=300)
    knop_F=tkinter.ttk.Button(screenCalculator, text="F", command=F_ins, width=2).place(x=60, y=325)
    knop_P=tkinter.ttk.Button(screenCalculator, text="P", command=P_ins, width=2).place(x=60, y=350)
    knop_Q=tkinter.ttk.Button(screenCalculator, text="Q", command=Q_ins, width=2).place(x=60, y=375)
    knop_R=tkinter.ttk.Button(screenCalculator, text="R", command=R_ins, width=2).place(x=60, y=400)
    knop_X=tkinter.ttk.Button(screenCalculator, text="X", command=X_ins, width=2).place(x=60, y=425)
    knop_Y=tkinter.ttk.Button(screenCalculator, text="Y", command=Y_ins, width=2).place(x=60, y=450)
    knop_Z=tkinter.ttk.Button(screenCalculator, text="Z", command=Z_ins, width=2).place(x=60, y=475)
    
    screenCalculator.mainloop()
Login()
##rekenmachine()
