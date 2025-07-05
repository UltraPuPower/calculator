import tkinter
import tkinter.ttk
import tkinter.messagebox

from screenLogin import screenLoginDef
from screenRegister import screenRegisterDef

from variables import language

from langControl import langFile

def screenWelcomeDef(calculatorDef):

    chosenLang = language.getLang()

    langData = langFile[chosenLang].screenWelcome

    screenWelcome = tkinter.Tk()
    screenWelcome.title(langData.Title)
    screenWelcome.geometry("250x125+550+200")

    tkinter.ttk.Label(screenWelcome, text=langData.Labels.Welcome).place(x=10, y=10)

    tkinter.ttk.Label(screenWelcome, text=langData.Labels.Login).place(x=10, y=35)

    tkinter.ttk.Label(screenWelcome, text=langData.Labels.Register).place(x=10, y=60)

    def actionRegister():
        screenWelcome.destroy()
        screenRegisterDef(screenWelcomeDef)
    buttonRegister = tkinter.ttk.Button(screenWelcome, text=langData.Buttons.Register, command=actionRegister, width=10).place(x=10, y=90)

    def actionLogin():
        screenWelcome.destroy()
        screenLoginDef(calculatorDef, screenWelcomeDef)
    buttonLogin = tkinter.ttk.Button(screenWelcome, text=langData.Buttons.Login, command=actionLogin, width=10).place(x=170, y=90)

    screenWelcome.mainloop()