import tkinter
import tkinter.ttk
import tkinter.messagebox
import re

def screenLoginDef(calculatorDef, registerDef):

    screenLogin = tkinter.Tk()
    screenLogin.title("Login")
    screenLogin.geometry("200x145+550+200")

    tkinter.ttk.Label(screenLogin, text="Username").place(x=10, y=10)
    usernameEntry = tkinter.Entry(screenLogin, width=29)
    usernameEntry.place(x=10, y=35)
    usernameEntry.focus()

    tkinter.ttk.Label(screenLogin, text="Password").place(x=10, y=60)
    passwordEntry = tkinter.Entry(screenLogin, width=29, show="•")
    passwordEntry.place(x=10, y=85)

    def loadUser(username, password):
        loginFound = False

        with open("./calculator/accounts.json", 'r', encoding='utf-8') as file:
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
    
    def validateLogin():    
        attemptUsername = usernameEntry.get()
        attemptPassword = passwordEntry.get()

        if loadUser(attemptUsername, attemptPassword):
            tkinter.messagebox.showinfo(title="Beware", message="Calculator not fully operational, there may be bugs.")
            screenLogin.destroy()
            calculatorDef()
        else:
            tkinter.messagebox.showerror(title="Error", message="Username and password did not match.")
            usernameEntry.delete("0", "end")
            passwordEntry.delete("0", "end")
    buttonLogin = tkinter.ttk.Button(screenLogin, text="Log in", command=validateLogin, width=10).place(x=120, y=110)

    def actionRegister():
        screenLogin.destroy()
        registerDef(screenLoginDef)
    buttonRegister = tkinter.ttk.Button(screenLogin, text="Register", command=actionRegister, width=10).place(x=10, y=110)

    screenLogin.mainloop()