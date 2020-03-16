from tkinter import Tk
from app import AppMain
from db_util import createDB

createDB()
root = Tk()
root.geometry('950x600')

root.title("Identificador de Runas")

app = AppMain(root)
root.mainloop()