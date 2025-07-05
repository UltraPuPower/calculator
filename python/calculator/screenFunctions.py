import tkinter

from variables import language

from langControl import langFile

def screenFunctionsDef(inputWindowView):

    chosenLang = language.getLang()

    langData = langFile[chosenLang].screenFunctions

    screenFunctions = tkinter.Tk()
    screenFunctions.title(langData.Title)
    screenFunctions.geometry("300x665+150+200")

    tkinter.ttk.Label(screenFunctions, text=langData.Labels.Math).place(x=5, y=5)
    def actionScreenFunctionsExit():
        screenFunctions.destroy()
    buttonScreenFunctionsExit=tkinter.ttk.Button(screenFunctions, text=langData.Buttons.Exit, command=actionScreenFunctionsExit, width=6).place(x=245, y=0)

    def actionAcos(): inputWindowView.insert("end", "acos(")
    buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="acos", command=actionAcos, width=5).place(x=5, y=25)

    def actionAsin(): inputWindowView.insert("end", "asin(")
    buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="asin", command=actionAsin, width=5).place(x=5, y=50)

    def actionAtan(): inputWindowView.insert("end", "atan(")
    buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="atan", command=actionAtan, width=5).place(x=5, y=75)

    def actionAcosh(): inputWindowView.insert("end", "acosh(")
    buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="acosh", command=actionAcosh, width=5).place(x=50, y=25)

    def actionAsinh(): inputWindowView.insert("end", "asinh(")
    buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="asinh", command=actionAsinh, width=5).place(x=50, y=50)

    def actionAtanh(): inputWindowView.insert("end", "atanh(")
    buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="atanh", command=actionAtanh, width=5).place(x=50, y=75)

    screenFunctions.mainloop()