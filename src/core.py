from tkinter import Tk
from tkinter import ttk
from app import AppMain
from db_util import createDB

createDB()
root = Tk()

root.minsize(width=500,height=500)
root.resizable(width=0,height=0)  

root.iconbitmap("icons\\rune.ico")

root.style = ttk.Style()
root.style.theme_use("clam")

root.title("Identificador de Runas")

app = AppMain(root)
root.mainloop()