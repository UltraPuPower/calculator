import tkinter
import tkinter.ttk
import tkinter.messagebox
import re
import hashlib

from screenCalculator import screenCalculatorDef

from variables import loggedIn, filepath

from langControl import langFile

langData = langFile.screenLogin

def passwordHash(password):
   password_bytes = password.encode('utf-8')
   hash_object = hashlib.sha256(password_bytes)
   return hash_object.hexdigest()

def screenLoginDef(calculatorDef, welcomeDef):

    screenLogin = tkinter.Tk()
    screenLogin.title(langData.Title)
    screenLogin.geometry("200x145+550+200")

    tkinter.ttk.Label(screenLogin, text=langData.Labels.Name).place(x=10, y=10)
    usernameEntry = tkinter.Entry(screenLogin, width=29)
    usernameEntry.place(x=10, y=35)
    usernameEntry.focus()

    tkinter.ttk.Label(screenLogin, text=langData.Labels.Key).place(x=10, y=60)
    passwordEntry = tkinter.Entry(screenLogin, width=29, show="•")
    passwordEntry.place(x=10, y=85)

    def loadUser(username, password):
        loginFound = False
        userFound = False

        with open(f"{filepath}/accounts.json", 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            userNameLine = re.search(r'\s*"name": "(.*)".*', line)
            if userNameLine:
                compareName = userNameLine.group(1).strip()
                userKeyLine = re.search(r'\s*"password": "(.*)".*', lines[i+1])
                compareKey = userKeyLine.group(1).strip()
                if compareName == username and compareKey == passwordHash(password):
                    loginFound = True
                if compareName == username:
                    userFound = True

        return loginFound, userFound
    
    def validateLogin():    
        attemptUsername = usernameEntry.get()
        attemptPassword = passwordEntry.get()

        UserArr = loadUser(attemptUsername, attemptPassword)

        if UserArr[0]:
            tkinter.messagebox.showinfo(title=langData.Messageboxes.Success.Title, message=langData.Messageboxes.Success.Message)
            loggedIn.setState(True)
            loggedIn.setUser(attemptUsername)
            screenLogin.destroy()
            calculatorDef()
        elif UserArr[0] and UserArr[1]:
            tkinter.messagebox.showerror(title=langData.Messageboxes.Failure.Title, message=langData.Messageboxes.Failure.InvalidKey)
            passwordEntry.delete("0", "end")
        else:
            tkinter.messagebox.showerror(title=langData.Messageboxes.Failure.Title, message=langData.Messageboxes.Failure.NoAccount)
            usernameEntry.delete("0", "end")
            passwordEntry.delete("0", "end")
    buttonLogin = tkinter.ttk.Button(screenLogin, text=langData.Buttons.Login, command=validateLogin, width=10).place(x=120, y=110)

    def actionReturn():
        screenLogin.destroy()
        welcomeDef(screenCalculatorDef)
    buttonRegister = tkinter.ttk.Button(screenLogin, text=langData.Buttons.Return, command=actionReturn, width=10).place(x=10, y=110)

    screenLogin.mainloop()