import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

from calculations import actionCalculate

from variables import valAnsView, insertListView, loggedIn, language
from variables import debugger, debugMode

from screenFunctions import screenFunctionsDef

from screenVariables import screenVariablesDef

from screenConstants import screenConstantsDef

from screenLang import screenLangPickDef

from langControl import langFile
print('Calculator running')

def screenCalculatorDef():

    chosenLang = language.getLang()

    langData = langFile[chosenLang].screenCalculator

    debugger(f"Current lang: {language.getLang()}")

    screenCalculator = tkinter.Tk()
    screenCalculator.title(langData.Title)
    screenCalculator.geometry("310x595+500+200")

    helperLines = False
    if helperLines:
        helperLinesHori = False
        helperLinesVert = True
        i = 1
        if helperLinesHori:
            while i <= 119:
                ttk.Separator(screenCalculator, orient=tkinter.HORIZONTAL).place(x=0, y=i*5, height=5, width=465)
                i = i + 1
        if helperLinesVert:
            while i <= 93:
                ttk.Separator(screenCalculator, orient=tkinter.VERTICAL).place(x=i*5, y=0, height=595, width=5)
                i = i + 1

    windowInputCalculatorView = tkinter.Entry(screenCalculator, width=47)
    windowInputCalculatorView.place(x=10, y=10)

    ttk.Label(screenCalculator, text=langData.Labels.Credits, font=["Verdana", "9"]).place(x=5, y=210)
    ttk.Label(screenCalculator, text=langData.Labels.Disclaimer, font=["Verdana", "7"]).place(x=5, y=550)
    ttk.Separator(screenCalculator, orient=tkinter.VERTICAL).place(x=1, y=65, height=135, width=5)
    ttk.Separator(screenCalculator, orient=tkinter.HORIZONTAL).place(x=2, y=65, height=5, width=195)
    ttk.Separator(screenCalculator, orient=tkinter.VERTICAL).place(x=195, y=65, height=135, width=5)
    ttk.Separator(screenCalculator, orient=tkinter.HORIZONTAL).place(x=1, y=200, height=5, width=195)

    windowOutputCalculator=ttk.Label(screenCalculator, text = "")
    windowOutputCalculator.place(x=10, y=30)

    def actionCalculatorClose():
        messagebox.showinfo(title=langData.Messageboxes.Close.Title, message=langData.Messageboxes.Close.Message)
        screenCalculator.destroy()
    buttonCalculatorClose=ttk.Button(screenCalculator, text=langData.Buttons.Close, command=actionCalculatorClose, width=6).place(x=255, y=70)

    def actionOne(): windowInputCalculatorView.insert("end", "1")
    buttonOne=ttk.Button(screenCalculator, text="1", command=actionOne, width=3).place(x=10, y=70)
    
    def actionTwo(): windowInputCalculatorView.insert("end", "2")
    buttonTwo=ttk.Button(screenCalculator, text="2", command=actionTwo, width=3).place(x=40, y=70)

    def actionThree(): windowInputCalculatorView.insert("end", "3")
    buttonThree=ttk.Button(screenCalculator, text="3", command=actionThree, width=3).place(x=70, y=70)

    def actionAdd(): windowInputCalculatorView.insert("end", "+")
    buttonAdd = ttk.Button(screenCalculator, text="+", command=actionAdd, width=3).place(x=100, y=70)

    def actionBackspace():
        try:
            viewString = windowInputCalculatorView.get()
            viewLength = len(list) - 1
            viewCutLength = list[viewLength]
            list.pop(viewLength)
            cutViewString = viewString[0:-viewCutLength]
            windowInputCalculatorView.delete("0", "end")
            windowInputCalculatorView.insert("end", cutViewString)
        except IndexError:
            debugger("No more items to delete.")
        debugger(f'View:{insertListView}')
    buttonBackspace=ttk.Button(screenCalculator, text="del", command=actionBackspace, width=3).place(x=130, y=70)

    def actionSine(): windowInputCalculatorView.insert("end", "sin(")
    buttonSine=ttk.Button(screenCalculator, text="sin", command=actionSine, width=3).place(x=160, y=70)

    def actionFour(): windowInputCalculatorView.insert("end", "4")
    buttonFour=ttk.Button(screenCalculator, text="4", command=actionFour, width=3).place(x=10, y=95)

    def actionFive(): windowInputCalculatorView.insert("end", "5")
    buttonFive=ttk.Button(screenCalculator, text="5", command=actionFive, width=3).place(x=40, y=95)

    def actionSix(): windowInputCalculatorView.insert("end", "6")
    buttonSix=ttk.Button(screenCalculator, text="6", command=actionSix, width=3).place(x=70, y=95)

    def actionSubtract(): windowInputCalculatorView.insert("end", "-")
    buttonSubtract = ttk.Button(screenCalculator, text="-", command=actionSubtract, width=3).place(x=100, y=95)

    def actionClear():
        windowInputCalculatorView.delete("0", "end")
        insertListView.clear()
        windowOutputCalculator.config(text = "")
    buttonClear=ttk.Button(screenCalculator, text="C", command=actionClear, width=3).place(x=130, y=95)

    def actionCosine(): windowInputCalculatorView.insert("end", "cos(")
    buttonCosine=ttk.Button(screenCalculator, text="cos", command=actionCosine, width=3).place(x=160, y=95)

    def actionSeven(): windowInputCalculatorView.insert("end", "7")
    buttonSeven=ttk.Button(screenCalculator, text="7", command=actionSeven, width=3).place(x=10, y=120)

    def actionEight(): windowInputCalculatorView.insert("end", "8")
    buttonEight=ttk.Button(screenCalculator, text="8", command=actionEight, width=3).place(x=40, y=120)

    def actionNine(): windowInputCalculatorView.insert("end", "9")
    buttonNine=ttk.Button(screenCalculator, text="9", command=actionNine, width=3).place(x=70, y=120)

    def actionMultiply(): windowInputCalculatorView.insert("end", "×")
    buttonMultiply = ttk.Button(screenCalculator, text="×", command=actionMultiply, width=3).place(x=100, y=120)

    def actionDot(): windowInputCalculatorView.insert("end", ".")
    buttonDot=ttk.Button(screenCalculator, text=".", command=actionDot, width=3).place(x=130, y=120)

    def actionTangent(): windowInputCalculatorView.insert("end", "tan")
    buttonTangent=ttk.Button(screenCalculator, text="tan", command=actionTangent, width=3).place(x=160, y=120)

    def actionZero(): windowInputCalculatorView.insert("end", "0")
    buttonZero=ttk.Button(screenCalculator, text="0", command=actionZero, width=3).place(x=40, y=145)

    def actionDivide(): windowInputCalculatorView.insert("end", "÷")
    buttonDivide = ttk.Button(screenCalculator, text="÷", command=actionDivide, width=3).place(x=100, y=145)

    def actionOpenParenthesis(): windowInputCalculatorView.insert("end", "(")
    buttonOpenParenthesis=ttk.Button(screenCalculator, text="(", command=actionOpenParenthesis, width=3).place(x=130, y=145)

    def actionLog(): windowInputCalculatorView.insert("end", "log10(")
    buttonLog=ttk.Button(screenCalculator, text="log", command=actionLog, width=3).place(x=160, y=145)

    def storeAns(valPrint):
        valAnsView.clear()
        valAnsView.insert(0, valPrint)

    def actionDisplayCalculation():
        result = actionCalculate(windowInputCalculatorView)
        outputValue = result[0]
        errorLog = result[1]
        if errorLog == None:
            windowOutputCalculator.config(text = "")
            windowOutputCalculator.config(text = "= "+str(outputValue))
            storeAns(outputValue)
        else:
            debugger("printing error")
            windowOutputCalculator.config(text = "")
            messagebox.showerror(title="Error", message=str(errorLog))
            storeAns('0')
    buttonCalculate=ttk.Button(screenCalculator, text="=", command=actionDisplayCalculation, width=3).place(x=10, y=170)

    def actionAns(): windowInputCalculatorView.insert("end", "Ans")
    buttonAns=ttk.Button(screenCalculator, text="ans", command=actionAns, width=3).place(x=40, y=170)

    def actionAns(): windowInputCalculatorView.insert("end", "×10^")
    buttonAns=ttk.Button(screenCalculator, text="×10", command=actionAns, width=4).place(x=70, y=170)

    def actionPower(): windowInputCalculatorView.insert("end", "^")
    buttonPower=ttk.Button(screenCalculator, text="^", command=actionPower, width=3).place(x=100, y=170)

    def actionCloseParenthesis(): windowInputCalculatorView.insert("end", ")")
    buttonCloseParenthesis=ttk.Button(screenCalculator, text=")", command=actionCloseParenthesis, width=3).place(x=130, y=170)

    def actionSquareroot(): windowInputCalculatorView.insert("end", "√")
    buttonSquareroot=ttk.Button(screenCalculator, text="√", command=actionSquareroot, width=3).place(x=160, y=170)

    def actionOpenVariables(): screenVariablesDef(windowInputCalculatorView, actionCalculate)
    buttonVariables=ttk.Button(screenCalculator, text=langFile[chosenLang].screenVariables.Title, command=actionOpenVariables, width=15).place(x=200, y=120)
    
    def actionOpenFunctions(): screenFunctionsDef(windowInputCalculatorView)
    buttonFunctions=ttk.Button(screenCalculator, text=langFile[chosenLang].screenFunctions.Title, command=actionOpenFunctions, width=15).place(x=200, y=145)
    
    def actionOpenConstants(): screenConstantsDef(windowInputCalculatorView)
    buttonConstants=ttk.Button(screenCalculator, text=langFile[chosenLang].screenConstants.Title, command=actionOpenConstants, width=15).place(x=200, y=170)

    if loggedIn.getState():    
        def actionOpenLangPicker(): screenLangPickDef()
        buttonOpenLangPicker=ttk.Button(screenCalculator, text=langData.Buttons.ChangeLang, command=actionOpenLangPicker, width=15).place(x=200, y=235)

    if debugMode == True:
        def actionViewCheck():
            viewString = windowInputCalculatorView.get()
            debugger('------======------')
            debugger(f'View:{viewString}')
            debugger('------======------')
        buttonBackspace=ttk.Button(screenCalculator, text="Check", command=actionViewCheck, width=6).place(x=255, y=95)
    
    screenCalculator.mainloop()