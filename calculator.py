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
            rekenmachine()
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
def rekenmachine(): #Organise def()'s to be with respective buttons
    def plus():
        scherm1.insert("end","+")
    def min():
        scherm1.insert("end","-")        
    def keer():
        scherm1.insert("end","*")        
    def delen():
        scherm1.insert("end","/")
    def een():
        scherm1.insert("end","1")        
    def twee():
        scherm1.insert("end","2")        
    def drie():
        scherm1.insert("end","3")        
    def vier():
        scherm1.insert("end","4")        
    def vijf():
        scherm1.insert("end","5")        
    def zes():
        scherm1.insert("end","6")        
    def zeven():
        scherm1.insert("end","7")        
    def acht():
        scherm1.insert("end","8")        
    def negen():
        scherm1.insert("end","9")        
    def nul():
        scherm1.insert("end","0")
    def clear():
        scherm1.delete("0", "end")
    def punt():
        scherm1.insert("end", ".")
    def haakje_openen():
        scherm1.insert("end", "(")
    def haakje_sluiten():
        scherm1.insert("end", ")")
    def macht():
        scherm1.insert("end", "**")
    def log():
        scherm1.insert("end", "math.log10(")
    def sin():
        scherm1.insert("end", "math.sin(")
    def cos():
        scherm1.insert("end", "math.cos(")
    def tan():
        scherm1.insert("end", "math.tan(")
    def backspace():
        inhoud_scherm1 = scherm1.get()
        inhoud_scherm1 = inhoud_scherm1[:-1]
        scherm1.delete("0", "end")
        scherm1.insert("end", inhoud_scherm1)
    def berekenen():
        input=scherm1.get()
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
                    a = output+"x×10^"+n
                    b = "= "+a
            else:
                a = str(output)
                b = "= "+a
        except:
            b = "Error"
            ans_output = 0
        scherm2=tkinter.ttk.Label(venster_rekenmachine, text=b+"                                               ")
        scherm2.place(x=10, y=35)
        if b != "Error" or b!= "Error: te klein getal" or b!= "Error, te groot getal":
            ans_var.clear()
            ans_var.insert(0, ans_output)
    def ans():
        scherm1.insert("end", ans_var)

    venster_rekenmachine = Tk()
    venster_rekenmachine.title("Rekenmachine")
    venster_rekenmachine.geometry("195x510+550+200")
    scherm1=tkinter.Entry(venster_rekenmachine, width=29)
    scherm1.place(x=10, y=10)
    buttonAdd = tkinter.ttk.Button(venster_rekenmachine, text="+", command=plus, width=3).place(x=85, y=110)
    buttonSubtract = tkinter.ttk.Button(venster_rekenmachine, text="-", command=min, width=3).place(x=110, y=110)
    buttonMultiply = tkinter.ttk.Button(venster_rekenmachine, text="*", command=keer, width=3).place(x=85, y=85)
    buttonDivide = tkinter.ttk.Button(venster_rekenmachine, text="/", command=delen, width=3).place(x=110, y=85)
    knop_1=tkinter.ttk.Button(venster_rekenmachine, text="1", command=een, width=3).place(x=10, y=110)
    knop_2=tkinter.ttk.Button(venster_rekenmachine, text="2", command=twee, width=3).place(x=35, y=110)
    knop_3=tkinter.ttk.Button(venster_rekenmachine, text="3", command=drie, width=3).place(x=60, y=110)
    knop_4=tkinter.ttk.Button(venster_rekenmachine, text="4", command=vier, width=3).place(x=10, y=85)
    knop_5=tkinter.ttk.Button(venster_rekenmachine, text="5", command=vijf, width=3).place(x=35, y=85)
    knop_6=tkinter.ttk.Button(venster_rekenmachine, text="6", command=zes, width=3).place(x=60, y=85)
    knop_7=tkinter.ttk.Button(venster_rekenmachine, text="7", command=zeven, width=3).place(x=10, y=60)
    knop_8=tkinter.ttk.Button(venster_rekenmachine, text="8", command=acht, width=3).place(x=35, y=60)
    knop_9=tkinter.ttk.Button(venster_rekenmachine, text="9", command=negen, width=3).place(x=60, y=60)
    knop_0=tkinter.ttk.Button(venster_rekenmachine, text="0", command=nul, width=7).place(x=10, y=135)
    buttonDot=tkinter.ttk.Button(venster_rekenmachine, text=".", command=punt, width=3).place(x=60, y=135)
    buttonClear=tkinter.ttk.Button(venster_rekenmachine, text="C", command=clear, width=3).place(x=85, y=60)
    buttonBackspace=tkinter.ttk.Button(venster_rekenmachine, text="del", command=backspace, width=3).place(x=110, y=60)
    buttonCalculate=tkinter.ttk.Button(venster_rekenmachine, text="=", command=berekenen, width=7).place(x=85, y=135)
    buttonPower=tkinter.ttk.Button(venster_rekenmachine, text="^", command=macht, width=3).place(x=135, y=85)
    buttonOpenParenthesis=tkinter.ttk.Button(venster_rekenmachine, text="(", command=haakje_openen, width=3).place(x=135, y=60)
    buttonCloseParenthesis=tkinter.ttk.Button(venster_rekenmachine, text=")", command=haakje_sluiten, width=3).place(x=160, y=60)
    buttonLog=tkinter.ttk.Button(venster_rekenmachine, text="log", command=log, width=3).place(x=160, y=85)
    buttonSine=tkinter.ttk.Button(venster_rekenmachine, text="sin", command=sin, width=3).place(x=135, y=110)
    buttonCosine=tkinter.ttk.Button(venster_rekenmachine, text="cos", command=cos, width=3).place(x=160, y=110)
    buttonAns=tkinter.ttk.Button(venster_rekenmachine, text="ans", command=ans, width=3).place(x=135, y=135)
    buttonTangent=tkinter.ttk.Button(venster_rekenmachine, text="tan", command=tan, width=3).place(x=160, y=135)
    tkinter.ttk.Label(venster_rekenmachine, text="Rekenmachine van 刘键明").place(x=300, y=500)
    tkinter.ttk.Label(venster_rekenmachine, text="De antwoorden zijn mogelijk onjuist.\nGebruik op eigen risico.\nV1.1", font=["Verdana", "7"]).place(x=0, y=550)
    tkinter.ttk.Separator(venster_rekenmachine, orient=VERTICAL).place(x=195, y=55, height=110, width=5)
    tkinter.ttk.Separator(venster_rekenmachine, orient=HORIZONTAL).place(x=0, y=165, height=5, width=195)
    tkinter.ttk.Separator(venster_rekenmachine, orient=HORIZONTAL).place(x=0, y=55, height=5, width=195)

    def anstoA():
        ans_output2 = eval(scherm1.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            A.clear()
            A.insert(0, "0")
        else:
            A.clear()
            A.insert(0, ans_output2)
##        toon_A=tkinter.ttk.Label(venster_rekenmachine, text=["A", "=", A], font=["Verdana", "11"]).place(x=85, y=200)
    def anstoB():
        ans_output2 = eval(scherm1.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            B.clear()
            B.insert(0, "0")
        else:
            B.clear()
            B.insert(0, ans_output2)
##        toon_B=tkinter.ttk.Label(venster_rekenmachine, text=["B", "=", B], font=["Verdana", "11"]).place(x=85, y=225)
    def anstoC():
        ans_output2 = eval(scherm1.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            C.clear()
            C.insert(0, "0")
        else:
            C.clear()
            C.insert(0, ans_output2)
##        toon_C=tkinter.ttk.Label(venster_rekenmachine, text=["C", "=", C], font=["Verdana", "11"]).place(x=85, y=250)
    def anstoD():
        ans_output2 = eval(scherm1.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            D.clear()
            D.insert(0, "0")
        else:
            D.clear()
            D.insert(0, ans_output2)
##        toon_D=tkinter.ttk.Label(venster_rekenmachine, text=["D", "=", D], font=["Verdana", "11"]).place(x=85, y=275)
    def anstoE():
        ans_output2 = eval(scherm1.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            E.clear()
            E.insert(0, "0")
        else:
            E.clear()
            E.insert(0, ans_output2)
##        toon_E=tkinter.ttk.Label(venster_rekenmachine, text=["E", "=", E], font=["Verdana", "11"]).place(x=85, y=300)
    def anstoF():
        ans_output2 = eval(scherm1.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            F.clear()
            F.insert(0, "0")
        else:
            F.clear()
            F.insert(0, ans_output2)
##        toon_F=tkinter.ttk.Label(venster_rekenmachine, text=["F", "=", F], font=["Verdana", "11"]).place(x=85, y=325)
    def anstoP():
        ans_output2 = eval(scherm1.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            P.clear()
            P.insert(0, "0")
        else:
            P.clear()
            P.insert(0, ans_output2)
##        toon_P=tkinter.ttk.Label(venster_rekenmachine, text=["P", "=", P], font=["Verdana", "11"]).place(x=85, y=350)
    def anstoQ():
        ans_output2 = eval(scherm1.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            Q.clear()
            Q.insert(0, "0")
        else:
            Q.clear()
            Q.insert(0, ans_output2)
##        toon_Q=tkinter.ttk.Label(venster_rekenmachine, text=["Q", "=", Q], font=["Verdana", "11"]).place(x=85, y=375)
    def anstoR():
        ans_output2 = eval(scherm1.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            R.clear()
            R.insert(0, "0")
        else:
            R.clear()
            R.insert(0, ans_output2)
##        toon_R=tkinter.ttk.Label(venster_rekenmachine, text=["R", "=", R], font=["Verdana", "11"]).place(x=85, y=400)
    def anstoX():
        ans_output2 = eval(scherm1.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            X.clear()
            X.insert(0, "0")
        else:
            X.clear()
            X.insert(0, ans_output2)
##        toon_X=tkinter.ttk.Label(venster_rekenmachine, text=["X", "=", X], font=["Verdana", "11"]).place(x=85, y=425)
    def anstoY():
        ans_output2 = eval(scherm1.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            Y.clear()
            Y.insert(0, "0")
        else:
            Y.clear()
            Y.insert(0, ans_output2)
##        toon_Y=tkinter.ttk.Label(venster_rekenmachine, text=["Y", "=", Y], font=["Verdana", "11"]).place(x=85, y=450)
    def anstoZ():
        ans_output2 = eval(scherm1.get())
        if ans_output2 >= 10000000000 or abs(ans_output2) < 0.001 and ans_output2 != 0:
            Z.clear()
            Z.insert(0, "0")
        else:
            Z.clear()
            Z.insert(0, ans_output2)
##        toon_Z=tkinter.ttk.Label(venster_rekenmachine, text=["Z", "=", Z], font=["Verdana", "11"]).place(x=85, y=475)

    tkinter.ttk.Label(venster_rekenmachine, text="Variabelen", font=["Arial", "12"]).place(x=10, y=175)
    knop_anstoA=tkinter.ttk.Button(venster_rekenmachine, text="Ans=A", command=anstoA, width=7).place(x=10, y=200)
    knop_anstoB=tkinter.ttk.Button(venster_rekenmachine, text="Ans=B", command=anstoB, width=7).place(x=10, y=225)
    knop_anstoC=tkinter.ttk.Button(venster_rekenmachine, text="Ans=C", command=anstoC, width=7).place(x=10, y=250)
    knop_anstoD=tkinter.ttk.Button(venster_rekenmachine, text="Ans=D", command=anstoD, width=7).place(x=10, y=275)
    knop_anstoE=tkinter.ttk.Button(venster_rekenmachine, text="Ans=E", command=anstoE, width=7).place(x=10, y=300)
    knop_anstoF=tkinter.ttk.Button(venster_rekenmachine, text="Ans=F", command=anstoF, width=7).place(x=10, y=325)
    knop_anstoP=tkinter.ttk.Button(venster_rekenmachine, text="Ans=P", command=anstoP, width=7).place(x=10, y=350)
    knop_anstoQ=tkinter.ttk.Button(venster_rekenmachine, text="Ans=Q", command=anstoQ, width=7).place(x=10, y=375)
    knop_anstoR=tkinter.ttk.Button(venster_rekenmachine, text="Ans=R", command=anstoR, width=7).place(x=10, y=400)
    knop_anstoX=tkinter.ttk.Button(venster_rekenmachine, text="Ans=X", command=anstoX, width=7).place(x=10, y=425)
    knop_anstoY=tkinter.ttk.Button(venster_rekenmachine, text="Ans=Y", command=anstoY, width=7).place(x=10, y=450)
    knop_anstoZ=tkinter.ttk.Button(venster_rekenmachine, text="Ans=Z", command=anstoZ, width=7).place(x=10, y=475)

    def A_ins():
        scherm1.insert("end", A)
    def B_ins():
        scherm1.insert("end", B)
    def C_ins():
        scherm1.insert("end", C)
    def D_ins():
        scherm1.insert("end", D)
    def E_ins():
        scherm1.insert("end", E)
    def F_ins():
        scherm1.insert("end", F)
    def P_ins():
        scherm1.insert("end", P)
    def Q_ins():
        scherm1.insert("end", Q)
    def R_ins():
        scherm1.insert("end", R)
    def X_ins():
        scherm1.insert("end", X)
    def Y_ins():
        scherm1.insert("end", Y)
    def Z_ins():
        scherm1.insert("end", Z)

    knop_A=tkinter.ttk.Button(venster_rekenmachine, text="A", command=A_ins, width=2).place(x=60, y=200)
    knop_B=tkinter.ttk.Button(venster_rekenmachine, text="B", command=B_ins, width=2).place(x=60, y=225)
    knop_C=tkinter.ttk.Button(venster_rekenmachine, text="C", command=C_ins, width=2).place(x=60, y=250)
    knop_D=tkinter.ttk.Button(venster_rekenmachine, text="D", command=D_ins, width=2).place(x=60, y=275)
    knop_E=tkinter.ttk.Button(venster_rekenmachine, text="E", command=E_ins, width=2).place(x=60, y=300)
    knop_F=tkinter.ttk.Button(venster_rekenmachine, text="F", command=F_ins, width=2).place(x=60, y=325)
    knop_P=tkinter.ttk.Button(venster_rekenmachine, text="P", command=P_ins, width=2).place(x=60, y=350)
    knop_Q=tkinter.ttk.Button(venster_rekenmachine, text="Q", command=Q_ins, width=2).place(x=60, y=375)
    knop_R=tkinter.ttk.Button(venster_rekenmachine, text="R", command=R_ins, width=2).place(x=60, y=400)
    knop_X=tkinter.ttk.Button(venster_rekenmachine, text="X", command=X_ins, width=2).place(x=60, y=425)
    knop_Y=tkinter.ttk.Button(venster_rekenmachine, text="Y", command=Y_ins, width=2).place(x=60, y=450)
    knop_Z=tkinter.ttk.Button(venster_rekenmachine, text="Z", command=Z_ins, width=2).place(x=60, y=475)
    
    venster_rekenmachine.mainloop()
Login()
##rekenmachine()
