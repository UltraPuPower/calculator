import tkinter

from variables import actionBaseDef

def screenConstantsDef(inputWindowView, inputWindowMath):

    def actionBase(viewInput, viewLength, mathInput, mathLength): actionBaseDef(viewInput, viewLength, mathInput, mathLength, inputWindowView, inputWindowMath)

    screenConstants = tkinter.Tk()
    screenConstants.title("Constants")
    screenConstants.geometry("300x665+1365+200")

    # def actionPhysicsWarning():
    #     tkinter.messagebox.showinfo(title="Beware", message="Physics constants use unconventional symbols.\nThis means that you won't be able to type them with your keyboard.\nYou can use the buttons to insert them into the calculator.")
    # actionPhysicsWarning()

    # buttonPhysicsWarning=tkinter.ttk.Button(screenConstants, text="?", command=actionPhysicsWarning, width=1).place(x=105, y=45)

    tkinter.ttk.Label(screenConstants, text="Mathematical constants").place(x=5, y=5)
    def actionScreenConstantsExit():
        screenConstants.destroy()
    buttonScreenConstantsExit=tkinter.ttk.Button(screenConstants, text="Exit", command=actionScreenConstantsExit, width=5).place(x=250, y=0)

    def actionPi(): actionBase("π", 1, "math.pi", 7)
    buttonPi=tkinter.ttk.Button(screenConstants, text="π", command=actionPi, width=3).place(x=5, y=20)

    def actionEuler(): actionBase("e", 1, "math.e", 6)
    buttonEuler=tkinter.ttk.Button(screenConstants, text="e", command=actionEuler, width=3).place(x=35, y=20)

    def actionTau(): actionBase("τ", 1, "math.tau", 8)
    buttonTau=tkinter.ttk.Button(screenConstants, text="τ", command=actionTau, width=3).place(x=65, y=20)

    def actionPhi(): actionBase("φ", 1, "((1+math.sqrt(5))/2)", 20)
    buttonPhi=tkinter.ttk.Button(screenConstants, text="φ", command=actionPhi, width=3).place(x=95, y=20)

    tkinter.ttk.Label(screenConstants, text="Physics constants").place(x=5, y=45)

    def actionLight(): actionBase("c", 1, "(2.99792458*10**8)", 18)
    buttonLight=tkinter.ttk.Button(screenConstants, text="c", command=actionLight, width=3).place(x=5, y=65)
    tkinter.ttk.Label(screenConstants, text="Speed of Light").place(x=30, y=70)

    def actionPlanck(): actionBase("h", 1, "(6.62607015*10**-34)", 20)
    buttonPlanck=tkinter.ttk.Button(screenConstants, text="h", command=actionPlanck, width=3).place(x=5, y=90)
    tkinter.ttk.Label(screenConstants, text="Planck Constant").place(x=30, y=95)

    def actionGravityConst(): actionBase("G", 1, "(6.67430*10**-11)", 17)
    buttonGravityConst=tkinter.ttk.Button(screenConstants, text="G", command=actionGravityConst, width=3).place(x=5, y=115)
    tkinter.ttk.Label(screenConstants, text="Gravitation Constant").place(x=30, y=120)

    def actionGravity(): actionBase("g", 1, "(9.81)", 6)
    buttonGravity=tkinter.ttk.Button(screenConstants, text="g", command=actionGravity, width=3).place(x=5, y=140)
    tkinter.ttk.Label(screenConstants, text="Gravitational Acceleration (NL)").place(x=30, y=145)

    def actionBoltzmann(): actionBase("k", 1, "(1.380649*10**-23)", 18)
    buttonBoltzmann=tkinter.ttk.Button(screenConstants, text="k", command=actionBoltzmann, width=3).place(x=5, y=165)
    tkinter.ttk.Label(screenConstants, text="Boltzmann Constant").place(x=30, y=170)

    def actionAvogadro(): actionBase("N", 1, "(6.02214076*10**23)", 19)
    buttonAvogadro=tkinter.ttk.Button(screenConstants, text="N", command=actionAvogadro, width=3).place(x=5, y=190)
    tkinter.ttk.Label(screenConstants, text="Avogadro Constant").place(x=30, y=195)

    def actionElementalChargeQuantum(): actionBase("eV", 2, "(1.602176634*10**-19)", 21)
    buttonElementalChargeQuantum=tkinter.ttk.Button(screenConstants, text="eV", command=actionElementalChargeQuantum, width=3).place(x=5, y=215)
    tkinter.ttk.Label(screenConstants, text="Elementary Charge").place(x=30, y=220)

    screenConstants.mainloop()