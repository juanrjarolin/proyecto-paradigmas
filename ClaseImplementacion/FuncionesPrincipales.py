import os
import ClasesControladores.Controlador_pasajero as controlador
import ClasesDominios.Cabina as cabina
import ClasesDominios.Persona as per
import ClaseImplementacion.Instanciador_cabinas as cabinas
import ClaseImplementacion.Instanciador_lugares as lugares
import ClaseImplementacion.Pantalla as pantalla
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5
import random
import barcode

class FuncionesPrincipales:
    '''Abstracción que representa a una función que realiza las tareas principales'''
    def __init__(self):
        self.aux = 0
        self.lugar = 0

    def reservar_vuelo(self, n_pais):
        '''Función que reserva un vuelo'''
        lugar = lugares.InstanciadorLugares()
        dicc = {'Buenos Aires':lugar.instanciar_bsas,
                'Rio de Janeiro':lugar.instanciar_rio,
                'Lima':lugar.instanciar_lima,
                'Guayaquil':lugar.instanciar_guayaquil,
                'Madrid':lugar.instanciar_madrid,
                'Miami':lugar.instanciar_miami,
                'Punta Cana':lugar.instanciar_punta,
                'Paris': lugar.instanciar_paris,
                'Cancún':lugar.instanciar_cancun,
                'Montevideo':lugar.instanciar_montevideo,
                'Bogotá':lugar.instanciar_bogota,
                'La Paz':lugar.instanciar_lapaz}

        if n_pais in dicc:
            self.lugar = dicc[n_pais]()
            return self.lugar

    def imprimir_comprobante(self, reserva):
        '''Funcion que imprime un comprobante de vuelo'''
        self.aux = canvas.Canvas(reserva.pasajero.nombre + '.pdf', pagesize = A5)
        self.aux.drawString(150, 550, "LTAM SERVICE ONLINE")
        self.aux.drawString(130, 530, "COMPROBANTE DE RESERVA")
        textobject = self.aux.beginText()
        textobject.setTextOrigin(40, 500)
        textobject.setFont("Courier", 13)
        lineas_texto = str(reserva)
        textobject.textLines(lineas_texto)
        self.aux.drawText(textobject)
        generador = "0"
        for num in range (9):
            generador = generador + str(random.randrange(10))
        isbn = barcode.ISBN13("978" + generador, writer=barcode.writer.ImageWriter())
        filename = isbn.save(reserva.pasajero.nombre)
        self.aux.drawImage(filename, 13, 20, width=400, height=80)
        self.aux.showPage()
        self.aux.save()
