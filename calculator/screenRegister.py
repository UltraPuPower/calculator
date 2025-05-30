import tkinter
import re
import hashlib
import pathlib

from screenCalculator import screenCalculatorDef

def passwordHash(password):
   password_bytes = password.encode('utf-8')
   hash_object = hashlib.sha256(password_bytes)
   return hash_object.hexdigest()

def screenRegisterDef(welcomeDef):
    filepath = pathlib.Path().absolute()

    screenRegister = tkinter.Tk()
    screenRegister.title("Register")
    screenRegister.geometry("200x195+550+200")

    tkinter.ttk.Label(screenRegister, text="Username").place(x=10, y=10)
    usernameEntry = tkinter.Entry(screenRegister, width=29)
    usernameEntry.place(x=10, y=35)
    usernameEntry.focus()

    tkinter.ttk.Label(screenRegister, text="Password").place(x=10, y=60)
    passwordEntry1 = tkinter.Entry(screenRegister, width=29, show="•")
    passwordEntry1.place(x=10, y=85)

    labelPassword2 = tkinter.ttk.Label(screenRegister, text="Repeat Password").place(x=10, y=110)
    passwordEntry2 = tkinter.Entry(screenRegister, width=29, show="•")
    passwordEntry2.place(x=10, y=135)

    def saveUser(username, password):
        with open(f"{filepath}/accounts.json") as f:
            userData= f.read()
            userData = userData[0:-18]
            userData += '\n        },\n        {'
            userData += f'\n        "name": "{username}",\n        "password": "{passwordHash(password)}"'
            userData += '\n        }\n    ]\n}'
            with open(f"{filepath}/accounts.json", 'w') as file:
                file.write(userData)


    def checkUserName(username):
        taken = False
        with open(f"{filepath}/accounts.json", 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            userNameLine = re.search(r'\s*"name": "(.*)".*', line)
            if userNameLine:
                compareName = userNameLine.group(1).strip()
                if compareName == username:
                    taken = True
        return taken

    def actionReturn():
        screenRegister.destroy()
        welcomeDef(screenCalculatorDef)
    buttonRegister = tkinter.ttk.Button(screenRegister, text="Return", command=actionReturn, width=10).place(x=10, y=160)
    
    def validateRegistry():
        attemptUsername = usernameEntry.get()
        attemptPassword1 = passwordEntry1.get()
        attemptPassword2 = passwordEntry2.get()
        if re.search(r"[^a-zA-Z0-9]", attemptUsername):
            tkinter.messagebox.showerror(title="Error", message="Invalid username. Only alphanumeric characters are allowed.")
            usernameEntry.delete("0", "end")
            passwordEntry1.delete("0", "end")
            passwordEntry2.delete("0", "end")
            return
        if re.search(r".*`.*", attemptPassword1) or re.search(r".*'.*", attemptPassword1) or re.search(r".*\".*", attemptPassword1):
            tkinter.messagebox.showerror(title="Error", message="Invalid Password. Using quotes or backticks is not allowed.")
            passwordEntry1.delete("0", "end")
            passwordEntry2.delete("0", "end")
            return
        if not attemptPassword1 == attemptPassword2:
            tkinter.messagebox.showerror(title="Error", message="Passwords are not identical.")
            passwordEntry1.delete("0", "end")
            passwordEntry2.delete("0", "end")
            return
        if checkUserName(attemptUsername):
            tkinter.messagebox.showerror(title="Error", message="Username is already taken.")
            usernameEntry.delete("0", "end")
            passwordEntry1.delete("0", "end")
            passwordEntry2.delete("0", "end")
            return
        saveUser(attemptUsername, attemptPassword1)
        tkinter.messagebox.showinfo(title="Success", message="You have registered successfully.\nYou will be returned to the welcome screen.")
        screenRegister.destroy()
        welcomeDef(screenCalculatorDef)
    buttonRegister = tkinter.ttk.Button(screenRegister, text="Register", command=validateRegistry, width=10).place(x=120, y=160)