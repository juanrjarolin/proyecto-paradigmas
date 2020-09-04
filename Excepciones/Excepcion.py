from tkinter.messagebox import showerror
class ErrCed(Exception):
    def __init__(self, valor):
        if valor == 0:
            showerror('Error', 'Error a causa de '+str(valor))