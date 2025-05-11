import json

import re

loginCheck = False

alphabetPrinter = False

letterprinter = True

userDataTest = False

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
        print(f'            result = actionCalculate(); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; store{letter}.clear()')
        print(f'            if errorLog == None:')
        print(f'                store{letter}.insert(0, outputValue); store{letter}.insert(1, outputMath)')
        print(f'            else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))')
        print(f'            textShow{letter}.config(text = ""); textShow{letter}.config(text = "= "+str(store{letter}[0]))')
        print(f'        buttonStore{letter}=tkinter.ttk.Button(screenVariables, text="Ans={letter}", command=actionStore{letter}, width=7).place(x=10, y={10+25*i})')
        print(f'        def actionType{letter}():windowInputCalculator.insert("end", "{letter}")')
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