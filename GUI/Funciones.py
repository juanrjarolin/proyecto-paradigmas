class FuncionesGui:
    '''Función que representa a una función del GUI Tkinter'''
    def __init__(self):
        pass

    def mostrar_ventana(self, ventana):
        ventana.deiconify()

    def ocultar_ventana(self, ventana):
        ventana.withdraw()

    def cerrar_ventana(self, ventana):
        ventana.destroy()

    def habilitar_boton(self, boton):
        boton.configure(state='normal')

    def deshabilitar_boton(self, boton):
        boton.configure(state='disabled')
