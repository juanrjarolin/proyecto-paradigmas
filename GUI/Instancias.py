from tkinter import *

class MiVentana(Frame):
    '''Abstracción que representa a una ventana'''
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()

class MiBoton(Button):
    '''Abstracción que representa a un boton'''
    def __init__(self, parent, **config):
        Button.__init__(self, parent, **config)
        self.pack()


class MiMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)


class MiLabel(Label):
    def __init__(self, parent, **config):
        Label.__init__(self, parent, **config)

class MiStringVar(StringVar):
    def __init__(self):
        StringVar.__init__(self)

class MiRadioButton(Radiobutton):
    def __init__(self, parent, **config):
        Radiobutton.__init__(self, parent, **config)


class MiEntry(Entry):
    def __init__(self, parent, **config):
        Entry.__init__(self, parent, **config)

class MiToplevel(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

class MiPhotoImage(PhotoImage):
    def __init__(self, file):
        PhotoImage.__init__(self, file)