import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

import re

from variables import language, langList, loggedIn, filepath

from variables import debugger

def saveLang(language):
    if loggedIn.getState():
        username = loggedIn.getUser()
        with open(f"{filepath}/accounts.json", 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            userNameLine = re.search(fr'\s*"name": "{username}".*', line)
            if userNameLine:
                lines[i+2] = f'        "language": "{language}"\n'
                break
        
        with open(f"{filepath}/accounts.json", 'w') as file:
            userData = ""
            for line in lines:
                userData += line
            debugger(f'New User file:\n{userData}')
            file.write(userData)


def screenLangPickDef():

    screenLangPick = tkinter.Tk()
    screenLangPick.title("Select Language")
    screenLangPick.geometry("150x200+600+300")

    def actionscreenLangPickExit():
        screenLangPick.destroy()
    buttonscreenLangPickExit=ttk.Button(screenLangPick, text="Exit", command=actionscreenLangPickExit, width=5).place(x=98, y=0)

    optionString = ""
    i = 0

    langOptions = tkinter.Listbox(screenLangPick, selectmode='single', width=20, height=6)
    langOptions.place(x=13, y=25)

    while i < len(langList):
        langOptions.insert(i, langList[i])
        optionString += f"{langList[i]} "
        i += 1
    debugger(f"Available languages: ({optionString})")

    def actionChoose():
        selection = langOptions.curselection()
        for i in selection:
            newLanguage = langOptions.get(i)
            if not newLanguage in langList:
                messagebox.showinfo(title="Invalid Entry", message="You entered an unsupported language.\nIf you believe this to be an error, contact the developers.")
                break
            saveLang(newLanguage)
            messagebox.showinfo(title="Success", message=f"You changed your language to {language.getLang()}\nRestart the calculator for this to take effect.")
            screenLangPick.destroy()
    buttonChoose = ttk.Button(screenLangPick, text="Choose selected", command=actionChoose)
    buttonChoose.place(x=25, y=130)

    screenLangPick.mainloop()