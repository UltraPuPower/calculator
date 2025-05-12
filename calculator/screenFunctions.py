import tkinter

def screenFunctionsDef(inputWindow):
    screenFunctions = tkinter.Tk()
    screenFunctions.title("Functions")
    screenFunctions.geometry("300x665+150+200")

    tkinter.ttk.Label(screenFunctions, text="Mathematical functions").place(x=5, y=5)
    def actionScreenFunctionsExit():
        screenFunctions.destroy()
    buttonScreenFunctionsExit=tkinter.ttk.Button(screenFunctions, text="Exit", command=actionScreenFunctionsExit, width=5).place(x=250, y=0)

    def actionSquareroot(): inputWindow.insert("end", "√(")
    buttonSquareroot=tkinter.ttk.Button(screenFunctions, text="√", command=actionSquareroot, width=3).place(x=5, y=20)

    screenFunctions.mainloop()