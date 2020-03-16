from tkinter import Tk
from app import AppMain
from db_util import createDB

createDB()
root = Tk()
root.geometry('600x400')

root.title("Identificador de Runas")

app = AppMain(root)
root.mainloop()