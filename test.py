import tkinter
import tkinter.ttk

import re

debug = True

def debugger(message):
    if debug == True:
        print(message)

loginCheck = False

alphabetPrinter = False

letterprinter = True

userDataTest = False

registerInjection = False

mathRegistry = False

mathRegex = False

sinBug = False

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
        print(f'    textShow{letter} = tkinter.ttk.Label(screenVariables, text="= "+str(store{letter}[0]), font=["Verdana", "7"])')
        print(f'    textShow{letter}.place(x=85, y={15+25*i})')
        print(f'    def actionStore{letter}():')
        print(f'        result = actionCalculate(inputWindowView); outputValue = result[0]; errorLog = result[1]; store{letter}.clear()')
        print(f'        if errorLog == None: store{letter}.insert(0, outputValue)')
        print(f'        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))')
        print(f'        textShow{letter}.config(text = ""); textShow{letter}.config(text = "= "+str(store{letter}[0]))')
        print(f'    buttonStore{letter}=tkinter.ttk.Button(screenVariables, text="Ans={letter}", command=actionStore{letter}, width=7).place(x=10, y={10+25*i})')
        print(f'    def actionType{letter}(): inputWindowView.insert("end", "{letter}")')
        print(f'    buttonType{letter}=tkinter.ttk.Button(screenVariables, text="{letter}", command=actionType{letter}, width=2).place(x=60, y={10+25*i})')
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
            debugger(f'View:{insertListView}')
            debugger(f'Math:{insertListMath}')

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
                debugger("No more items to delete.")
    
        def actionBackspace():
            actionBackspacer(windowInputCalculatorView, insertListView)
            actionBackspacer(windowInputCalculatorMath, insertListMath)
            debugger(f'View:{insertListView}')
            debugger(f'Math:{insertListMath}')
        buttonBackspace=tkinter.ttk.Button(screen, text="del", command=actionBackspace, width=3).place(x=110, y=70)

        def actionViewCheck():
            viewString = windowInputCalculatorView.get()
            mathString = windowInputCalculatorMath.get()
            debugger('------======------')
            debugger(f'View:{viewString}')
            debugger(f'Math:{mathString}')
            debugger('------======------')
        buttonBackspace=tkinter.ttk.Button(screen, text="Check", command=actionViewCheck, width=5).place(x=110, y=110)

        screen.mainloop()

    windowTesting()

if mathRegex == True:
    operatorlist = ["*", "/", "+", "-", "(", ")"]
    txt = ["\u221a(2*2)", ")*\u221a(", "2*2"]

    def mathChecker():
        for line in txt:
            x = re.findall("(.)c(.)", line)
            if not x: return
            y = x[0]
            # print(y[0], y[1], type(y), len(y))
            if y[0] in operatorlist and y[1] in operatorlist:
                print(f"The c in {line} was found to be lightspeed")
            else:
                print(f"The c in {line} was found not to be lightspeed")

    def mathReplacer():

        def constantReplacer(line, target, replacement):
            cleanTarget = re.escape(target)
            line = re.sub(rf'([\+\-\*/\(]){cleanTarget}([\+\-\*/\)])', rf'\1{replacement}\2', line)
            line = re.sub(rf'([\+\-\*/\(]){cleanTarget}\b', rf'\1{replacement}', line)
            line = re.sub(rf'\b{cleanTarget}([\+\-\*/\)])', rf'{replacement}\1', line)
            line = re.sub(rf'\b{cleanTarget}\b', rf'{replacement}', line)
            return line
        
        print('------======------')
        print('√ => math.sqrt')
        for line in txt:
            line = line.replace('√', 'math.sqrt')
            #line = constantReplacer(line, '√', 'math.sqrt')
            print(line)
        
        # print('------======------')
        # print('cos => math.cos')
        # for line in txt:
        #     line = constantReplacer(line, 'cos', 'math.cos')
        #     print(line)
    
    mathReplacer()

if sinBug == True:
    def mathReplacer(input):

        savedInput = input

        def constantReplacerClean(line, target, replacement):
            cleanTarget = re.escape(target)
            line = re.sub(rf'([\+\-\*/\(]){cleanTarget}([\+\-\*/\)\(])', rf'\1{replacement}\2', line)
            line = re.sub(rf'\b{cleanTarget}([\+\-\*/\)])', rf'{replacement}\1', line)
            line = re.sub(rf'([\+\-\*/\(]){cleanTarget}\b', rf'\1{replacement}', line)
            line = re.sub(rf'\b{cleanTarget}\b', rf'{replacement}', line)
            return line

        def constantReplacer1(line, target, replacement):
            cleanTarget = re.escape(target)
            line = re.sub(rf'([\+\-\*/\(]){cleanTarget}([\+\-\*/\)\(])', rf'\1{replacement}\2-triggered first', line)
            line = re.sub(rf'\b{cleanTarget}([\+\-\*/\)])', rf'{replacement}\1-triggered second', line)
            line = re.sub(rf'([\+\-\*/\(]){cleanTarget}\b', rf'\1{replacement}-triggered third', line)
            line = re.sub(rf'\b{cleanTarget}\b', rf'{replacement}-triggered fourth', line)
            return line

        def constantReplacer2(line, target, replacement):
            cleanTarget = re.escape(target)
            line = re.sub(rf'(^|[\+\-\*/\(]){cleanTarget}([\+\-\*/\)\(]|$)', rf'\1{replacement}\2', line)
            return line
        
        #operators
        for filter in [{"t": '×', "r": '*'}, {"t": '^', "r": '**'}, {"t": '÷', "r": '/'}, {"t": '√', "r": 'math.sqrt'}]:
            input = input.replace(filter["t"], filter["r"])

        #advanced operators
        # add exception for log that allows numbers right after
        for filter in [{"t": 'sin', "r": 'math.sin'}, {"t": 'cos', "r": 'math.cos'}, {"t": 'tan', "r": 'math.tan'},
                    {"t": 'asin', "r": 'math.asin'}, {"t": 'acos', "r": 'math.acos'}, {"t": 'atan', "r": 'math.atan'},
                    {"t": 'asinh', "r": 'math.asinh'}, {"t": 'acosh', "r": 'math.acosh'}, {"t": 'atanh', "r": 'math.atanh'}]:
            input = constantReplacer2(input, filter["t"], filter["r"])

        #constants
        for filter in [{"t": 'π', "r": 'math.pi'}, {"t": 'e', "r": 'math.e'}, {"t": 'τ', "r": 'math.tau'}, {"t": 'φ', "r": '((1+math.sqrt(5))/2)'},
                    {"t": 'c', "r": '(2.99792458*10**8)'}, {"t": 'h', "r": '(6.62607015*10**-34)'}, {"t": 'G', "r": '(6.67430*10**-11)'},
                    {"t": 'g', "r": '(9.81)'}, {"t": 'k', "r": '(1.380649*10**-23)'}, {"t": 'N', "r": '(6.02214076*10**23)'},
                    {"t": 'eV', "r": '(1.602176634*10**-19)'}]:
            input = constantReplacerClean(input, filter["t"], filter["r"])

        idTest = False
        if re.search(r'.*math.cos.*', input):
            idTest = True
        debugger(f"converted [{savedInput}] into [{input}] => {idTest}")
        return(input)
    
    print('First:')
    mathReplacer("1+2×cos(π)+1")
    print('Two:')
    mathReplacer("cos(π)+1")
    print('Third:')
    mathReplacer("1+2×cos")
    print('Four:')
    mathReplacer("cos")