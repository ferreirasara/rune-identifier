from tkinter import Frame, Button, Label, Text, filedialog, messagebox, DoubleVar, PhotoImage
from tkinter import LEFT, RIGHT, TOP, X, DISABLED, NORMAL, BOTH, HORIZONTAL, END, BOTTOM
from tkinter import ttk
from img_process import identifyImg, addImg, calcHuMoments
from db_util import searchAvgRunes, searchAllRunes, getRune, getRuneNames, getIdRuneInfo, delRune

class AppMain:
    def __init__(self, parent):
        # ========== NOTEBOOK ==========
        self.TAB_CONTROL = ttk.Notebook(parent, height=500)
        
        # ========== NOTEBOOK TABS ==========

        self.TAB_HOME = ttk.Frame(self.TAB_CONTROL)
        self.TAB_ANALYZE = ttk.Frame(self.TAB_CONTROL)
        self.TAB_ADD = ttk.Frame(self.TAB_CONTROL)
        self.TAB_SHOW = ttk.Frame(self.TAB_CONTROL)

        self.TAB_CONTROL.add(self.TAB_HOME, text="Home")
        self.TAB_CONTROL.add(self.TAB_ANALYZE, text="Analisar Runa")
        self.TAB_CONTROL.add(self.TAB_ADD, text="Adicionar Runa")
        self.TAB_CONTROL.add(self.TAB_SHOW, text="Mostrar Runas")

        self.TAB_CONTROL.pack(fill=BOTH)

        # ========== ICONS ==========
        self.ICO_UPLOAD = PhotoImage(file="icons\\upload.png")
        self.ICO_SEARCH = PhotoImage(file="icons\\search.png")
        self.ICO_PLUS = PhotoImage(file="icons\\plus.png")
        self.ICO_REFRESH = PhotoImage(file="icons\\refresh.png")
        self.ICO_BIN = PhotoImage(file="icons\\bin.png")
        
        # ========== HOME ==========
        self.LABEL_HOME_TITLE = ttk.Label(self.TAB_HOME, text="Bem vindo!", font=("Arial Bold", 25))
        self.LABEL_HOME_TITLE.grid(row=0, column=0, stick='w')

        self.LABELFRAME_HOME_INSTRUCTIONS = ttk.LabelFrame(self.TAB_HOME, text="Instruções:")
        self.LABELFRAME_HOME_INSTRUCTIONS.grid(row=1, column=0, stick='w')

        self.LABELFRAME_HOME_OBS = ttk.LabelFrame(self.TAB_HOME, text="Observações: ")
        self.LABELFRAME_HOME_OBS.grid(row=2, column=0, stick='w')

        self.LABEL_HOME_TEXT1 = ttk.Label(self.LABELFRAME_HOME_INSTRUCTIONS, text="Para analisar uma runa e descobrir o que ela significa, clique em Identificar Runa.", font=("Arial", 10), width=100)
        self.LABEL_HOME_TEXT1.grid(row=0, column=0, stick='w')

        self.LABEL_HOME_TEXT2 = ttk.Label(self.LABELFRAME_HOME_INSTRUCTIONS, text="Para adicionar uma runa à base de dados, clique em Adicionar Runa.", font=("Arial", 10))
        self.LABEL_HOME_TEXT2.grid(row=1, column=0, stick='w')

        self.LABEL_HOME_TEXT3 = ttk.Label(self.LABELFRAME_HOME_INSTRUCTIONS, text="Para ver as runas disponíveis e seus Momentos de Hu, clique em Mostrar Runas.", font=("Arial", 10))
        self.LABEL_HOME_TEXT3.grid(row=2, column=0, stick='w')

        self.LABEL_HOME_TEXT4 = ttk.Label(self.LABELFRAME_HOME_OBS, text="Inicialmente, o programa conta com 5 exemplares de cada uma das runas:\n\t- Ansuz\n\t- Fehu\n\t- Gebo\n\t- Kenaz\n\t- Raidho\n\t- Thurisaz\n\t- Uruz\n\t- Wunjo.", width=117)
        self.LABEL_HOME_TEXT4.grid(row=0, column=0, stick='w')

        self.LABEL_HOME_TEXT5 = ttk.Label(self.LABELFRAME_HOME_OBS, text="Existem várias imagens da mesma runa, para aumentar as chances do algoritmo identificar a runa corretamente.")
        self.LABEL_HOME_TEXT5.grid(row=1, column=0, stick='w')

        self.LABEL_HOME_TEXT6 = ttk.Label(self.LABELFRAME_HOME_OBS, text="Os Momentos de Hu das runas podem ser vistos na aba Mostrar Runas.")
        self.LABEL_HOME_TEXT6.grid(row=2, column=0, stick='w')

        # ========== Identify rune ==========

        self.LABELFRAME_ANALYZE_FILE = ttk.LabelFrame(self.TAB_ANALYZE, text="Arquivo: ")
        self.LABELFRAME_ANALYZE_FILE.grid(row=0, column=0, padx=8, pady=4)

        self.LABELFRAME_ANALYZE_BUTTON = ttk.LabelFrame(self.TAB_ANALYZE)
        self.LABELFRAME_ANALYZE_BUTTON.grid(row=1, column=0, padx=8, pady=4)

        self.LABELFRAME_ANALYZE_RESULT = ttk.LabelFrame(self.TAB_ANALYZE, text="Resultado: ")
        self.LABELFRAME_ANALYZE_RESULT.grid(row=2, column=0, padx=8, pady=4)

        self.BUTON_ANALYZE_OPEN = ttk.Button(self.LABELFRAME_ANALYZE_FILE, text="Abrir arquivo", image=self.ICO_UPLOAD, compound=LEFT, command=self.openFileToAnalyze)
        self.BUTON_ANALYZE_OPEN.grid(row=0, column=0, stick='w')

        self.LABEL_ANALYZE_FILE = ttk.Label(self.LABELFRAME_ANALYZE_FILE, text="Imagem selecionada: ", width=100)
        self.LABEL_ANALYZE_FILE.grid(row=0, column=1, stick='w')

        self.BUTTON_ANALYZE_ANALYZE = ttk.Button(self.LABELFRAME_ANALYZE_BUTTON, text="Analisar Imagem", image=self.ICO_SEARCH, compound=LEFT, state=DISABLED, command=self.analyzeImag)
        self.BUTTON_ANALYZE_ANALYZE.grid(row=0, column=0, stick='w')

        self.LABEL_ANALYZE_HU_MOMENTS = ttk.Label(self.LABELFRAME_ANALYZE_RESULT, width=117)
        self.LABEL_ANALYZE_HU_MOMENTS.grid(row=0, column=0, columnspan=2, stick='w')

        self.LABEL_ANALYZE_RESULT = ttk.Label(self.LABELFRAME_ANALYZE_RESULT)
        self.LABEL_ANALYZE_RESULT.grid(row=1, column=0, columnspan=2, stick='w')
        
        self.SEPARATOR_ANALYZE_RESULT = ttk.Separator(self.LABELFRAME_ANALYZE_RESULT, orient='horizontal')
        self.SEPARATOR_ANALYZE_RESULT.grid(row=2, column=0, columnspan=2, stick='ew')
        
        self.LABEL_ANALYZE_RESULT_NAME = ttk.Label(self.LABELFRAME_ANALYZE_RESULT, font=("Arial Bold", 25))
        self.LABEL_ANALYZE_RESULT_NAME.grid(row=3, column=0, columnspan=2, stick='w')
        
        self.LABEL_ANALYZE_RESULT_DESCRIPTION = ttk.Label(self.LABELFRAME_ANALYZE_RESULT)
        self.LABEL_ANALYZE_RESULT_DESCRIPTION.grid(row=4, column=0, columnspan=2, stick='w')

        # ========== Add rune ==========

        self.LABELFRAME_ADD_FILE = ttk.LabelFrame(self.TAB_ADD, text="Arquivo: ", width=300)
        self.LABELFRAME_ADD_FILE.grid(row=0, column=0, padx=8, pady=4)
        
        self.LABELFRAME_ADD_DATA = ttk.LabelFrame(self.LABELFRAME_ADD_FILE, text="Dados da imagem: ")
        self.LABELFRAME_ADD_DATA.grid(row=1, column=0, padx=8, pady=4, stick='w', columnspan=2)

        self.LABELFRAME_ADD_BUTTON = ttk.LabelFrame(self.TAB_ADD)
        self.LABELFRAME_ADD_BUTTON.grid(row=2, column=0, padx=8, pady=4)

        self.LABELFRAME_ADD_RESULT = ttk.LabelFrame(self.TAB_ADD, text="Resultado:")
        self.LABELFRAME_ADD_RESULT.grid(row=3, column=0, padx=8, pady=4)

        self.BUTTON_ADD_OPEN = ttk.Button(self.LABELFRAME_ADD_FILE, text="Abrir arquivo", image=self.ICO_UPLOAD, compound=LEFT, command=self.openFileToAdd)
        self.BUTTON_ADD_OPEN.grid(row=0, column=0, stick='w')

        self.LABEL_ADD_FILE = ttk.Label(self.LABELFRAME_ADD_FILE, text="Imagem selecionada: ", width=100)
        self.LABEL_ADD_FILE.grid(row=0, column=1, stick='e')

        self.LABEL_ADD_DATA_NAME = ttk.Label(self.LABELFRAME_ADD_DATA, text="Nome:")
        self.LABEL_ADD_DATA_NAME.grid(row=0, column=0, stick='e', pady=4)
        self.ENTRY_ADD_DATA_NAME = ttk.Combobox(self.LABELFRAME_ADD_DATA, state=DISABLED, values=getRuneNames())
        self.ENTRY_ADD_DATA_NAME.grid(row=0, column=1, stick='w', pady=4)

        self.BUTTON_ADD_ADD = ttk.Button(self.LABELFRAME_ADD_BUTTON, text="Adicionar Imagem", image=self.ICO_PLUS, compound=LEFT, state=DISABLED, command=self.addImg)
        self.BUTTON_ADD_ADD.grid(row=4, column=0)

        self.LABEL_ADD_SUCCESS_MESSAGE = ttk.Label(self.LABELFRAME_ADD_RESULT, width=117)
        self.LABEL_ADD_SUCCESS_MESSAGE.grid(row=5, column=0, stick='w', columnspan=2)
        
        self.LABEL_ADD_SUCCESS_HU_MOMENTS = ttk.Label(self.LABELFRAME_ADD_RESULT, width=117)
        self.LABEL_ADD_SUCCESS_HU_MOMENTS.grid(row=6, column=0, stick='w', columnspan=2)

        # ========== Show runes ==========
        self.BUTTON_SHOW_REFRESH = ttk.Button(self.TAB_SHOW, text="Atualizar", image=self.ICO_REFRESH, compound=LEFT, command=self.refreshRunes)
        self.BUTTON_SHOW_REFRESH.grid(row=0, column=0, stick='w')

        self.BUTTON_SHOW_DELETE = ttk.Button(self.TAB_SHOW, text="Excluir", image=self.ICO_BIN, compound=LEFT, command=self.deleteRune)
        self.BUTTON_SHOW_DELETE.grid(row=0, column=1, stick='e')

        self.TREEVIEW_SHOW_RUNES = ttk.Treeview(self.TAB_SHOW, height=21)
        self.TREEVIEW_SHOW_RUNES.grid(row=1, column=0, columnspan=2)
        
        self.TREEVIEW_SHOW_RUNES["columns"] = ("id", "name", "hu1", "hu2", "hu3", "hu4", "hu5", "hu6", "hu7")
        self.TREEVIEW_SHOW_RUNES.column("id", width=10)
        self.TREEVIEW_SHOW_RUNES.column("name", width=90)
        self.TREEVIEW_SHOW_RUNES.column("hu1", width=90)
        self.TREEVIEW_SHOW_RUNES.column("hu2", width=90)
        self.TREEVIEW_SHOW_RUNES.column("hu3", width=90)
        self.TREEVIEW_SHOW_RUNES.column("hu4", width=90)
        self.TREEVIEW_SHOW_RUNES.column("hu5", width=90)
        self.TREEVIEW_SHOW_RUNES.column("hu6", width=90)
        self.TREEVIEW_SHOW_RUNES.column("hu7", width=90)
        self.TREEVIEW_SHOW_RUNES.heading("id", text="ID")
        self.TREEVIEW_SHOW_RUNES.heading("name", text="Nome")
        self.TREEVIEW_SHOW_RUNES.heading("hu1", text="Hu[1]")
        self.TREEVIEW_SHOW_RUNES.heading("hu2", text="Hu[2]")
        self.TREEVIEW_SHOW_RUNES.heading("hu3", text="Hu[3]")
        self.TREEVIEW_SHOW_RUNES.heading("hu4", text="Hu[4]")
        self.TREEVIEW_SHOW_RUNES.heading("hu5", text="Hu[5]")
        self.TREEVIEW_SHOW_RUNES.heading("hu6", text="Hu[6]")
        self.TREEVIEW_SHOW_RUNES.heading("hu7", text="Hu[7]")

        self.TREEVIEW_SHOW_RUNES["show"] = "headings"

        self.refreshRunes()

    def openFileToAnalyze(self):
        self.filename = filedialog.askopenfilename()

        if self.filename == '':
            pass
        elif self.filename.split('.')[-1] not in ('png', 'jpg'):
            messagebox.showerror("Identificador de Runas", "O arquivo deve ser uma imagem.")
        else:
            self.LABEL_ANALYZE_FILE["text"] = "Imagem selecionada: " + self.filename
            self.BUTTON_ANALYZE_ANALYZE["state"] = NORMAL

    def openFileToAdd(self):
        self.filename = filedialog.askopenfilename()

        if self.filename == '':
            pass
        elif self.filename.split('.')[-1] not in ('png', 'jpg', 'gif'):
            messagebox.showerror("Identificador de Runas", "O arquivo deve ser uma imagem.")
        else:
            self.LABEL_ADD_FILE["text"] = "Imagem selecionada: " + self.filename
            self.BUTTON_ADD_ADD["state"] = NORMAL
            self.ENTRY_ADD_DATA_NAME["state"] = NORMAL

    def analyzeImag(self):
        result = identifyImg(self.filename)
        rune = getRune(result[0])[0]
        precision = 0 - result[1]

        huMoments = calcHuMoments(self.filename)

        self.LABEL_ANALYZE_HU_MOMENTS["text"] = "Momentos de Hu: ["
        for i in range(0, 6):
            self.LABEL_ANALYZE_HU_MOMENTS["text"] += str(round(huMoments[i], 6)) + ", "
        self.LABEL_ANALYZE_HU_MOMENTS["text"] += str(round(huMoments[6], 6)) + "]"

        self.LABEL_ANALYZE_RESULT["text"] = "Encontrada runa com " + str(round(precision, 6)) + " de desvio." + "\n"
        self.LABEL_ANALYZE_RESULT["text"] += "Momentos de Hu da runa encontrada: ["
        for i in range(2, 8):
            self.LABEL_ANALYZE_RESULT["text"] += str(round(rune[i], 6)) + ", "
        self.LABEL_ANALYZE_RESULT["text"] += str(round(rune[7], 6)) + "]"


        self.LABEL_ANALYZE_RESULT_NAME["text"] = rune[0]
        
        self.LABEL_ANALYZE_RESULT_DESCRIPTION["text"] = rune[1]

    def addImg(self):
        if self.ENTRY_ADD_DATA_NAME.get() == '':
            messagebox.showerror("Identificador de Runas", "Todos os campos devem ser preenchidos.")
        else:
            huMoments = addImg(self.filename, getIdRuneInfo(self.ENTRY_ADD_DATA_NAME.get()))

            self.BUTTON_ADD_ADD["state"] = DISABLED
            self.ENTRY_ADD_DATA_NAME["state"] = DISABLED

            self.LABEL_ADD_SUCCESS_MESSAGE["text"] = "Imagem adicionada com sucesso!"
            self.LABEL_ADD_SUCCESS_HU_MOMENTS["text"] = "Momentos de Hu: ["
            for i in range(0, 6):
                self.LABEL_ADD_SUCCESS_HU_MOMENTS["text"] += str(round(huMoments[i], 6)) + ", "
            self.LABEL_ADD_SUCCESS_HU_MOMENTS["text"] += str(round(huMoments[6], 6)) + "]"

    def refreshRunes(self):
        for item in self.TREEVIEW_SHOW_RUNES.get_children():
            self.TREEVIEW_SHOW_RUNES.delete(item)
        runes = searchAllRunes()
        i = 0
        for rune in runes:
            self.TREEVIEW_SHOW_RUNES.insert("", i, values=(rune[0], rune[1], round(rune[2], 6), round(rune[3], 6), round(rune[4], 6), round(rune[5], 6), round(rune[6], 6), round(rune[7], 6), round(rune[8], 6)))
            i += 1

    def deleteRune(self):
        currentRune = self.TREEVIEW_SHOW_RUNES.focus()
        try:
            delRune(int(self.TREEVIEW_SHOW_RUNES.item(currentRune)["values"][0]))
            self.refreshRunes()
        except:
            messagebox.showerror("Identificador de Runas", "Selecione uma runa para excluir.")