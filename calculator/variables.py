valAnsView = [0, 1]; valAnsMath = [0, 1]

storeA = ['', '', 0, 0]; storeB = ['', '', 0, 0]; storeC = ['', '', 0, 0]; storeD = ['', '', 0, 0]; storeE = ['', '', 0, 0]; storeF = ['', '', 0, 0]; storeG = ['', '', 0, 0]
storeH = ['', '', 0, 0]; storeI = ['', '', 0, 0]; storeJ = ['', '', 0, 0]; storeK = ['', '', 0, 0]; storeL = ['', '', 0, 0]; storeM = ['', '', 0, 0]; storeN = ['', '', 0, 0]
storeO = ['', '', 0, 0]; storeP = ['', '', 0, 0]; storeQ = ['', '', 0, 0]; storeR = ['', '', 0, 0]; storeS = ['', '', 0, 0]; storeT = ['', '', 0, 0]; storeU = ['', '', 0, 0]
storeV = ['', '', 0, 0]; storeW = ['', '', 0, 0]; storeX = ['', '', 0, 0]; storeY = ['', '', 0, 0]; storeZ = ['', '', 0, 0]

insertListView = []
insertListMath = []

debug = False

def debugger(message):
    if debug == True:
        print(message)

def actionBaseDef(viewInput, viewLength, mathInput, mathLength, windowView, windowMath):
    windowView.insert("end", viewInput)
    windowMath.insert("end", mathInput)
    insertListView.append(viewLength)
    insertListMath.append(mathLength)
    debugger(f'View:{insertListView}')
    debugger(f'Math:{insertListMath}')