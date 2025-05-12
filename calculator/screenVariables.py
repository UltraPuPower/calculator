import tkinter

from variables import storeA, storeB, storeC, storeD, storeE, storeF, storeG, storeH, storeI, storeJ, storeK, storeL, storeM, storeN, storeO, storeP, storeQ, storeR, storeS, storeT, storeU, storeV, storeW, storeX, storeY, storeZ

def screenVariablesDef(inputWindow, actionCalculate):
    screenVariables = tkinter.Tk()
    screenVariables.title("Variables")
    screenVariables.geometry("250x665+1065+200")

    def actionScreenVariablesExit():
        screenVariables.destroy()
    buttonScreenVariablesExit=tkinter.ttk.Button(screenVariables, text="Exit", command=actionScreenVariablesExit, width=5).place(x=200, y=0)

    textShowA = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowA.place(x=85, y=15)
    def actionStoreA():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeA.clear()
        if errorLog == None:
            storeA.insert(0, outputValue); storeA.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowA.config(text = ""); textShowA.config(text = "= "+str(storeA[0]))
    buttonStoreA=tkinter.ttk.Button(screenVariables, text="Ans=A", command=actionStoreA, width=7).place(x=10, y=10)
    def actionTypeA():inputWindow.insert("end", "A")
    buttonTypeA=tkinter.ttk.Button(screenVariables, text="A", command=actionTypeA, width=2).place(x=60, y=10)

    textShowB = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowB.place(x=85, y=40)
    def actionStoreB():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeB.clear()
        if errorLog == None:
            storeB.insert(0, outputValue); storeB.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowB.config(text = ""); textShowB.config(text = "= "+str(storeB[0]))
    buttonStoreB=tkinter.ttk.Button(screenVariables, text="Ans=B", command=actionStoreB, width=7).place(x=10, y=35)
    def actionTypeB():inputWindow.insert("end", "B")
    buttonTypeB=tkinter.ttk.Button(screenVariables, text="B", command=actionTypeB, width=2).place(x=60, y=35)

    textShowC = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowC.place(x=85, y=65)
    def actionStoreC():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeC.clear()
        if errorLog == None:
            storeC.insert(0, outputValue); storeC.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowC.config(text = ""); textShowC.config(text = "= "+str(storeC[0]))
    buttonStoreC=tkinter.ttk.Button(screenVariables, text="Ans=C", command=actionStoreC, width=7).place(x=10, y=60)
    def actionTypeC():inputWindow.insert("end", "C")
    buttonTypeC=tkinter.ttk.Button(screenVariables, text="C", command=actionTypeC, width=2).place(x=60, y=60)

    textShowD = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowD.place(x=85, y=90)
    def actionStoreD():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeD.clear()
        if errorLog == None:
            storeD.insert(0, outputValue); storeD.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowD.config(text = ""); textShowD.config(text = "= "+str(storeD[0]))
    buttonStoreD=tkinter.ttk.Button(screenVariables, text="Ans=D", command=actionStoreD, width=7).place(x=10, y=85)
    def actionTypeD():inputWindow.insert("end", "D")
    buttonTypeD=tkinter.ttk.Button(screenVariables, text="D", command=actionTypeD, width=2).place(x=60, y=85)

    textShowE = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowE.place(x=85, y=115)
    def actionStoreE():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeE.clear()
        if errorLog == None:
            storeE.insert(0, outputValue); storeE.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowE.config(text = ""); textShowE.config(text = "= "+str(storeE[0]))
    buttonStoreE=tkinter.ttk.Button(screenVariables, text="Ans=E", command=actionStoreE, width=7).place(x=10, y=110)
    def actionTypeE():inputWindow.insert("end", "E")
    buttonTypeE=tkinter.ttk.Button(screenVariables, text="E", command=actionTypeE, width=2).place(x=60, y=110)

    textShowF = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowF.place(x=85, y=140)
    def actionStoreF():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeF.clear()
        if errorLog == None:
            storeF.insert(0, outputValue); storeF.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowF.config(text = ""); textShowF.config(text = "= "+str(storeF[0]))
    buttonStoreF=tkinter.ttk.Button(screenVariables, text="Ans=F", command=actionStoreF, width=7).place(x=10, y=135)
    def actionTypeF():inputWindow.insert("end", "F")
    buttonTypeF=tkinter.ttk.Button(screenVariables, text="F", command=actionTypeF, width=2).place(x=60, y=135)

    textShowG = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowG.place(x=85, y=165)
    def actionStoreG():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeG.clear()
        if errorLog == None:
            storeG.insert(0, outputValue); storeG.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowG.config(text = ""); textShowG.config(text = "= "+str(storeG[0]))
    buttonStoreG=tkinter.ttk.Button(screenVariables, text="Ans=G", command=actionStoreG, width=7).place(x=10, y=160)
    def actionTypeG():inputWindow.insert("end", "G")
    buttonTypeG=tkinter.ttk.Button(screenVariables, text="G", command=actionTypeG, width=2).place(x=60, y=160)

    textShowH = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowH.place(x=85, y=190)
    def actionStoreH():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeH.clear()
        if errorLog == None:
            storeH.insert(0, outputValue); storeH.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowH.config(text = ""); textShowH.config(text = "= "+str(storeH[0]))
    buttonStoreH=tkinter.ttk.Button(screenVariables, text="Ans=H", command=actionStoreH, width=7).place(x=10, y=185)
    def actionTypeH():inputWindow.insert("end", "H")
    buttonTypeH=tkinter.ttk.Button(screenVariables, text="H", command=actionTypeH, width=2).place(x=60, y=185)

    textShowI = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowI.place(x=85, y=215)
    def actionStoreI():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeI.clear()
        if errorLog == None:
            storeI.insert(0, outputValue); storeI.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowI.config(text = ""); textShowI.config(text = "= "+str(storeI[0]))
    buttonStoreI=tkinter.ttk.Button(screenVariables, text="Ans=I", command=actionStoreI, width=7).place(x=10, y=210)
    def actionTypeI():inputWindow.insert("end", "I")
    buttonTypeI=tkinter.ttk.Button(screenVariables, text="I", command=actionTypeI, width=2).place(x=60, y=210)

    textShowJ = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowJ.place(x=85, y=240)
    def actionStoreJ():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeJ.clear()
        if errorLog == None:
            storeJ.insert(0, outputValue); storeJ.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowJ.config(text = ""); textShowJ.config(text = "= "+str(storeJ[0]))
    buttonStoreJ=tkinter.ttk.Button(screenVariables, text="Ans=J", command=actionStoreJ, width=7).place(x=10, y=235)
    def actionTypeJ():inputWindow.insert("end", "J")
    buttonTypeJ=tkinter.ttk.Button(screenVariables, text="J", command=actionTypeJ, width=2).place(x=60, y=235)

    textShowK = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowK.place(x=85, y=265)
    def actionStoreK():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeK.clear()
        if errorLog == None:
            storeK.insert(0, outputValue); storeK.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowK.config(text = ""); textShowK.config(text = "= "+str(storeK[0]))
    buttonStoreK=tkinter.ttk.Button(screenVariables, text="Ans=K", command=actionStoreK, width=7).place(x=10, y=260)
    def actionTypeK():inputWindow.insert("end", "K")
    buttonTypeK=tkinter.ttk.Button(screenVariables, text="K", command=actionTypeK, width=2).place(x=60, y=260)

    textShowL = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowL.place(x=85, y=290)
    def actionStoreL():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeL.clear()
        if errorLog == None:
            storeL.insert(0, outputValue); storeL.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowL.config(text = ""); textShowL.config(text = "= "+str(storeL[0]))
    buttonStoreL=tkinter.ttk.Button(screenVariables, text="Ans=L", command=actionStoreL, width=7).place(x=10, y=285)
    def actionTypeL():inputWindow.insert("end", "L")
    buttonTypeL=tkinter.ttk.Button(screenVariables, text="L", command=actionTypeL, width=2).place(x=60, y=285)

    textShowM = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowM.place(x=85, y=315)
    def actionStoreM():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeM.clear()
        if errorLog == None:
            storeM.insert(0, outputValue); storeM.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowM.config(text = ""); textShowM.config(text = "= "+str(storeM[0]))
    buttonStoreM=tkinter.ttk.Button(screenVariables, text="Ans=M", command=actionStoreM, width=7).place(x=10, y=310)
    def actionTypeM():inputWindow.insert("end", "M")
    buttonTypeM=tkinter.ttk.Button(screenVariables, text="M", command=actionTypeM, width=2).place(x=60, y=310)

    textShowN = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowN.place(x=85, y=340)
    def actionStoreN():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeN.clear()
        if errorLog == None:
            storeN.insert(0, outputValue); storeN.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowN.config(text = ""); textShowN.config(text = "= "+str(storeN[0]))
    buttonStoreN=tkinter.ttk.Button(screenVariables, text="Ans=N", command=actionStoreN, width=7).place(x=10, y=335)
    def actionTypeN():inputWindow.insert("end", "N")
    buttonTypeN=tkinter.ttk.Button(screenVariables, text="N", command=actionTypeN, width=2).place(x=60, y=335)

    textShowO = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowO.place(x=85, y=365)
    def actionStoreO():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeO.clear()
        if errorLog == None:
            storeO.insert(0, outputValue); storeO.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowO.config(text = ""); textShowO.config(text = "= "+str(storeO[0]))
    buttonStoreO=tkinter.ttk.Button(screenVariables, text="Ans=O", command=actionStoreO, width=7).place(x=10, y=360)
    def actionTypeO():inputWindow.insert("end", "O")
    buttonTypeO=tkinter.ttk.Button(screenVariables, text="O", command=actionTypeO, width=2).place(x=60, y=360)

    textShowP = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowP.place(x=85, y=390)
    def actionStoreP():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeP.clear()
        if errorLog == None:
            storeP.insert(0, outputValue); storeP.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowP.config(text = ""); textShowP.config(text = "= "+str(storeP[0]))
    buttonStoreP=tkinter.ttk.Button(screenVariables, text="Ans=P", command=actionStoreP, width=7).place(x=10, y=385)
    def actionTypeP():inputWindow.insert("end", "P")
    buttonTypeP=tkinter.ttk.Button(screenVariables, text="P", command=actionTypeP, width=2).place(x=60, y=385)

    textShowQ = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowQ.place(x=85, y=415)
    def actionStoreQ():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeQ.clear()
        if errorLog == None:
            storeQ.insert(0, outputValue); storeQ.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowQ.config(text = ""); textShowQ.config(text = "= "+str(storeQ[0]))
    buttonStoreQ=tkinter.ttk.Button(screenVariables, text="Ans=Q", command=actionStoreQ, width=7).place(x=10, y=410)
    def actionTypeQ():inputWindow.insert("end", "Q")
    buttonTypeQ=tkinter.ttk.Button(screenVariables, text="Q", command=actionTypeQ, width=2).place(x=60, y=410)

    textShowR = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowR.place(x=85, y=440)
    def actionStoreR():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeR.clear()
        if errorLog == None:
            storeR.insert(0, outputValue); storeR.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowR.config(text = ""); textShowR.config(text = "= "+str(storeR[0]))
    buttonStoreR=tkinter.ttk.Button(screenVariables, text="Ans=R", command=actionStoreR, width=7).place(x=10, y=435)
    def actionTypeR():inputWindow.insert("end", "R")
    buttonTypeR=tkinter.ttk.Button(screenVariables, text="R", command=actionTypeR, width=2).place(x=60, y=435)

    textShowS = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowS.place(x=85, y=465)
    def actionStoreS():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeS.clear()
        if errorLog == None:
            storeS.insert(0, outputValue); storeS.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowS.config(text = ""); textShowS.config(text = "= "+str(storeS[0]))
    buttonStoreS=tkinter.ttk.Button(screenVariables, text="Ans=S", command=actionStoreS, width=7).place(x=10, y=460)
    def actionTypeS():inputWindow.insert("end", "S")
    buttonTypeS=tkinter.ttk.Button(screenVariables, text="S", command=actionTypeS, width=2).place(x=60, y=460)

    textShowT = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowT.place(x=85, y=490)
    def actionStoreT():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeT.clear()
        if errorLog == None:
            storeT.insert(0, outputValue); storeT.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowT.config(text = ""); textShowT.config(text = "= "+str(storeT[0]))
    buttonStoreT=tkinter.ttk.Button(screenVariables, text="Ans=T", command=actionStoreT, width=7).place(x=10, y=485)
    def actionTypeT():inputWindow.insert("end", "T")
    buttonTypeT=tkinter.ttk.Button(screenVariables, text="T", command=actionTypeT, width=2).place(x=60, y=485)

    textShowU = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowU.place(x=85, y=515)
    def actionStoreU():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeU.clear()
        if errorLog == None:
            storeU.insert(0, outputValue); storeU.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowU.config(text = ""); textShowU.config(text = "= "+str(storeU[0]))
    buttonStoreU=tkinter.ttk.Button(screenVariables, text="Ans=U", command=actionStoreU, width=7).place(x=10, y=510)
    def actionTypeU():inputWindow.insert("end", "U")
    buttonTypeU=tkinter.ttk.Button(screenVariables, text="U", command=actionTypeU, width=2).place(x=60, y=510)

    textShowV = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowV.place(x=85, y=540)
    def actionStoreV():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeV.clear()
        if errorLog == None:
            storeV.insert(0, outputValue); storeV.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowV.config(text = ""); textShowV.config(text = "= "+str(storeV[0]))
    buttonStoreV=tkinter.ttk.Button(screenVariables, text="Ans=V", command=actionStoreV, width=7).place(x=10, y=535)
    def actionTypeV():inputWindow.insert("end", "V")
    buttonTypeV=tkinter.ttk.Button(screenVariables, text="V", command=actionTypeV, width=2).place(x=60, y=535)

    textShowW = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowW.place(x=85, y=565)
    def actionStoreW():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeW.clear()
        if errorLog == None:
            storeW.insert(0, outputValue); storeW.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowW.config(text = ""); textShowW.config(text = "= "+str(storeW[0]))
    buttonStoreW=tkinter.ttk.Button(screenVariables, text="Ans=W", command=actionStoreW, width=7).place(x=10, y=560)
    def actionTypeW():inputWindow.insert("end", "W")
    buttonTypeW=tkinter.ttk.Button(screenVariables, text="W", command=actionTypeW, width=2).place(x=60, y=560)

    textShowX = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowX.place(x=85, y=590)
    def actionStoreX():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeX.clear()
        if errorLog == None:
            storeX.insert(0, outputValue); storeX.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowX.config(text = ""); textShowX.config(text = "= "+str(storeX[0]))
    buttonStoreX=tkinter.ttk.Button(screenVariables, text="Ans=X", command=actionStoreX, width=7).place(x=10, y=585)
    def actionTypeX():inputWindow.insert("end", "X")
    buttonTypeX=tkinter.ttk.Button(screenVariables, text="X", command=actionTypeX, width=2).place(x=60, y=585)

    textShowY = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowY.place(x=85, y=615)
    def actionStoreY():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeY.clear()
        if errorLog == None:
            storeY.insert(0, outputValue); storeY.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowY.config(text = ""); textShowY.config(text = "= "+str(storeY[0]))
    buttonStoreY=tkinter.ttk.Button(screenVariables, text="Ans=Y", command=actionStoreY, width=7).place(x=10, y=610)
    def actionTypeY():inputWindow.insert("end", "Y")
    buttonTypeY=tkinter.ttk.Button(screenVariables, text="Y", command=actionTypeY, width=2).place(x=60, y=610)

    textShowZ = tkinter.ttk.Label(screenVariables, text="", font=["Verdana", "7"])
    textShowZ.place(x=85, y=640)
    def actionStoreZ():
        result = actionCalculate(inputWindow.get()); outputValue = result[0]; outputMath = result[1]; errorLog = result[2]; storeZ.clear()
        if errorLog == None:
            storeZ.insert(0, outputValue); storeZ.insert(1, outputMath)
        else: tkinter.messagebox.showerror(title="Error", message=str(errorLog))
        textShowZ.config(text = ""); textShowZ.config(text = "= "+str(storeZ[0]))
    buttonStoreZ=tkinter.ttk.Button(screenVariables, text="Ans=Z", command=actionStoreZ, width=7).place(x=10, y=635)
    def actionTypeZ():inputWindow.insert("end", "Z")
    buttonTypeZ=tkinter.ttk.Button(screenVariables, text="Z", command=actionTypeZ, width=2).place(x=60, y=635)
    
    screenVariables.mainloop()