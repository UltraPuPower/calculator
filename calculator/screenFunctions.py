import tkinter

from variables import actionBaseDef

def screenFunctionsDef(inputWindowView, inputWindowMath):

    def actionBase(viewInput, viewLength, mathInput, mathLength): actionBaseDef(viewInput, viewLength, mathInput, mathLength, inputWindowView, inputWindowMath)

    screenFunctions = tkinter.Tk()
    screenFunctions.title("Functions")
    screenFunctions.geometry("300x665+150+200")

    tkinter.ttk.Label(screenFunctions, text="Mathematical functions").place(x=5, y=5)
    def actionScreenFunctionsExit():
        screenFunctions.destroy()
    buttonScreenFunctionsExit=tkinter.ttk.Button(screenFunctions, text="Exit", command=actionScreenFunctionsExit, width=5).place(x=250, y=0)

    screenFunctions.mainloop()