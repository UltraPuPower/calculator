import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

import re

from variables import langList, loggedIn, filepath, language

from variables import debugger

from langControl import langFile

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
            debugger(f'Adjusted User file generated')
            file.write(userData)


def screenLangPickDef():

    chosenLang = language.getLang()

    langData = langFile[chosenLang].screenLang

    screenLangPick = tkinter.Tk()
    screenLangPick.title(langData.Title)
    screenLangPick.geometry("150x200+600+300")

    def actionscreenLangPickExit():
        screenLangPick.destroy()
    buttonscreenLangPickExit=ttk.Button(screenLangPick, text=langData.Buttons.Exit, command=actionscreenLangPickExit, width=6).place(x=93, y=0)

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
                messagebox.showinfo(title=langData.Messageboxes.Failure.Title, message=langData.Messageboxes.Failure.Message)
                break
            saveLang(newLanguage)
            messagebox.showinfo(title=langData.Messageboxes.Success.Title, message=langData.Messageboxes.Success.Message)
            screenLangPick.destroy()
    buttonChoose = ttk.Button(screenLangPick, text=langData.Buttons.Choose, command=actionChoose)
    buttonChoose.place(x=25, y=130)

    screenLangPick.mainloop()