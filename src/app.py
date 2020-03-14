from tkinter import Frame, Button, Label, Text, filedialog, messagebox, DoubleVar
from tkinter import LEFT, RIGHT, TOP, X, DISABLED, NORMAL, BOTH, HORIZONTAL
from tkinter import ttk
from img_process import identifyImg, addImg
from db_util import createDB

class AppMain:
    def __init__(self, parent):
        self.tabControl = ttk.Notebook(parent, height=400)

        self.tabHome = ttk.Frame(self.tabControl)
        self.tabAnalyze = ttk.Frame(self.tabControl)
        self.tabAdd = ttk.Frame(self.tabControl)
        self.tabShow = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tabHome, text="Home")
        self.tabControl.add(self.tabAnalyze, text="Analisar Runa")
        self.tabControl.add(self.tabAdd, text="Adicionar Runa")
        self.tabControl.add(self.tabShow, text="Mostrar Runas")

        self.tabControl.pack(fill=BOTH)
        
        # ========== HOME ==========
        self.lblTitle = Label(self.tabHome, text="Bem vindo!", font=("Arial Bold", 25))
        self.lblTitle.grid(row=0, column=0, stick='w')

        self.lblWelcomeText1 = Label(self.tabHome, text="Para analisar uma runa e descobrir o que ela significa, clique em Identificar Runa.", font=("Arial", 10))
        self.lblWelcomeText1.grid(row=1, column=0, stick='w')

        self.lblWelcomeText2 = Label(self.tabHome, text="Para adicionar uma runa à base de dados, clique em Adicionar Runa.", font=("Arial", 10))
        self.lblWelcomeText2.grid(row=2, column=0, stick='w')

        # ========== Identify rune ==========
        self.btnOpenFileAnalyze = Button(self.tabAnalyze, text="Abrir arquivo", command=self.openFileToAnalyze)
        self.btnOpenFileAnalyze.grid(row=0, column=0, stick='w')

        self.lblFileAnalyze = Label(self.tabAnalyze, text="Imagem selecionada: ")
        self.lblFileAnalyze.grid(row=1, column=0, columnspan=2, stick='w')

        self.btnAnalyze = Button(self.tabAnalyze, text="Analisar Imagem", state=DISABLED)
        self.btnAnalyze.grid(row=2, column=0, stick='w')

        self.lblResultText = Label(self.tabAnalyze, text="Resultado: ")
        self.lblResultText.grid(row=3, column=0, columnspan=2, stick='w')

        # ========== Add rune ==========
        self.btnOpenFileAdd = Button(self.tabAdd, text="Abrir arquivo", command=self.openFileToAdd)
        self.btnOpenFileAdd.grid(row=0, column=0, stick='w')

        self.lblFileAdd = Label(self.tabAdd, text="Imagem selecionada: ")
        self.lblFileAdd.grid(row=1, column=0, columnspan=2, stick='w')

        self.btnAddImg = Button(self.tabAdd, text="Adicionar Imagem", state=DISABLED)
        self.btnAddImg.grid(row=2, column=0, stick='w')

        # ========== Show runes ==========

    def openFileToAnalyze(self):
        self.filename = filedialog.askopenfilename()

        if self.filename == '':
            pass
        elif self.filename.split('.')[-1] != 'png':
            messagebox.showinfo("Arquivo inválido!", "A imagem deve ter extensão .png")
        else:
            self.lblFileAnalyze["text"] += self.filename
            self.btnAnalyze["state"] = NORMAL

    def openFileToAdd(self):
        self.filename = filedialog.askopenfilename()

        if self.filename == '':
            pass
        elif self.filename.split('.')[-1] != 'png':
            messagebox.showinfo("Arquivo inválido!", "A imagem deve ter extensão .png")
        else:
            self.lblFileAdd["text"] += self.filename
            self.btnAddImg["state"] = NORMAL