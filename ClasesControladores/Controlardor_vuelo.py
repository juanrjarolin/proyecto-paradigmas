from tkinter.messagebox import showinfo
class ControlarVuelo:
    '''Abstracción que representa a un controlador de vuelos'''

    @classmethod
    def controlar_partida(cls, hora_now, vuelo):
        '''Funcion que controla partida del avion'''
        if hora_now > vuelo.horario_partida:
            vuelo.cambiar_estado("Partió")
            vuelo.cambiar_habilitacion(False)
        else:
            vuelo.cambiar_estado("Programado")
            vuelo.cambiar_habilitacion(True)

    @classmethod
    def controlar_cantidad_personas(cls, adultos, niños, bebes):
        maxima = 9
        cantidad_pasajeros = bebes + adultos + niños

        if cantidad_pasajeros > maxima:
            cantidad_pasajeros = 0
            showinfo('Corrección', 'Pasajeros seleccionados sobrepasan la cantidad requerida')
            return False
        else:
            return True