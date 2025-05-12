import tkinter

def screenConstantsDef(inputWindow):

    def actionPhysicsWarning():
        tkinter.messagebox.showinfo(title="Beware", message="Physics constants use unconventional symbols.\nThis means that you won't be able to type them with your keyboard.\nYou can use the buttons to insert them into the calculator.")
    actionPhysicsWarning()

    screenConstants = tkinter.Tk()
    screenConstants.title("Constants")
    screenConstants.geometry("300x665+1365+200")

    buttonPhysicsWarning=tkinter.ttk.Button(screenConstants, text="?", command=actionPhysicsWarning, width=1).place(x=105, y=45)

    tkinter.ttk.Label(screenConstants, text="Mathematical constants").place(x=5, y=5)
    def actionScreenConstantsExit():
        screenConstants.destroy()
    buttonScreenConstantsExit=tkinter.ttk.Button(screenConstants, text="Exit", command=actionScreenConstantsExit, width=5).place(x=250, y=0)

    def actionPi(): inputWindow.insert("end", "π")
    buttonPi=tkinter.ttk.Button(screenConstants, text="π", command=actionPi, width=3).place(x=5, y=20)

    def actionEuler(): inputWindow.insert("end", "e")
    buttonEuler=tkinter.ttk.Button(screenConstants, text="e", command=actionEuler, width=3).place(x=35, y=20)

    def actionTau(): inputWindow.insert("end", "τ")
    buttonTau=tkinter.ttk.Button(screenConstants, text="τ", command=actionTau, width=3).place(x=65, y=20)

    def actionPhi(): inputWindow.insert("end", "φ")
    buttonPhi=tkinter.ttk.Button(screenConstants, text="φ", command=actionPhi, width=3).place(x=95, y=20)

    tkinter.ttk.Label(screenConstants, text="Physics constants").place(x=5, y=45)

    def actionLight(): inputWindow.insert("end", "ϲ")
    buttonLight=tkinter.ttk.Button(screenConstants, text="ϲ", command=actionLight, width=3).place(x=5, y=65)
    tkinter.ttk.Label(screenConstants, text="Speed of Light").place(x=30, y=70)

    def actionPlanck(): inputWindow.insert("end", "Ꮒ")
    buttonPlanck=tkinter.ttk.Button(screenConstants, text="Ꮒ", command=actionPlanck, width=3).place(x=5, y=90)
    tkinter.ttk.Label(screenConstants, text="Planck Constant").place(x=30, y=95)

    def actionGravityConst(): inputWindow.insert("end", "Ꮐ")
    buttonGravityConst=tkinter.ttk.Button(screenConstants, text="Ꮐ", command=actionGravityConst, width=3).place(x=5, y=115)
    tkinter.ttk.Label(screenConstants, text="Gravitation Constant").place(x=30, y=120)

    def actionGravity(): inputWindow.insert("end", "ց")
    buttonGravity=tkinter.ttk.Button(screenConstants, text="ց", command=actionGravity, width=3).place(x=5, y=140)
    tkinter.ttk.Label(screenConstants, text="Gravitational Acceleration (NL)").place(x=30, y=145)

    def actionBoltzmann(): inputWindow.insert("end", "k")
    buttonBoltzmann=tkinter.ttk.Button(screenConstants, text="k", command=actionBoltzmann, width=3).place(x=5, y=165)
    tkinter.ttk.Label(screenConstants, text="Boltzmann Constant").place(x=30, y=170)

    def actionAvogadro(): inputWindow.insert("end", "Ｎ")
    buttonAvogadro=tkinter.ttk.Button(screenConstants, text="Ｎ", command=actionAvogadro, width=3).place(x=5, y=190)
    tkinter.ttk.Label(screenConstants, text="Avogadro Constant").place(x=30, y=195)

    def actionElementalChargeQuantum(): inputWindow.insert("end", "ҽ")
    buttonElementalChargeQuantum=tkinter.ttk.Button(screenConstants, text="ҽ", command=actionElementalChargeQuantum, width=3).place(x=5, y=215)
    tkinter.ttk.Label(screenConstants, text="Elementary Charge").place(x=30, y=220)

    screenConstants.mainloop()