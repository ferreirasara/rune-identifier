from tkinter import Frame, Button, Label, Text, filedialog, messagebox, DoubleVar
from tkinter import LEFT, RIGHT, TOP, X, DISABLED, NORMAL, BOTH, HORIZONTAL, END
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

        self.btnAnalyze = Button(self.tabAnalyze, text="Analisar Imagem", state=DISABLED, command=self.analyzeImag)
        self.btnAnalyze.grid(row=2, column=0, stick='w')

        # ========== Add rune ==========
        self.btnOpenFileAdd = Button(self.tabAdd, text="Abrir arquivo", command=self.openFileToAdd)
        self.btnOpenFileAdd.grid(row=0, column=0, stick='w')

        self.lblFile = Label(self.tabAdd, text="Imagem selecionada: ")
        self.lblFile.grid(row=1, column=0, stick='e')
        self.lblFileName = Label(self.tabAdd)
        self.lblFileName.grid(row=1, column=1, stick='w') 

        self.lblName = Label(self.tabAdd, text="Nome:")
        self.lblName.grid(row=2, column=0, stick='e')
        self.entName = ttk.Entry(self.tabAdd)
        self.entName.grid(row=2, column=1, stick='w')

        self.lblDescription = Label(self.tabAdd, text="Descrição:")
        self.lblDescription.grid(row=3, column=0, stick='e')
        self.entDescription = ttk.Entry(self.tabAdd)
        self.entDescription.grid(row=3, column=1, stick='w')

        self.btnAddImg = Button(self.tabAdd, text="Adicionar Imagem", state=DISABLED, command=self.addImg)
        self.btnAddImg.grid(row=4, column=0)

        # ========== Show runes ==========
        self.trvRunes = ttk.Treeview(self.tabShow)
        self.trvRunes.grid(row=0, column=0)
        
        self.trvRunes["columns"] = ("name", "hu1", "hu2", "hu3", "hu4", "hu5", "hu6", "hu7")
        self.trvRunes.column("name", width=100)
        self.trvRunes.column("hu1", width=71)
        self.trvRunes.column("hu2", width=71)
        self.trvRunes.column("hu3", width=71)
        self.trvRunes.column("hu4", width=71)
        self.trvRunes.column("hu5", width=71)
        self.trvRunes.column("hu6", width=71)
        self.trvRunes.column("hu7", width=71)
        self.trvRunes.heading("name", text="Nome")
        self.trvRunes.heading("hu1", text="Hu[1]")
        self.trvRunes.heading("hu2", text="Hu[2]")
        self.trvRunes.heading("hu3", text="Hu[3]")
        self.trvRunes.heading("hu4", text="Hu[4]")
        self.trvRunes.heading("hu5", text="Hu[5]")
        self.trvRunes.heading("hu6", text="Hu[6]")
        self.trvRunes.heading("hu7", text="Hu[7]")

        self.trvRunes["show"] = "headings"

        self.trvRunes.insert("", 0, values=("Exemple 01", "0.00162663", "3.11619e-07", "3.61005e-10", "1.44485e-10", "-2.55279e-20", "-7.57625e-14", "2.09098e-20"))

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
            self.lblFileName["text"] = self.filename
            self.btnAddImg["state"] = NORMAL

    def analyzeImag(self):
        pass

    def addImg(self):
        addImg(self.filename)