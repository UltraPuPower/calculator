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

    def actionAcos(): actionBase("acos(", 5, "math.acos(", 10)
    buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="acos", command=actionAcos, width=5).place(x=5, y=25)

    def actionAsin(): actionBase("asin(", 5, "math.asin(", 10)
    buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="asin", command=actionAsin, width=5).place(x=5, y=50)

    def actionAtan(): actionBase("atan(", 5, "math.atan(", 10)
    buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="atan", command=actionAtan, width=5).place(x=5, y=75)

    def actionAcosh(): actionBase("acosh(", 6, "math.acosh(", 11)
    buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="acosh", command=actionAcosh, width=5).place(x=50, y=25)

    def actionAsinh(): actionBase("asinh(", 6, "math.asinh(", 11)
    buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="asinh", command=actionAsinh, width=5).place(x=50, y=50)

    def actionAtanh(): actionBase("atanh(", 6, "math.atanh(", 11)
    buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="atanh", command=actionAtanh, width=5).place(x=50, y=75)

    screenFunctions.mainloop()