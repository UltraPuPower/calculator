import tkinter
import tkinter.ttk

import re

debugger = True

def debug(message):
    if debugger == True:
        print(message)

loginCheck = False

alphabetPrinter = False

letterprinter = True

userDataTest = False

registerInjection = False

mathRegistry = False

if loginCheck == True:
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
    print(loginCheck('Admin', 'P@$$w0rd'))


if alphabetPrinter == True:
    text = '['
    for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        text += f"{{'mesh': '{letter}', 'new': str({letter}[1])}}"
        if not letter == 'Z':
            text += ', '
    text += ']'
    print(text)


if letterprinter == True:
    i = 0
    nextRow = False
    for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        print(f'        textShow{letter} = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])')
        print(f'        textShow{letter}.place(x=85, y={15+25*i})')
        print(f'        def actionStore{letter}():')
        print(f'            result = actionCalculate(inputWindowMath); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; store{letter}.clear()')
        print(f'            if errorLog == None:')
        print(f'                store{letter}.insert(0, outputValue); store{letter}.insert(1, outputMath)')
        print(f'            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))')
        print(f'            textShow{letter}.config(text = ""); textShow{letter}.config(text = "= "+str(store{letter}[0]))')
        print(f'        buttonStore{letter}=tkinter.ttk.Button(screenVariables, text="Ans={letter}", command=actionStore{letter}, width=7).place(x=10, y={10+25*i})')
        print(f'        def actionType{letter}(): actionBase("{letter}", 1, store{letter}[0], len(store{letter}[0]))')
        print(f'        buttonType{letter}=tkinter.ttk.Button(screenVariables, text="{letter}", command=actionType{letter}, width=2).place(x=60, y={10+25*i})')
        print(f'')
        i += 1

if userDataTest == True:
    users = [
        {'userName': 'Admin', 'userPassword': 'P@$$w0rd'},
        {'userName': 'User1', 'userPassword': 'password'}
    ]

    def saveUser(username, password):
        with open("accounts.json") as f:
            userData= f.read()
            userData = userData[0:-18]
            userData += '\n        },\n        {'
            userData += f'\n        "name": "{username}",\n        "password": "{password}"'
            userData += '\n        }\n    ]\n}'
            with open('accounts.json', 'w') as file:
                file.write(userData)

    def loadUser(username, password):
        loginFound = False

        with open("accounts.json", 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            userNameLine = re.search(r'\s*"name": "(.*)".*', line)
            if userNameLine:
                compareName = userNameLine.group(1).strip()
                userKeyLine = re.search(r'\s*"password": "(.*)".*', lines[i+1])
                compareKey = userKeyLine.group(1).strip()
                if compareName == username and compareKey == password:
                    loginFound = True

        return loginFound
    
    print(loadUser('Admin', 'P@$$w0rd'))

if registerInjection == True:
    y = input("Enter your username: ")
    print(y)
    if re.search(r"[^a-zA-Z0-9]", y):
        print("Invalid username. Only alphanumeric characters are allowed.")
    else:
        print("Valid username.")

if mathRegistry == True:
    def windowTesting():
        insertListView = []
        insertListMath = []

        screen = tkinter.Tk()
        screen.title("Math Registry")
        screen.geometry("300x665+200+200")
        screen.configure(bg="white")

        windowInputCalculatorMath = tkinter.Entry(screen, width=29)
        windowInputCalculatorMath.place(x=10, y=10)

        windowInputCalculatorView = tkinter.Entry(screen, width=29)
        windowInputCalculatorView.place(x=10, y=10)

        def actionBase(viewInput, viewLength, mathInput, mathLength):
            windowInputCalculatorView.insert("end", viewInput)
            windowInputCalculatorMath.insert("end", mathInput)
            insertListView.append(viewLength)
            insertListMath.append(mathLength)
            debug(f'View:{insertListView}')
            debug(f'Math:{insertListMath}')

        def actionPi(): actionBase("π", 1, "math.pi", 7)
        buttonPi = tkinter.ttk.Button(screen, text="π", command=actionPi, width=3).place(x=10, y=120)

        def actionMultiply(): actionBase("×", 1, "*", 1)
        buttonMultiply = tkinter.ttk.Button(screen, text="*", command=actionMultiply, width=3).place(x=85, y=95)
        
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
                debug("No more items to delete.")
    
        def actionBackspace():
            actionBackspacer(windowInputCalculatorView, insertListView)
            actionBackspacer(windowInputCalculatorMath, insertListMath)
            debug(f'View:{insertListView}')
            debug(f'Math:{insertListMath}')
        buttonBackspace=tkinter.ttk.Button(screen, text="del", command=actionBackspace, width=3).place(x=110, y=70)

        def actionViewCheck():
            viewString = windowInputCalculatorView.get()
            mathString = windowInputCalculatorMath.get()
            debug('------======------')
            debug(f'View:{viewString}')
            debug(f'Math:{mathString}')
            debug('------======------')
        buttonBackspace=tkinter.ttk.Button(screen, text="Check", command=actionViewCheck, width=5).place(x=110, y=110)

        screen.mainloop()

    windowTesting()