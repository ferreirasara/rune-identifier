from tkinter import Tk
from tkinter import ttk
from app import AppMain
from db_util import createDB

createDB()
root = Tk()
root.geometry('950x630')

root.style = ttk.Style()
root.style.theme_use("clam")
# print(root.style.theme_names())

root.title("Identificador de Runas")

app = AppMain(root)
root.mainloop()