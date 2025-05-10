loginCheck = False

alphabetPrinter = True

letterprinter = False

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
    for letter in ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        i += 1
        if letter == 'N':
            nextRow = True
            i = 0
        if nextRow == False:
            print(f'    textShow{letter} = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])')
            print(f'    textShow{letter}.place(x=85, y={340+25*i})')
            print(f'    def actionStore{letter}(): storeVarGenerator({letter})()')
            print(f'    buttonStore{letter}=tkinter.ttk.Button(screenCalculator, text="Ans={letter}", command=actionStore{letter}, width=7).place(x=10, y={335+25*i})')
            print(f'    def actionType{letter}():windowInputCalculator.insert("end", "{letter}")')
            print(f'    buttonType{letter}=tkinter.ttk.Button(screenCalculator, text="{letter}", command=actionType{letter}, width=2).place(x=60, y={335+25*i})')
            print(f'')
        if nextRow == True:
            print(f'    textShow{letter} = tkinter.ttk.Label(screenCalculator, text="", font=["Verdana", "7"])')
            print(f'    textShow{letter}.place(x=275, y={215+25*i})')
            print(f'    def actionStore{letter}(): storeVarGenerator({letter})()')
            print(f'    buttonStore{letter}=tkinter.ttk.Button(screenCalculator, text="Ans={letter}", command=actionStore{letter}, width=7).place(x=200, y={210+25*i})')
            print(f'    def actionType{letter}():windowInputCalculator.insert("end", "{letter}")')
            print(f'    buttonType{letter}=tkinter.ttk.Button(screenCalculator, text="{letter}", command=actionType{letter}, width=2).place(x=250, y={210+25*i})')
            print(f'')