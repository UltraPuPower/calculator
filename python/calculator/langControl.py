import re

from variables import language, filepath, loggedIn

from variables import debugger

def langFileSearch(lang):
    target = lang.lower()

    try:
        open(f"{filepath}\\lang\\{lang}.json")
        debugger(f"succes, language support for {lang} was found")
        return True
    except:
        debugger(f"Selected language ({lang}) is not available at {filepath}\\lang\\{lang}.json\nFalling back on English")
        return False

def loadUserLang(username):
    with open(f"{filepath}/accounts.json", 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        userNameLine = re.search(r'\s*"name": "(.*)".*', line)
        if userNameLine:
            compareName = userNameLine.group(1).strip()
            userLangLine = re.search(r'\s*"language": "(.*)".*', lines[i+2])
            if compareName == username:
                userLang = userLangLine.group(1).strip()

    return userLang

def setLangPref():
    if loggedIn.getState():
        langPref = loadUserLang(loggedIn.getUser())
        debugger("Loaded Lang preference")
        if langFileSearch(langPref):
            language.setLang(langPref)
            debugger("Lang preference integrated")
            return
        debugger("Lang preference not found")
        return
    debugger("Not logged in")

# by @LightWing at stackoverflow in "multi language support in python script"
from langData.english import english
from types import SimpleNamespace

class NestedNamespace(SimpleNamespace):
    def __init__(self, dictionary, **kwargs):
        super().__init__(**kwargs)
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.__setattr__(key, NestedNamespace(value))
            else:
                self.__setattr__(key, value)

langRData = {}
langRData.update({"English": NestedNamespace(english)})

setLangPref()

chosenLang = language.getLang()

langFile = langRData[chosenLang]