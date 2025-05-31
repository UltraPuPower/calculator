from variables import language, filepath, langSearch

from variables import debugger

def langFileSearch():
    calculatorLang = language.getLang().lower()

    try:
        open(f"{filepath}\\lang\\{calculatorLang}.json")
        debugger(f"succes, language support for {calculatorLang} was found")
    except:
        debugger(f"Selected language ({calculatorLang}) is not available at {filepath}\\lang\\{calculatorLang}.json")