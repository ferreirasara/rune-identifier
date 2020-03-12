from tkinter import Frame, Button, Label, Text, LEFT, RIGHT, X, N

class AppMain:
    def __init__(self, parent):
        self.mainFrame = Frame(parent)
        self.mainFrame.pack(side=LEFT)

        self.sideFrame = Frame(parent)
        self.sideFrame.pack(side=RIGHT, anchor=N)


        self.lblActions = Label(self.sideFrame, text="Ações")
        self.btnIdentifyRune = Button(self.sideFrame, text="Identificar Runa")
        self.btnAddRune = Button(self.sideFrame, text="Adicionar Runa")
        self.btnShowRunes = Button(self.sideFrame, text="Ver Runas")
        self.lblActions.pack()
        self.btnIdentifyRune.pack(fill=X)
        self.btnAddRune.pack(fill=X)
        self.btnShowRunes.pack(fill=X)