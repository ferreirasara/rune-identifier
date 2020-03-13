from tkinter import Frame, Button, Label, Text, filedialog, messagebox, DoubleVar
from tkinter import LEFT, RIGHT, TOP, X, DISABLED, NORMAL, BOTH, HORIZONTAL
from tkinter.ttk import Progressbar, LabelFrame, Separator
from img_process import identifyImg
from db_util import createDB

class AppMain:
    def __init__(self, parent):
        createDB()
        # Cria o frame principal
        self.frmMain = Frame(parent)
        self.frmMain.pack(side=LEFT, anchor='n')

        # Cria o frame lateral
        self.frmSide = Frame(parent)
        self.frmSide.pack(side=RIGHT, anchor='n')

        # Adiciona os botões ao frame lateral
        self.lblfrmActions = LabelFrame(self.frmSide, text="Ações:")
        self.lblfrmActions.pack()
        self.btnIdentifyRune = Button(self.lblfrmActions, text="Identificar Runa", command=self.identifyRune)
        self.btnAddRune = Button(self.lblfrmActions, text="Adicionar Runa", command=self.addRune)
        self.btnShowRunes = Button(self.lblfrmActions, text="Ver Runas", command=self.showRunes)
        self.btnQuit = Button(self.lblfrmActions, text="Sair", command=parent.quit)
        self.btnIdentifyRune.pack(fill=X)
        self.btnAddRune.pack(fill=X)
        self.btnShowRunes.pack(fill=X)
        self.btnQuit.pack(fill=X)

    def start(self):
        # Adiciona os textos iniciais à tela principal
        self.lblTitle = Label(self.frmMain, text="Bem vindo!", font=("Arial Bold", 25))
        self.lblWelcomeText = Label(self.frmMain, text="Para analisar uma runa e descobrir o que ela significa, clique em Identificar Runa.", font=("Arial", 10))
        self.lblTitle.pack()
        self.lblWelcomeText.pack()

    def destroyChildrenFrmMain(self):
        # Destroi todos os widgets filhos do frame principal
        for children in self.frmMain.winfo_children():
            children.destroy()

    def identifyRune(self):
        self.destroyChildrenFrmMain()

        # Titulo da tela
        self.setTitle("Identificar Runa")

        # Cria um frame para os widgets
        self.frmButtons = Frame(self.frmMain)
        self.frmButtons.pack(anchor='nw')

        # Cria os widgets
        self.btnOpenFile = Button(self.frmButtons, text="Abrir arquivo", command=self.openFile)
        self.btnAnalyzeImg = Button(self.frmButtons, text="Analisar Imagem", command=self.analyzeImg, state=DISABLED)
        self.btnOpenFile.pack(side=LEFT)
        self.btnAnalyzeImg.pack(side=LEFT)

    def addRune(self):
        self.destroyChildrenFrmMain()

        # Titulo da tela
        self.setTitle("Adicionar Runa")

        # Cria um frame para os widgets
        self.frmButtons = Frame(self.frmMain)
        self.frmButtons.pack(anchor='nw')

        # Cria os widgets
        self.btnOpenFile = Button(self.frmButtons, text="Abrir arquivo", command=self.openFile)
        self.btnAddImg = Button(self.frmButtons, text="Adicionar Runa", command=self.addImg, state=DISABLED)
        self.btnOpenFile.pack(side=LEFT)
        self.btnAddImg.pack(side=LEFT)

    def showRunes(self):
        for children in self.frmMain.winfo_children():
            children.destroy()

        # Titulo da tela
        self.setTitle("Ver Runas")

    def openFile(self):
        # Abre a janela para selecionar o arquivo
        self.filename = filedialog.askopenfilename()

        # Validações do arquivo
        if self.filename == '':
            pass
        elif self.filename.split('.')[-1] != 'png':
            messagebox.showinfo("Arquivo inválido!", "A imagem deve ter extensão .png")
        else:
            # Cria um frame para os widgets
            self.frmTextImg = Frame(self.frmMain)
            self.frmTextImg.pack(anchor='nw')

            # Cria os widgets
            self.lblFileText = Label(self.frmTextImg, text="Imagem selecionada: ")
            self.lblFile = Label(self.frmTextImg, text=self.filename)
            self.lblFileText.pack(side=LEFT)
            self.lblFile.pack(side=LEFT)

            # Habilita o botão para análise da imagem
            self.btnAddImg["state"] = NORMAL

    def analyzeImg(self):
        # Desabilita o botão para análise da imagem
        self.btnAnalyzeImg["state"] = DISABLED

        # Cria um frame para os widgets
        self.frmAnalyze = Frame(self.frmMain)
        self.frmAnalyze.pack(anchor='nw')

        # Cria os textos
        self.lblTextAnalyze = Label(self.frmAnalyze, text="Analisando...")

        # Analisa a imagem
        identifyImg(self.filename)

        # Exibe o resultado
        self.lblTextAnalyze["text"] = "Análise completa!"
        self.lblTextResult = Label(self.frmAnalyze, text="Resultado:")
        self.lblTextAnalyze.pack()
        self.lblTextResult.pack()

    def addImg(self):
        # Desabilita o botão para análise da imagem
        self.btnAddImg["state"] = DISABLED

        # Cria um frame para os widgets
        self.frmAdd = Frame(self.frmMain)
        self.frmAdd.pack(anchor='nw')

        # Cria os textos
        self.lblTextAdd = Label(self.frmAdd, text="")

        # Adiciona a imagem
        addImg(self.filename)

        # Exibe o resultado
        self.lblTextAdd["text"] = "Imagem adicionada!"
        self.lblTextAdd.pack()

    def setTitle(self, title):
        # Titulo da tela
        self.lblTitle = Label(self.frmMain, text=title, font=("Arial Bold", 25))
        self.lblTitle.pack()
        self.sprTitle = Separator(self.frmMain, orient=HORIZONTAL)
        self.sprTitle.pack(fill=X)