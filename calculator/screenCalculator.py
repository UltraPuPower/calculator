import tkinter
import tkinter.ttk
import tkinter.messagebox

from calculations import actionCalculate

from variables import valAnsView, valAnsMath, insertListView, insertListMath
from variables import actionBaseDef
from variables import debugger, debug

from screenFunctions import screenFunctionsDef

from screenVariables import screenVariablesDef

from screenConstants import screenConstantsDef
print('Calculator running')

def screenCalculatorDef():

    screenCalculator = tkinter.Tk()
    screenCalculator.title("Calculator")
    screenCalculator.geometry("310x595+500+200")

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

    windowInputCalculatorMath = tkinter.Entry(screenCalculator, width=47)
    windowInputCalculatorMath.place(x=10, y=10)

    windowInputCalculatorView = tkinter.Entry(screenCalculator, width=47)
    windowInputCalculatorView.place(x=10, y=10)

    def actionBase(viewInput, viewLength, mathInput, mathLength): actionBaseDef(viewInput, viewLength, mathInput, mathLength, windowInputCalculatorView, windowInputCalculatorMath)

    tkinter.ttk.Label(screenCalculator, text="Calculator by UltraPuPower1\ninspired by:\nCalculator by 刘键明", font=["Verdana", "9"]).place(x=5, y=210)
    tkinter.ttk.Label(screenCalculator, text="Answers might not be correct.\nUse at your own risk.\nV0.1", font=["Verdana", "7"]).place(x=5, y=550)
    tkinter.ttk.Separator(screenCalculator, orient=tkinter.VERTICAL).place(x=1, y=65, height=135, width=5)
    tkinter.ttk.Separator(screenCalculator, orient=tkinter.HORIZONTAL).place(x=2, y=65, height=5, width=195)
    tkinter.ttk.Separator(screenCalculator, orient=tkinter.VERTICAL).place(x=195, y=65, height=135, width=5)
    tkinter.ttk.Separator(screenCalculator, orient=tkinter.HORIZONTAL).place(x=1, y=200, height=5, width=195)

    windowOutputCalculator=tkinter.ttk.Label(screenCalculator, text = "")
    windowOutputCalculator.place(x=10, y=30)

    def actionCalculatorClose():
        tkinter.messagebox.showinfo(title="Goodbye", message="Thank you for using the calculator.\nSee you next time!")
        screenCalculator.destroy()
    buttonCalculatorClose=tkinter.ttk.Button(screenCalculator, text="Close", command=actionCalculatorClose, width=6).place(x=255, y=70)

    def actionOne(): actionBase("1", 1, "1", 1)
    buttonOne=tkinter.ttk.Button(screenCalculator, text="1", command=actionOne, width=3).place(x=10, y=70)
    
    def actionTwo(): actionBase("2", 1, "2", 1)
    buttonTwo=tkinter.ttk.Button(screenCalculator, text="2", command=actionTwo, width=3).place(x=40, y=70)

    def actionThree(): actionBase("3", 1, "3", 1)
    buttonThree=tkinter.ttk.Button(screenCalculator, text="3", command=actionThree, width=3).place(x=70, y=70)

    def actionAdd(): actionBase("+", 1, "+", 1)
    buttonAdd = tkinter.ttk.Button(screenCalculator, text="+", command=actionAdd, width=3).place(x=100, y=70)
    
    def actionBackspacer(window, list):
        try:
            viewString = window.get()
            viewLength = len(list) - 1
            viewCutLength = list[viewLength]
            list.pop(viewLength)
            cutViewString = viewString[0:-viewCutLength]
            window.delete("0", "end")
            window.insert("end", cutViewString)
        except IndexError:
            debugger("No more items to delete.")

    def actionBackspace():
        actionBackspacer(windowInputCalculatorView, insertListView)
        actionBackspacer(windowInputCalculatorMath, insertListMath)
        debugger(f'View:{insertListView}')
        debugger(f'Math:{insertListMath}')
    buttonBackspace=tkinter.ttk.Button(screenCalculator, text="del", command=actionBackspace, width=3).place(x=130, y=70)

    def actionSine(): actionBase("sin(", 4, "math.sin(", 9)
    buttonSine=tkinter.ttk.Button(screenCalculator, text="sin", command=actionSine, width=3).place(x=160, y=70)

    def actionFour(): actionBase("4", 1, "4", 1)
    buttonFour=tkinter.ttk.Button(screenCalculator, text="4", command=actionFour, width=3).place(x=10, y=95)

    def actionFive(): actionBase("5", 1, "5", 1)
    buttonFive=tkinter.ttk.Button(screenCalculator, text="5", command=actionFive, width=3).place(x=40, y=95)

    def actionSix(): actionBase("6", 1, "6", 1)
    buttonSix=tkinter.ttk.Button(screenCalculator, text="6", command=actionSix, width=3).place(x=70, y=95)

    def actionSubtract(): actionBase("-", 1, "-", 1)
    buttonSubtract = tkinter.ttk.Button(screenCalculator, text="-", command=actionSubtract, width=3).place(x=100, y=95)

    def actionClear():
        windowInputCalculatorView.delete("0", "end")
        windowInputCalculatorMath.delete("0", "end")
        insertListView.clear()
        insertListMath.clear()
        windowOutputCalculator.config(text = "")
    buttonClear=tkinter.ttk.Button(screenCalculator, text="C", command=actionClear, width=3).place(x=130, y=95)

    def actionCosine(): actionBase("cos(", 4, "math.cos(", 9)
    buttonCosine=tkinter.ttk.Button(screenCalculator, text="cos", command=actionCosine, width=3).place(x=160, y=95)

    def actionSeven(): actionBase("7", 1, "7", 1)
    buttonSeven=tkinter.ttk.Button(screenCalculator, text="7", command=actionSeven, width=3).place(x=10, y=120)

    def actionEight(): actionBase("8", 1, "8", 1)
    buttonEight=tkinter.ttk.Button(screenCalculator, text="8", command=actionEight, width=3).place(x=40, y=120)

    def actionNine(): actionBase("9", 1, "9", 1)
    buttonNine=tkinter.ttk.Button(screenCalculator, text="9", command=actionNine, width=3).place(x=70, y=120)

    def actionMultiply(): actionBase("×", 1, "*", 1)
    buttonMultiply = tkinter.ttk.Button(screenCalculator, text="×", command=actionMultiply, width=3).place(x=100, y=120)

    def actionDot(): actionBase(".", 1, ".", 1)
    buttonDot=tkinter.ttk.Button(screenCalculator, text=".", command=actionDot, width=3).place(x=130, y=120)

    def actionTangent(): actionBase("tan(", 4, "math.tan(", 9)
    buttonTangent=tkinter.ttk.Button(screenCalculator, text="tan", command=actionTangent, width=3).place(x=160, y=120)

    def actionZero(): actionBase("0", 1, "0", 1)
    buttonZero=tkinter.ttk.Button(screenCalculator, text="0", command=actionZero, width=3).place(x=40, y=145)

    def actionDivide(): actionBase("÷", 1, "/", 1)
    buttonDivide = tkinter.ttk.Button(screenCalculator, text="÷", command=actionDivide, width=3).place(x=100, y=145)

    def actionOpenParenthesis(): actionBase("(", 1, "(", 1)
    buttonOpenParenthesis=tkinter.ttk.Button(screenCalculator, text="(", command=actionOpenParenthesis, width=3).place(x=130, y=145)

    def actionLog():
        windowInputCalculatorView.insert("end", "log10(")
        windowInputCalculatorMath.insert("end", "math.log10(")
        insertListView.append(3)
        insertListView.append(2)
        insertListView.append(1)
        insertListMath.append(8)
        insertListMath.append(2)
        insertListMath.append(1)
        debugger(f'View:{insertListView}')
        debugger(f'Math:{insertListMath}')
    buttonLog=tkinter.ttk.Button(screenCalculator, text="log", command=actionLog, width=3).place(x=160, y=145)

    def storeAns(valPrint, valMath):
        valAnsView.clear()
        valAnsView.insert(0, valPrint)
        valAnsMath.clear()
        valAnsMath.insert(1, valMath)

    def actionDisplayCalculation():
        result = actionCalculate(windowInputCalculatorMath)
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
    buttonCalculate=tkinter.ttk.Button(screenCalculator, text="=", command=actionDisplayCalculation, width=3).place(x=10, y=170)

    def actionAns(): actionBase("Ans", 3, valAnsMath[0], len(valAnsMath[0]))
    buttonAns=tkinter.ttk.Button(screenCalculator, text="ans", command=actionAns, width=3).place(x=40, y=170)

    def actionAns(): actionBase("×10^", 4, "*10**", 5)
    buttonAns=tkinter.ttk.Button(screenCalculator, text="×10", command=actionAns, width=4).place(x=70, y=170)

    def actionPower(): actionBase("^", 1, "**", 2)
    buttonPower=tkinter.ttk.Button(screenCalculator, text="^", command=actionPower, width=3).place(x=100, y=170)

    def actionCloseParenthesis(): actionBase(")", 1, ")", 1)
    buttonCloseParenthesis=tkinter.ttk.Button(screenCalculator, text=")", command=actionCloseParenthesis, width=3).place(x=130, y=170)

    def actionSquareroot(): actionBase("√(", 2, "math.sqrt(", 10)
    buttonSquareroot=tkinter.ttk.Button(screenCalculator, text="√", command=actionSquareroot, width=3).place(x=160, y=170)

    def actionOpenVariables(): screenVariablesDef(windowInputCalculatorView, windowInputCalculatorMath, actionCalculate)
    buttonVariables=tkinter.ttk.Button(screenCalculator, text="Variables", command=actionOpenVariables, width=15).place(x=200, y=120)
    
    def actionOpenFunctions(): screenFunctionsDef(windowInputCalculatorView, windowInputCalculatorMath)
    buttonFunctions=tkinter.ttk.Button(screenCalculator, text="Functions", command=actionOpenFunctions, width=15).place(x=200, y=145)
    
    def actionOpenConstants(): screenConstantsDef(windowInputCalculatorView, windowInputCalculatorMath)
    buttonConstants=tkinter.ttk.Button(screenCalculator, text="Constants", command=actionOpenConstants, width=15).place(x=200, y=170)

    if debug == True:
        def actionViewCheck():
            viewString = windowInputCalculatorView.get()
            mathString = windowInputCalculatorMath.get()
            debugger('------======------')
            debugger(f'View:{viewString}')
            debugger(f'Math:{mathString}')
            debugger('------======------')
        buttonBackspace=tkinter.ttk.Button(screenCalculator, text="Check", command=actionViewCheck, width=6).place(x=255, y=95)
    
    screenCalculator.mainloop()