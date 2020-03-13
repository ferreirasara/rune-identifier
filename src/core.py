from tkinter import Tk
from app import AppMain

root = Tk()
root.geometry('600x400')

root.title("Identificador de Runas")

app = AppMain(root)
app.start()
root.mainloop()