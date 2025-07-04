import tkinter

from langControl import langFile

langData = langFile.screenConstants

def screenConstantsDef(inputWindowView):

    screenConstants = tkinter.Tk()
    screenConstants.title(langData.Title)
    screenConstants.geometry("300x665+1160+200")

    # def actionPhysicsWarning():
    #     tkinter.messagebox.showinfo(title="Beware", message="Physics constants use unconventional symbols.\nThis means that you won't be able to type them with your keyboard.\nYou can use the buttons to insert them into the calculator.")
    # actionPhysicsWarning()

    # buttonPhysicsWarning=tkinter.ttk.Button(screenConstants, text="?", command=actionPhysicsWarning, width=1).place(x=105, y=45)

    tkinter.ttk.Label(screenConstants, text=langData.Labels.Math).place(x=5, y=5)
    def actionScreenConstantsExit():
        screenConstants.destroy()
    buttonScreenConstantsExit=tkinter.ttk.Button(screenConstants, text=langData.Buttons.Exit, command=actionScreenConstantsExit, width=5).place(x=250, y=0)

    def actionPi(): inputWindowView.insert("end", "π")
    buttonPi=tkinter.ttk.Button(screenConstants, text="π", command=actionPi, width=3).place(x=5, y=20)

    def actionEuler(): inputWindowView.insert("end", "e")
    buttonEuler=tkinter.ttk.Button(screenConstants, text="e", command=actionEuler, width=3).place(x=35, y=20)

    def actionTau(): inputWindowView.insert("end", "τ")
    buttonTau=tkinter.ttk.Button(screenConstants, text="τ", command=actionTau, width=3).place(x=65, y=20)

    def actionPhi(): inputWindowView.insert("end", "φ")
    buttonPhi=tkinter.ttk.Button(screenConstants, text="φ", command=actionPhi, width=3).place(x=95, y=20)

    tkinter.ttk.Label(screenConstants, text=langData.Labels.Physics).place(x=5, y=45)

    def actionLight(): inputWindowView.insert("end", "c")
    buttonLight=tkinter.ttk.Button(screenConstants, text="c", command=actionLight, width=3).place(x=5, y=65)
    tkinter.ttk.Label(screenConstants, text=langData.Labels.Lightspeed).place(x=35, y=70)

    def actionPlanck(): inputWindowView.insert("end", "h")
    buttonPlanck=tkinter.ttk.Button(screenConstants, text="h", command=actionPlanck, width=3).place(x=5, y=90)
    tkinter.ttk.Label(screenConstants, text=langData.Labels.Planck).place(x=35, y=95)

    def actionGravityConst(): inputWindowView.insert("end", "G")
    buttonGravityConst=tkinter.ttk.Button(screenConstants, text="G", command=actionGravityConst, width=3).place(x=5, y=115)
    tkinter.ttk.Label(screenConstants, text=langData.Labels.GravConst).place(x=35, y=120)

    def actionGravity(): inputWindowView.insert("end", "g")
    buttonGravity=tkinter.ttk.Button(screenConstants, text="g", command=actionGravity, width=3).place(x=5, y=140)
    tkinter.ttk.Label(screenConstants, text=langData.Labels.Gravity).place(x=35, y=145)

    def actionBoltzmann(): inputWindowView.insert("end", "k")
    buttonBoltzmann=tkinter.ttk.Button(screenConstants, text="k", command=actionBoltzmann, width=3).place(x=5, y=165)
    tkinter.ttk.Label(screenConstants, text=langData.Labels.Boltzmann).place(x=35, y=170)

    def actionAvogadro(): inputWindowView.insert("end", "Na")
    buttonAvogadro=tkinter.ttk.Button(screenConstants, text="Na", command=actionAvogadro, width=3).place(x=5, y=190)
    tkinter.ttk.Label(screenConstants, text=langData.Labels.Avogadro).place(x=35, y=195)

    def actionElementalChargeQuantum(): inputWindowView.insert("end", "eV")
    buttonElementalChargeQuantum=tkinter.ttk.Button(screenConstants, text="eV", command=actionElementalChargeQuantum, width=3).place(x=5, y=215)
    tkinter.ttk.Label(screenConstants, text=langData.Labels.ElemCharge).place(x=35, y=220)

    screenConstants.mainloop()