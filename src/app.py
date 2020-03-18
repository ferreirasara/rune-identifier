from tkinter import Frame, Button, Label, Text, filedialog, messagebox, DoubleVar, PhotoImage
from tkinter import LEFT, RIGHT, TOP, X, DISABLED, NORMAL, BOTH, HORIZONTAL, END
from tkinter import ttk
from img_process import identifyImg, addImg
from db_util import searchRunes, delRune, getRune

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

        # ========== ICONS ==========
        self.icoUpload = PhotoImage(file="upload.png")
        self.icoSearch = PhotoImage(file="search.png")
        self.icoPlus = PhotoImage(file="plus.png")
        self.icoRefresh = PhotoImage(file="refresh.png")
        self.icoBin = PhotoImage(file="bin.png")
        
        # ========== HOME ==========
        self.lblTitle = ttk.Label(self.tabHome, text="Bem vindo!", font=("Arial Bold", 25))
        self.lblTitle.grid(row=0, column=0, stick='w')

        self.lblWelcomeText1 = ttk.Label(self.tabHome, text="Para analisar uma runa e descobrir o que ela significa, clique em Identificar Runa.", font=("Arial", 10))
        self.lblWelcomeText1.grid(row=1, column=0, stick='w')

        self.lblWelcomeText2 = ttk.Label(self.tabHome, text="Para adicionar uma runa à base de dados, clique em Adicionar Runa.", font=("Arial", 10))
        self.lblWelcomeText2.grid(row=2, column=0, stick='w')

        # ========== Identify rune ==========

        self.btnOpenFileAnalyze = ttk.Button(self.tabAnalyze, text="Abrir arquivo", image=self.icoUpload, compound=LEFT, command=self.openFileToAnalyze)
        self.btnOpenFileAnalyze.grid(row=0, column=0, stick='w')

        self.lblFileAnalyze = ttk.Label(self.tabAnalyze, text="Imagem selecionada: ")
        self.lblFileAnalyze.grid(row=1, column=0, columnspan=2, stick='w')

        self.btnAnalyze = ttk.Button(self.tabAnalyze, text="Analisar Imagem", image=self.icoSearch, compound=LEFT, state=DISABLED, command=self.analyzeImag)
        self.btnAnalyze.grid(row=2, column=0, stick='w')

        # ========== Add rune ==========
        self.btnOpenFileAdd = ttk.Button(self.tabAdd, text="Abrir arquivo", image=self.icoUpload, compound=LEFT, command=self.openFileToAdd)
        self.btnOpenFileAdd.grid(row=0, column=0, stick='w')

        self.lblFile = ttk.Label(self.tabAdd, text="Imagem selecionada: ")
        self.lblFile.grid(row=1, column=0, stick='e')
        self.lblFileName = ttk.Label(self.tabAdd)
        self.lblFileName.grid(row=1, column=1, stick='w') 

        self.lblName = ttk.Label(self.tabAdd, text="Nome:")
        self.lblName.grid(row=2, column=0, stick='e')
        self.entName = ttk.Entry(self.tabAdd, state=DISABLED)
        self.entName.grid(row=2, column=1, stick='w')

        self.lblDescription = ttk.Label(self.tabAdd, text="Descrição:")
        self.lblDescription.grid(row=3, column=0, stick='e')
        self.entDescription = ttk.Entry(self.tabAdd, state=DISABLED)
        self.entDescription.grid(row=3, column=1, stick='w')

        self.btnAddImg = ttk.Button(self.tabAdd, text="Adicionar Imagem", image=self.icoPlus, compound=LEFT, state=DISABLED, command=self.addImg)
        self.btnAddImg.grid(row=4, column=0)

        # ========== Show runes ==========
        self.btnRefreshRunes = ttk.Button(self.tabShow, text="Atualizar", image=self.icoRefresh, compound=LEFT, command=self.refreshRunes)
        self.btnRefreshRunes.grid(row=0, column=0, stick='w')

        self.btnDelRune = ttk.Button(self.tabShow, text="Excluir", image=self.icoBin, compound=LEFT, command=self.delRune)
        self.btnDelRune.grid(row=0, column=1, stick='e')

        self.trvRunes = ttk.Treeview(self.tabShow, height=600)
        self.trvRunes.grid(row=1, column=0, columnspan=2)
        
        self.trvRunes["columns"] = ("id", "name", "hu1", "hu2", "hu3", "hu4", "hu5", "hu6", "hu7")
        self.trvRunes.column("id", width=15)
        self.trvRunes.column("name", width=80)
        self.trvRunes.column("hu1", width=120)
        self.trvRunes.column("hu2", width=120)
        self.trvRunes.column("hu3", width=120)
        self.trvRunes.column("hu4", width=120)
        self.trvRunes.column("hu5", width=120)
        self.trvRunes.column("hu6", width=120)
        self.trvRunes.column("hu7", width=120)
        self.trvRunes.heading("id", text="ID")
        self.trvRunes.heading("name", text="Nome")
        self.trvRunes.heading("hu1", text="Hu[1]")
        self.trvRunes.heading("hu2", text="Hu[2]")
        self.trvRunes.heading("hu3", text="Hu[3]")
        self.trvRunes.heading("hu4", text="Hu[4]")
        self.trvRunes.heading("hu5", text="Hu[5]")
        self.trvRunes.heading("hu6", text="Hu[6]")
        self.trvRunes.heading("hu7", text="Hu[7]")

        self.trvRunes["show"] = "headings"

        self.refreshRunes()

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
            self.entName["state"] = NORMAL
            self.entDescription["state"] = NORMAL
            self.entName.focus_set()
            self.entName.delete(0, 'end')
            self.entName.insert(0, "")
            self.entDescription.delete(0, 'end')
            self.entDescription.insert(0, "")

    def analyzeImag(self):
        result = identifyImg(self.filename)
        rune = getRune(result[0])
        precision = 0 - result[1]
        self.lblResult = ttk.Label(self.tabAnalyze, text="Encontrada runa com " + str(precision) + " de desvio.")
        self.lblResultName = ttk.Label(self.tabAnalyze, text=rune[0][0], font=("Arial Bold", 25))
        self.lblResultDescription = ttk.Label(self.tabAnalyze, text=rune[0][1])
        self.lblResult.grid(row=3, column=0, columnspan=2, stick='w')
        self.lblResultName.grid(row=4, column=0, columnspan=2, stick='w')
        self.lblResultDescription.grid(row=5, column=0, columnspan=2, stick='w')

    def addImg(self):
        if self.entName.get() == '' or self.entDescription.get() == '':
            messagebox.showinfo("Atenção!", "Todos os campos devem ser preenchidos.")
        else:
            try:
                addImg(self.filename, self.entName.get(), self.entDescription.get())

                self.btnAddImg["state"] = DISABLED
                self.entName["state"] = DISABLED
                self.entDescription["state"] = DISABLED

                self.lblSuccessAddImg = ttk.Label(self.tabAdd, text="Imagem adicionada com sucesso!")
                self.lblSuccessAddImg.grid(row=5, column=0, stick='w', columnspan=2)
            except Exception as e:
                messagebox.showinfo("Erro!", e)

    def refreshRunes(self):
        for item in self.trvRunes.get_children():
            self.trvRunes.delete(item)

        runes = searchRunes()
        i = 0
        for rune in runes:
            self.trvRunes.insert("", i, values=(rune[0], rune[1], rune[2], rune[3], rune[4], rune[5], rune[6], rune[7], rune[8]))
            i += 1

    def delRune(self):
        currentItem = self.trvRunes.focus()
        try:
            delRune(int(self.trvRunes.item(currentItem)["values"][0]))
            self.refreshRunes()
        except:
            messagebox.showinfo("Atenção!", "Selecione pelo menos uma runa.")