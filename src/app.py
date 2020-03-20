from tkinter import Frame, Button, Label, Text, filedialog, messagebox, DoubleVar, PhotoImage
from tkinter import LEFT, RIGHT, TOP, X, DISABLED, NORMAL, BOTH, HORIZONTAL, END
from tkinter import ttk
from img_process import identifyImg, addImg
from db_util import searchRunes, getRune, getRuneNames, getIdRuneInfo

class AppMain:
    def __init__(self, parent):
        self.tabControl = ttk.Notebook(parent, height=500)

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
        self.icoUpload = PhotoImage(file="icons\\upload.png")
        self.icoSearch = PhotoImage(file="icons\\search.png")
        self.icoPlus = PhotoImage(file="icons\\plus.png")
        self.icoRefresh = PhotoImage(file="icons\\refresh.png")
        self.icoBin = PhotoImage(file="icons\\bin.png")
        
        # ========== HOME ==========
        self.lblTitle = ttk.Label(self.tabHome, text="Bem vindo!", font=("Arial Bold", 25))
        self.lblTitle.grid(row=0, column=0, stick='w')

        self.lblWelcomeText1 = ttk.Label(self.tabHome, text="Para analisar uma runa e descobrir o que ela significa, clique em Identificar Runa.", font=("Arial", 10))
        self.lblWelcomeText1.grid(row=1, column=0, stick='w')

        self.lblWelcomeText2 = ttk.Label(self.tabHome, text="Para adicionar uma runa à base de dados, clique em Adicionar Runa.", font=("Arial", 10))
        self.lblWelcomeText2.grid(row=2, column=0, stick='w')

        self.lblWelcomeText3 = ttk.Label(self.tabHome, text="Para ver as runas disponíveis e seus Momentos de Hu, clique em Mostrar Runas.", font=("Arial", 10))
        self.lblWelcomeText3.grid(row=3, column=0, stick='w')

        # ========== Identify rune ==========

        self.lbfAnalyzeImage1 = ttk.LabelFrame(self.tabAnalyze, text="Arquivo: ")
        self.lbfAnalyzeImage1.grid(row=0, column=0, padx=8, pady=4)

        self.lbfAnalyzeImage2 = ttk.LabelFrame(self.tabAnalyze)
        self.lbfAnalyzeImage2.grid(row=1, column=0, padx=8, pady=4)

        self.lbfAnalyzeImage3 = ttk.LabelFrame(self.tabAnalyze, text="Resultado: ")
        self.lbfAnalyzeImage3.grid(row=2, column=0, padx=8, pady=4)

        self.btnOpenFileAnalyze = ttk.Button(self.lbfAnalyzeImage1, text="Abrir arquivo", image=self.icoUpload, compound=LEFT, command=self.openFileToAnalyze)
        self.btnOpenFileAnalyze.grid(row=0, column=0, stick='w')

        self.lblFileAnalyze = ttk.Label(self.lbfAnalyzeImage1, text="Imagem selecionada: ", width=100)
        self.lblFileAnalyze.grid(row=0, column=1, stick='w')

        self.btnAnalyze = ttk.Button(self.lbfAnalyzeImage2, text="Analisar Imagem", image=self.icoSearch, compound=LEFT, state=DISABLED, command=self.analyzeImag)
        self.btnAnalyze.grid(row=0, column=0, stick='w')

        self.lblResultHuMoments = ttk.Label(self.lbfAnalyzeImage3, width=117)
        self.lblResultHuMoments.grid(row=0, column=0, columnspan=2, stick='w')

        self.lblResult = ttk.Label(self.lbfAnalyzeImage3)
        self.lblResult.grid(row=1, column=0, columnspan=2, stick='w')
        
        self.sprResult = ttk.Separator(self.lbfAnalyzeImage3, orient='horizontal')
        self.sprResult.grid(row=2, column=0, columnspan=2, stick='ew')
        
        self.lblResultName = ttk.Label(self.lbfAnalyzeImage3, font=("Arial Bold", 25))
        self.lblResultName.grid(row=3, column=0, columnspan=2, stick='w')
        
        self.lblResultDescription = ttk.Label(self.lbfAnalyzeImage3)
        self.lblResultDescription.grid(row=4, column=0, columnspan=2, stick='w')

        # ========== Add rune ==========

        self.lbfAddImage1 = ttk.LabelFrame(self.tabAdd, text="Arquivo: ", width=300)
        self.lbfAddImage1.grid(row=0, column=0, padx=8, pady=4)
        
        self.lbfAddImage2 = ttk.LabelFrame(self.lbfAddImage1, text="Dados da imagem: ")
        self.lbfAddImage2.grid(row=1, column=0, padx=8, pady=4, stick='w', columnspan=2)

        self.lbfAddImage3 = ttk.LabelFrame(self.tabAdd)
        self.lbfAddImage3.grid(row=2, column=0, padx=8, pady=4)

        self.lbfAddImage4 = ttk.LabelFrame(self.tabAdd, text="Resultado:")
        self.lbfAddImage4.grid(row=3, column=0, padx=8, pady=4)

        self.btnOpenFileAdd = ttk.Button(self.lbfAddImage1, text="Abrir arquivo", image=self.icoUpload, compound=LEFT, command=self.openFileToAdd)
        self.btnOpenFileAdd.grid(row=0, column=0, stick='w')

        self.lblFile = ttk.Label(self.lbfAddImage1, text="Imagem selecionada: ", width=100)
        self.lblFile.grid(row=0, column=1, stick='e')

        self.lblName = ttk.Label(self.lbfAddImage2, text="Nome:")
        self.lblName.grid(row=0, column=0, stick='e', pady=4)
        self.entName = ttk.Combobox(self.lbfAddImage2, state=DISABLED, values=getRuneNames())
        self.entName.grid(row=0, column=1, stick='w', pady=4)

        self.btnAddImg = ttk.Button(self.lbfAddImage3, text="Adicionar Imagem", image=self.icoPlus, compound=LEFT, state=DISABLED, command=self.addImg)
        self.btnAddImg.grid(row=4, column=0)

        self.lblSuccessAddImg1 = ttk.Label(self.lbfAddImage4, width=117)
        self.lblSuccessAddImg1.grid(row=5, column=0, stick='w', columnspan=2)
        
        self.lblSuccessAddImg2 = ttk.Label(self.lbfAddImage4, width=117)
        self.lblSuccessAddImg2.grid(row=6, column=0, stick='w', columnspan=2)

        # ========== Show runes ==========
        self.btnRefreshRunes = ttk.Button(self.tabShow, text="Atualizar", image=self.icoRefresh, compound=LEFT, command=self.refreshRunes)
        self.btnRefreshRunes.grid(row=0, column=0, stick='w')

        self.trvRunes = ttk.Treeview(self.tabShow, height=500)
        self.trvRunes.grid(row=1, column=0, columnspan=2)
        
        self.trvRunes["columns"] = ("id", "name", "hu1", "hu2", "hu3", "hu4", "hu5", "hu6", "hu7")
        self.trvRunes.column("id", width=15)
        self.trvRunes.column("name", width=80)
        self.trvRunes.column("hu1", width=90)
        self.trvRunes.column("hu2", width=90)
        self.trvRunes.column("hu3", width=90)
        self.trvRunes.column("hu4", width=90)
        self.trvRunes.column("hu5", width=90)
        self.trvRunes.column("hu6", width=90)
        self.trvRunes.column("hu7", width=90)
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
        elif self.filename.split('.')[-1] not in ('png', 'jpg'):
            messagebox.showinfo("Arquivo inválido!", "A imagem deve ter extensão .png ou .jgp")
        else:
            self.lblFileAnalyze["text"] = "Imagem selecionada: " + self.filename
            self.btnAnalyze["state"] = NORMAL

    def openFileToAdd(self):
        self.filename = filedialog.askopenfilename()

        if self.filename == '':
            pass
        elif self.filename.split('.')[-1] not in ('png', 'jpg'):
            messagebox.showinfo("Arquivo inválido!", "A imagem deve ter extensão .png ou .jgp")
        else:
            self.lblFile["text"] = "Imagem selecionada: " + self.filename
            self.btnAddImg["state"] = NORMAL
            self.entName["state"] = NORMAL
            self.entName.focus_set()
            self.entName.delete(0, 'end')
            self.entName.insert(0, "")

    def analyzeImag(self):
        result = identifyImg(self.filename)
        rune = getRune(result[0])[0]
        precision = 0 - result[1]

        self.lblResultHuMoments["text"] = "Momentos de Hu: ["
        for i in range(2, 8):
            self.lblResultHuMoments["text"] += str(round(rune[i], 6)) + ", "
        self.lblResultHuMoments["text"] += str(round(rune[7], 6)) + "]"

        self.lblResult["text"] = "Encontrada runa com " + str(precision) + " de desvio."
        
        self.lblResultName["text"] = rune[0]
        
        self.lblResultDescription["text"] = rune[1]

    def addImg(self):
        if self.entName.get() == '':
            messagebox.showinfo("Atenção!", "Todos os campos devem ser preenchidos.")
        else:
            try:
                huMoments = addImg(self.filename, getIdRuneInfo(self.entName.get()))

                self.btnAddImg["state"] = DISABLED
                self.entName["state"] = DISABLED

                self.lblSuccessAddImg1["text"] = "Imagem adicionada com sucesso!"
                self.lblSuccessAddImg2["text"] = "Momentos de Hu: ["
                for i in range(0, 6):
                    self.lblSuccessAddImg2["text"] += str(round(float(huMoments[i]), 6)) + ", "
                self.lblSuccessAddImg2["text"] += str(round(float(huMoments[6]), 6)) + "]"
            except Exception as e:
                messagebox.showinfo("Erro!", e)

    def refreshRunes(self):
        for item in self.trvRunes.get_children():
            self.trvRunes.delete(item)

        runes = searchRunes()
        i = 0
        for rune in runes:
            self.trvRunes.insert("", i, values=(rune[0], rune[1], round(rune[2], 6), round(rune[3], 6), round(rune[4], 6), round(rune[5], 6), round(rune[6], 6), round(rune[7], 6), round(rune[8], 6)))
            i += 1