from tkinter import Frame, Button, Label, Text, filedialog, messagebox, DoubleVar
from tkinter import LEFT, RIGHT, TOP, X, DISABLED, NORMAL, BOTH
from img_process import identifyImg

class AppMain:
    def __init__(self, parent):
        self.frmMain = Frame(parent)
        self.frmMain.pack(side=LEFT)

        self.frmSide = Frame(parent)
        self.frmSide.pack(side=RIGHT, anchor='n')

        self.lblActions = Label(self.frmSide, text="Ações")
        self.btnIdentifyRune = Button(self.frmSide, text="Identificar Runa", command=self.identifyRune)
        self.btnAddRune = Button(self.frmSide, text="Adicionar Runa")
        self.btnShowRunes = Button(self.frmSide, text="Ver Runas")
        self.btnQuit = Button(self.frmSide, text="Sair", command=parent.quit)
        self.lblActions.pack()
        self.btnIdentifyRune.pack(fill=X)
        self.btnAddRune.pack(fill=X)
        self.btnShowRunes.pack(fill=X)
        self.btnQuit.pack(fill=X)

    def start(self):
        self.lblWelcomeTitle = Label(self.frmMain, text="Bem vindo!", font=("Arial Bold", 25))
        self.lblWelcomeText = Label(self.frmMain, text="Para analisar uma runa e descobrir o que ela significa, clique em Identificar Runa.", font=("Arial", 10))
        self.lblWelcomeTitle.pack()
        self.lblWelcomeText.pack()

    def identifyRune(self):
        for children in self.frmMain.winfo_children():
            children.destroy()

        self.frmButtons = Frame(self.frmMain)
        self.frmButtons.pack(anchor='nw')

        self.btnOpenFile = Button(self.frmButtons, text="Abrir arquivo", command=self.openFile)
        self.btnOpenFile.pack(side=LEFT)
        self.btnAnalyzeImg = Button(self.frmButtons, text="Analisar Imagem", command=self.analyzeImg, state=DISABLED)
        self.btnAnalyzeImg.pack(side=LEFT)


    def addRune(self):
        for children in self.frmMain.winfo_children():
            children.destroy()

    def showRunes(self):
        for children in self.frmMain.winfo_children():
            children.destroy()

    def openFile(self):
        filename = filedialog.askopenfilename()
        if filename == '':
            pass
        elif filename.split('.')[-1] != 'png':
            messagebox.showinfo("Arquivo inválido!", "A imagem deve ter extensão .png")
        else:
            self.lblFileText = Label(self.frmMain, text="Imagem selecionada: ")
            self.lblFileText.pack(side=LEFT)
            self.lblFile = Label(self.frmMain, text=filename)
            self.lblFile.pack(side=LEFT)
            self.btnAnalyzeImg["state"] = NORMAL

    def analyzeImg(self):
        pass