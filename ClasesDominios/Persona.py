import ClasesControladores.Controlador_pasajero as controlador
from abc import ABCMeta
class Persona(metaclass=ABCMeta):
    '''Abstracción que representa a una persona'''

    def __init__(self, nombre, apellido, fecha_nacimiento, cedula, direccion, contacto, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = 0
        self.cedula = cedula
        self.direccion = direccion
        self.contacto = contacto
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.cant_max = 9 #cantidad máxima de personas

    def __str__(self):
        return 'Nombre:  ' + self.nombre + '\n' + 'Apellido: ' + self.apellido \
            + '\n' + 'Edad: ' + str(self.edad) + '\n' + 'Cédula: ' + str(self.cedula) \
            + '\n' + 'Dirección: ' + self.direccion + '\n' + 'Contacto: ' + str(self.contacto)\
            + '\n' + 'Correo electrónico: ' + str(self.correo) + '\n' \
            + 'Fecha de nacimiento: ' + str(self.fecha_nacimiento)


class Pasajero(Persona, metaclass=ABCMeta):
    '''Abstracción que representa a un pasajero'''
    def __init__(self, nombre, apellido, fecha_nacimiento, cedula, direccion, contacto, correo, nacionalidad):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, cedula, direccion, contacto, correo)
        self.nacionalidad = nacionalidad

    def __str__(self):
        return Persona.__str__(self) \
            + '\n' + 'Nacionalidad: ' + self.nacionalidad
