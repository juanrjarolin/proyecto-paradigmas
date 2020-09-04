from datetime import datetime
from tkinter.messagebox import showinfo, showerror, showwarning
class ErrCont(Exception):
    '''Mi excepción Error contacto'''
    def __init__(self, valor):
        showerror('Error', 'No se reconoce '+valor+'.')

class ErrVacio(Exception):
    '''Error campo vacio'''
    def __init__(self):
        showerror('Error', 'Campo vacío')
                        
class ControladorPasajero:
    def __init__(self):
        self.edad_superior = 18
        self.digito_minimo_ced = 5 #teniendo en cuenta otras nacionalidades
        self.digito_cont = 12

    def validar_cedula(self, pasajero):
        '''Función que valida una cédula'''
        try:
            self.ced = int(pasajero.cedula)
            if self.ced == 0 or self.ced < 0:
                raise ValueError
            elif len(pasajero.cedula) < self.digito_minimo_ced:
                raise ValueError
            return True
        except ValueError:
            showerror('Error', 'Cédula no válida.')
            return False

    def validar_fecha_nacimiento(self, pasajero):
        '''Función que valida la fecha de nacimiento del pasajero'''
        formato = "%d/%m/%Y"

        fecha_hoy = datetime.now()
        try:
            año = pasajero.fecha_nacimiento[6:]
            pasajero.fecha_nacimiento = datetime.strptime(pasajero.fecha_nacimiento, formato).date()
            pasajero.edad = fecha_hoy.year - int(año)
            if pasajero.edad < self.edad_superior:
                showwarning('Advertencia', 'Usted es menor de edad, no puede hacer la reserva')
                return False
            else:
                return True
        except ValueError:
            showerror('Error', 'Fecha y/o formato de fecha no válidos.'+'\nFormato requerido: dd/mm/aaaa')
            return False
    
    def validad_contacto(self, pasajero):
        '''Función que valida el contacto del pasajero'''
        texto = 'TIGO: 981-986\tPERSONAL: 971-973, 975-976\nCLARO: 991-994\t VOX: 961-962'
        rangos = ['981','982','983','984','985','986','991','992','993','994','971','972','973','975','976'
                  ,'961','962']
        try:
            contac = int(pasajero.contacto)#se produce una excepción si contiene letras
            long = len(str(contac))#longitud del contacto ingresado
            #si la longitud es inferior o superior del digito establecido
            if  long < self.digito_cont or long > self.digito_cont :
                raise ValueError
            #si el tipo de contacto no se encuentra
            if not str(contac)[3:6] in rangos:
                raise ErrCont(str(contac)[3:6])
            return True
        except ValueError:
            showerror('Error', 'Contacto no válido.')
            return False
        except ErrCont:
            showwarning('Atención', texto)
            return False
            

    def validar_nombre(self, pasajero):
        '''Función que valida campos vacíos, numéricos, alfanuméricos y letras minúsculas en nombre'''
        try:
            if pasajero.nombre == "" or not pasajero.nombre.isalpha():
                raise ErrVacio
            else:
                pasajero.nombre = pasajero.nombre.capitalize()
                return True
        except ErrVacio:
            showwarning('Advertencia', 'No debe haber campos vacíos')
            return False

    def validar_apellido(self, pasajero):
        '''Función que valida campos vacíos, numéricos, alfanuméricos y letras minúsculas en apellido'''
        try:
            if pasajero.apellido == "" or not pasajero.apellido.isalpha():
                raise ErrVacio
            else:
                pasajero.apellido = pasajero.apellido.capitalize()
                return True
        except ErrVacio:
            showwarning('Advertencia', 'No debe haber campos vacíos')
            return False

    def validar_correo(self, pasajero):
        '''Función que valida el correo electrónico ingresado'''
        import re
        try:
            if not re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', pasajero.correo.lower()):
                raise SyntaxError
            return True
        except SyntaxError:
            showerror('Error Correo', 'Campo vacío o error de caracteres.')
            return False

    def validar_nacionalidad(self, pasajero):
        try:
            if pasajero.nacionalidad == "" or not pasajero.nacionalidad.isalpha():
                raise ErrVacio
            else:
                pasajero.nacionalidad = pasajero.nacionalidad.capitalize()
                return True
        except ErrVacio:
            showwarning('Advertencia', 'No debe haber campos vacíos')
            return False

    def validar_direccion(self, pasajero):
        try:
            if pasajero.direccion == "":
                raise ErrVacio
            return True
        except ErrVacio:
            showwarning('Advertencia', 'No debe haber campos vacíos')
            return False
