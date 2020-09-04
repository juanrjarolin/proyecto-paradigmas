from tkinter import *
import GUI.Instancias as instancias
class Pantalla:
    def __init__(self):
        self.titulo = ""

    @classmethod
    def titulo_sistema(cls, ventana):
        ventana.title('LTAM Airlines')

    @classmethod
    def mostrar_titulo(cls, ventana, texto):
        '''Muestra cualquier titulo en la pantalla'''
        #print(titulo.center(86, '='))
        titulo = instancias.MiLabel(ventana, text=texto, font=('Arial', 13, 'bold'))
        titulo.pack()

    @classmethod
    def mostrar_bienvenida(cls, ventana):
        '''Muestra en la pantalla principal una bienvenida'''
        texto = "¡Viajá por el mundo con nuestras mejores ofertas!"
        bienvenida = Label(ventana, text=texto, fg='blue', font=('Arial', 12, 'bold'))
        bienvenida.pack()

    @classmethod
    def limpiar_pantalla(cls, frame):
        '''Oculta la pantalla para mostrar otra ventana'''
        frame.withdraw()

    @classmethod
    def mostrar_pantalla(cls, frame):
        '''Muestra la ventana principal'''
        frame.master.deiconify()
