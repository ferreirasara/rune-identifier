from tkinter import Frame, Button, Label, Text, LEFT, RIGHT, CENTER, TOP, BOTTOM, X, N, RAISED, BOTH, S

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
        self.btnQuit = Button(self.sideFrame, text="Sair", command=parent.quit)
        self.lblActions.pack()
        self.btnIdentifyRune.pack(fill=X)
        self.btnAddRune.pack(fill=X)
        self.btnShowRunes.pack(fill=X)
        self.btnQuit.pack(fill=X)

    def start(self):
        self.lblWelcomeTitle = Label(self.mainFrame, text="Bem vindo!", font=("Arial Bold", 25))
        self.lblWelcomeText = Label(self.mainFrame, text="Para analisar uma runa e descobrir o que ela significa, clique em Identificar Runa.", font=("Arial", 10))
        self.lblWelcomeTitle.pack()
        self.lblWelcomeText.pack()

    def identifyRune(self):
        pass

    def addRune(self):
        pass

    def showRunes(self):
        pass