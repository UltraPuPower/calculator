import tkinter
import tkinter.ttk
import tkinter.messagebox

from screenLogin import screenLoginDef
from screenRegister import screenRegisterDef

def screenWelcomeDef(calculatorDef):

    screenWelcome = tkinter.Tk()
    screenWelcome.title("Welcome")
    screenWelcome.geometry("250x125+550+200")

    tkinter.ttk.Label(screenWelcome, text="Welcome to UltraPuPower1's Calculator.").place(x=10, y=10)

    tkinter.ttk.Label(screenWelcome, text="Log in to continue.").place(x=10, y=35)

    tkinter.ttk.Label(screenWelcome, text="If you don't have an account, register one.").place(x=10, y=60)

    def actionRegister():
        screenWelcome.destroy()
        screenRegisterDef(screenWelcomeDef)
    buttonRegister = tkinter.ttk.Button(screenWelcome, text="Register", command=actionRegister, width=10).place(x=10, y=90)

    def actionLogin():
        screenWelcome.destroy()
        screenLoginDef(calculatorDef, screenWelcomeDef)
    buttonRegister = tkinter.ttk.Button(screenWelcome, text="Log in", command=actionLogin, width=10).place(x=170, y=90)

    screenWelcome.mainloop()