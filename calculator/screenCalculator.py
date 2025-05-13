import tkinter
import tkinter.ttk
import tkinter.messagebox

from calculations import actionCalculate
from variables import valAnsPrint, valAnsMath

from screenFunctions import screenFunctionsDef

from screenVariables import screenVariablesDef

from screenConstants import screenConstantsDef

print('Calculator running')

def screenCalculatorDef():

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

    windowInputCalculator = tkinter.Entry(screenCalculator, width=29)
    windowInputCalculator.place(x=10, y=10)
    tkinter.ttk.Label(screenCalculator, text="Calculator by UltraPuPower1\ninspired by:\nCalculator by 刘键明", font=["Verdana", "9"]).place(x=200, y=8)
    tkinter.ttk.Label(screenCalculator, text="Answers might not be correct.\nUse at your own risk.\nV0.1", font=["Verdana", "7"]).place(x=0, y=550)
    tkinter.ttk.Separator(screenCalculator, orient=tkinter.VERTICAL).place(x=195, y=65, height=110, width=5)
    tkinter.ttk.Separator(screenCalculator, orient=tkinter.HORIZONTAL).place(x=0, y=175, height=5, width=195)
    tkinter.ttk.Separator(screenCalculator, orient=tkinter.HORIZONTAL).place(x=0, y=65, height=5, width=195)

    windowOutputCalculator=tkinter.ttk.Label(screenCalculator, text = "")
    windowOutputCalculator.place(x=10, y=30)

    def actionCalculatorClose():
        tkinter.messagebox.showinfo(title="Goodbye", message="Thank you for using the calculator.\nSee you next time!")
        screenCalculator.destroy()
    buttonCalculatorClose=tkinter.ttk.Button(screenCalculator, text="Close", command=actionCalculatorClose, width=5).place(x=400, y=0)

    def getTextScreenCalculator():
        text = windowInputCalculator.get()
        return text

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

    def actionDisplayCalculation():
        result = actionCalculate(getTextScreenCalculator())
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

    def actionOpenVariables(): screenVariablesDef(windowInputCalculator, actionCalculate)
    buttonVariables=tkinter.ttk.Button(screenCalculator, text="Variables", command=actionOpenVariables, width=15).place(x=200, y=70)
    
    def actionOpenFunctions(): screenFunctionsDef(windowInputCalculator)
    buttonFunctions=tkinter.ttk.Button(screenCalculator, text="Functions", command=actionOpenFunctions, width=15).place(x=200, y=95)
    
    def actionOpenConstants(): screenConstantsDef(windowInputCalculator)
    buttonConstants=tkinter.ttk.Button(screenCalculator, text="Constants", command=actionOpenConstants, width=15).place(x=200, y=120)
    
    screenCalculator.mainloop()