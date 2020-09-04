#!/usr/bin/python env
import os
from datetime import datetime, time
os.chdir(os.getcwd() + '/Datos/Archivos') #se define el lugar de trabajo
import ClasesDominios.Vuelo as reserva
import ClaseImplementacion.FuncionesPrincipales as funcion
import ClaseImplementacion.Instanciador_lugares as lugares
import ClasesControladores.Controlardor_vuelo as controlar_vuelo
import Datos.Persistencia as persistencia
import ClaseImplementacion.Pantalla as pantalla
from tkinter import *
maximo_pasajeros = 9
'''@author: Juan Roberto Jarolin Morán'''

class Aplicacion:
    '''Abstracción que representa a una aplicación'''
    contador_reserva = 0
    def __init__(self):
        self.opcion_menu = 0
        self.operaciones = 0
        self.habilidado = ""
        self.estado = ""
        self.vuelo = 0
        self.reserva_pasajero = 0
        self.pasajero = 0
        self.pais = ""
    # ______________________________________________________________________________________________________#

    def viajes(self):
        '''Función que permite visualizar los diferentes países para viajar'''
        while True:
            pantalla.Pantalla.limpiar_pantalla()
            print()
            pantalla.Pantalla.mostrar_titulo('VIAJES')
            print('1. Buenos Aires (Argentina)' + '\t\t' + '8. Miami (EE. UU.)')
            print('2. Rio de Janeiro (Brasil)' + '\t\t' + '9. Madrid (España)')
            print('3. Montevideo (Uruguay)' + '\t\t\t' + '10. París (Francia)')
            print('4. La Paz (Bolivia)' + '\t\t\t\t' + '11. Punta Cana (República Dominicana)')
            print('5. Lima (Perú)' + '\t\t\t\t\t' + '12. Cancún (México)')
            print('6. Guayaquil (Ecuador)')
            print('7. Bogotá (Colombia)')

            self.operaciones = {1: lugares.InstanciadorLugares.instanciar_bsas,
                                2: lugares.InstanciadorLugares.instanciar_rio,
                                3: lugares.InstanciadorLugares.instanciar_montevideo,
                                4: lugares.InstanciadorLugares.instanciar_lapaz,
                                5: lugares.InstanciadorLugares.instanciar_lima,
                                6: lugares.InstanciadorLugares.instanciar_guayaquil,
                                7: lugares.InstanciadorLugares.instanciar_bogota,
                                8: lugares.InstanciadorLugares.instanciar_miami,
                                9: lugares.InstanciadorLugares.instanciar_madrid,
                                10: lugares.InstanciadorLugares.instanciar_paris,
                                11: lugares.InstanciadorLugares.instanciar_punta,
                                12: lugares.InstanciadorLugares.instanciar_cancun}

            while True:
                try:
                    self.opcion_menu = int(input('\nIngrese la opción para la descripción y precios o "0"'
                                     ' para salir: '))
                    if self.opcion_menu == 0:
                        break
                    self.pais = self.operaciones[self.opcion_menu]()
                    break
                except ValueError:
                    print('Error de valor')
                except KeyError:
                    print('Fuera de rango')


            if self.opcion_menu == 0:
                break
            pantalla.Pantalla.limpiar_pantalla()
            pantalla.Pantalla.mostrar_titulo('DESCRIPCIÓN')
            print(self.pais.descripcion)
            pantalla.Pantalla.mostrar_titulo('PRECIOS')

            if self.pais.precio.precio_economico == False:
                print('Precio económico No disponible')
            else:
                print('Precio económico (US$): ', self.pais.precio.precio_economico)

            if self.pais.precio.precio_intermedio == False:
                print('Precio intermedio No disponible')
            else:
                print('Precio intermedio (US$): ', self.pais.precio.precio_intermedio)

            if self.pais.precio.precio_especial == False:
                print('Precio especial No disponible')
            else:
                print('Precio especial (US$): ', self.pais.precio.precio_especial)

            input('\nPresione cualquier tecla para volver..')

    # ______________________________________________________________________________________________________#

    def cabinas(self):
        '''Función que permite visualizar los diferentes tipos de cabinas'''
        pantalla.Pantalla.limpiar_pantalla()
        while True:
            pantalla.Pantalla.mostrar_titulo('¡ECHA UN VISTASO A NUESTRAS CABINAS!')
            print('1. Cabina Especial')
            print('2. Cabina Intermedia')
            print('3. Cabina Económica')

            self.operaciones = {1: funcion.FuncionesPrincipales.mostrar_cabina_Especial,
                                2: funcion.FuncionesPrincipales.mostrar_cabina_Intermedia,
                                3: funcion.FuncionesPrincipales.mostrar_cabina_Economica}

            while True:
                try:
                    self.opcion_menu = int(input('\nPara ver la descripción de cada una, inserte su '
                                     'código correspondiente o "0" para salir: '))
                    if self.opcion_menu == 0:
                        break
                    else:
                        self.operaciones[self.opcion_menu]()
                        break
                except ValueError:
                    print('Error de valor')
                except KeyError:
                    print('Fuera de rango')

            if self.opcion_menu == 0:
                break

    # ______________________________________________________________________________________________________#

    def reservar(self):
        '''Simulación de una reserva'''
        pantalla.Pantalla.limpiar_pantalla()
        edad_superior = 18
        self.pasajero = funcion.FuncionesPrincipales.crear_pasajero()
        if self.pasajero.edad <= edad_superior:
            print('Usted es menor de edad, no puede hacer la reserva.')
            input('Presione cualquier tecla para continuar...')
            return

        pantalla.Pantalla.limpiar_pantalla()
        inventario = funcion.FuncionesPrincipales.reservar_vuelo()

        if inventario == 0:
            print('Ha cancelado la reserva.')
            return
        else:
            inventario[1].max_pasajeros(self.pasajero)

        while True:
            pantalla.Pantalla.limpiar_pantalla()
            pantalla.Pantalla.mostrar_titulo('SELECCIONE SU VUELO')
            print('  Código' + 3 * '\t' + 'Transporte' + 3 * '\t' + 'Horario' + 4 * '\t' + 'Fecha'
                  + 4 * '\t' + 'Estado')
            self.contador = 0  # contador de vuelos
            for vuelo in inventario[0].cant_vuelos:
                ahora = datetime.now()
                hora_actual = time(ahora.hour, ahora.minute, ahora.second)
                controlar_vuelo.ControlarVuelo.controlar_partida(hora_actual, vuelo)
                print(str(self.contador + 1) + '. ' + str(vuelo) + '\n')
                self.contador = self.contador + 1

            while True:
                try:
                    self.opcion_menu = int(input('\nElija la opción: '))
                    self.vuelo = inventario[0].cant_vuelos[self.opcion_menu - 1]
                    if self.opcion_menu <= 0:
                        print('No válido')
                    else:
                        break
                except IndexError:
                    print('Fuera de rango')

            if self.vuelo.habilitado:
                self.reserva_pasajero = reserva.Reserva(self.pasajero, inventario, self.vuelo)
                persistencia.PersistenciaP.save(str(self.pasajero.cedula), self.reserva_pasajero)
                pantalla.Pantalla.limpiar_pantalla()
                print('¡Ha hecho su reserva!')
                print('Imprima el comprobante y presente en la agencia para '
                      'su posterior confirmación.\n¡Gracias por su preferencia!')
                funcion.FuncionesPrincipales.imprimir_comprobante(self.reserva_pasajero)
                input('\nPulse cualquier tecla para continuar...')
                break
            else:
                print('No puede hacer esta reserva, el vuelo ya partió.\n')
                input('Presione cualquier tecla para continuar...')

    # ______________________________________________________________________________________________________#

    def ver_reserva(self):
        '''Función que hace ver al usuario su reserva, información o cancelación'''

        while True:
            pantalla.Pantalla.limpiar_pantalla()
            pantalla.Pantalla.mostrar_titulo('LTAM SERVICE ONLINE')
            print('\n1. Información de su reserva')
            print('2. Cancelar reserva')

            while True:
                try:
                    self.opcion_menu = int(input('\nIngrese opción o 0 para salir: '))
                    break
                except ValueError:
                    print('Error')

            if self.opcion_menu == 1:
                self.mostrar_reserva()
            elif self.opcion_menu == 0:
                break
            elif self.opcion_menu != 1 and self.opcion_menu != 2:
                print('Opción no válida.')
            else:
                self.cancelar_reserva()

    # ______________________________________________________________________________________________________#

    def mostrar_reserva(self):
        '''Esta función muestra la reserva que hizo un pasajero introduciendo el número de cédula'''
        while True:
            pantalla.Pantalla.limpiar_pantalla()
            pantalla.Pantalla.mostrar_titulo('LTAM SERVICE ONLINE')
            try:
                cedula = int(input('\nIngrese su cedula: '))
                break
            except ValueError:
                print('Error')

        if os.path.isfile(str(cedula) + '.data'): #busca en el directorio Persistencia la reserva hecha
            pantalla.Pantalla.limpiar_pantalla()
            pantalla.Pantalla.mostrar_titulo('LTAM SERVICE ONLINE')
            print()
            print(persistencia.PersistenciaP.load(str(cedula))) #si lo encuentra lo imprime
            input('\nPresione cualquier tecla para continuar...')
        else:
            print('No se ha encontrado su reserva.')
            input('\nPresione cualquier tecla para continuar...')
    #_____________________________________________________________________________________________________#

    def cancelar_reserva(self):
        '''Cancela la reserva del pasajero'''
        while True:
            pantalla.Pantalla.limpiar_pantalla()
            pantalla.Pantalla.mostrar_titulo('LTAM SERVICE ONLINE')
            try:
                cedula = int(input('\nIngrese su cedula: '))
                break
            except ValueError:
                print('Error')

        if os.path.isfile(str(cedula) + '.data'):  # busca en el directorio Persistencia la reserva hecha
            reserva.Reserva.eliminar_reserva(self, self.reserva_pasajero)#elimina el objeto reserva
            os.remove(str(cedula) + '.data') #eliminar el archivo
            print('Se ha cancelado su reserva.')
            input('\nPresione cualquier tecla para continuar...')
        else:
            print('No se ha encontrado su reserva.')
            input('\nPresione cualquier tecla para continuar...')
    #______________________________________________________________________________________________________#

    def menu_cliente(self):
        '''Aquí el cliente podrá ver lugares, precios y tipos de cabina, así también simular una reserva'''
        while True:
            pantalla.Pantalla.limpiar_pantalla()
            pantalla.Pantalla.mostrar_titulo('LTAM SERVICE ONLINE')
            print('1. Viajes')
            print('2. Cabinas')
            print('3. Reservar')
            print('4. Ver reserva')
            print('5. Salir')

            self.operaciones = {1: self.viajes, 2: self.cabinas, 3: self.reservar, 4: self.ver_reserva}

            while True:
                try:
                    self.opcion_menu = int(input('\nIngrese la opción: '))
                    if self.opcion_menu == 5:
                        break
                    else:
                        self.operaciones[self.opcion_menu]()
                        break
                except ValueError:
                    print('Error de valor')
                except KeyError:
                    print('Fuera de rango')

            if self.opcion_menu == 5:
                pantalla.Pantalla.limpiar_pantalla()
                print('¡Hasta pronto!')
                break
#___________________________________________________________________________________________________#
root = Tk()
app = Aplicacion(master=root)
app.mainloop()
