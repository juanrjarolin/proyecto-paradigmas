from abc import ABCMeta

class Vuelo(metaclass=ABCMeta):
    '''Abstracción que representa a un vuelo'''
    def __init__(self, codigo, avion, fecha_partida, horario_partida):
        self.aeropuerto_origen = "Silvio Pettirossi"
        self.pais_origen = "Paraguay"
        self.codigo = codigo
        self.avion = avion
        self.fecha_partida = fecha_partida
        self.horario_partida = horario_partida
        self.estado = ""
        self.habilitado = ""

    def __str__(self):
        return self.codigo + 2*'\t' + str(self.avion) + '\t'\
        + str(self.horario_partida) + 2*'\t' \
        + str(self.fecha_partida) + '\t' + self.estado

    def cambiar_estado(self, estado):
        '''Cambia el estado del vuelo'''
        self.estado = estado

    def cambiar_habilitacion(self, habilitacion_vuelo):
        '''Cambia la habilitación del vuelo'''
        self.habilitado = habilitacion_vuelo


class Reserva(metaclass=ABCMeta):
    '''Abstracción que representa a una reserva'''
    def __init__(self, pasajero, lugar, cabina, vuelo, cantidad_pasajero):
        self.pasajero = pasajero
        self.lugar = lugar
        self.cabina = cabina
        self.vuelo = vuelo
        self.cantidad_pasajero = cantidad_pasajero

    def obtener_cantidad_pasajero(self):
        total = str(self.cantidad_pasajero[0] + self.cantidad_pasajero[1] + self.cantidad_pasajero[2])
        return total

    def __str__(self):
        return str(self.pasajero) + '\n' + str(self.lugar) + '\n' + str(self.cabina) \
            + '\n' + 'Aeropuerto de partida: ' + self.vuelo.aeropuerto_origen + '\n'\
            + 'Cantidad de pasajeros: ' + self.obtener_cantidad_pasajero()\
            + '\n'+ 'Código de Avión: ' + self.vuelo.codigo + '\n' + 'Tipo de Avión: ' \
            + str(self.vuelo.avion) + '\n' + 'Horario de partida: ' + str(self.vuelo.horario_partida) \
            + '\n' + 'Fecha de partida: ' + str(self.vuelo.fecha_partida) + '\n' \
            + 'Estado del vuelo: ' + self.vuelo.estado

    def __del__(self):
        return 'Ha cancelado su reserva.'

    def eliminar_reserva(self, reserva):
        del(reserva)

class Precio(metaclass=ABCMeta):
    '''Abstracción que representa a un precio'''
    def __init__(self, precio_economico, precio_intermedio, precio_especial):
        self.precio_economico = precio_economico
        self.precio_intermedio = precio_intermedio
        self.precio_especial = precio_especial

    def __str__(self):
        return 'Precio Especial en US$: ' + str(self.precio_especial) + '\n' \
            'Precio Intermedio en US$: ' + str(self.precio_intermedio) + '\n' \
            'Precio Económico en US$: ' + str(self.precio_economico)


class Lugar(metaclass=ABCMeta):
    '''Abstracción que representa a un lugar'''
    def __init__(self, nombre, aeropuerto, precio):
        self.nombre = nombre
        self.aeropuerto = aeropuerto
        self.precio = precio
        self.descripcion = ""
        self.cant_vuelos = []

    def __str__(self):
        return 'Lugar: ' + self.nombre + '\n' + 'Aeropuerto destino: ' + self.aeropuerto



    def descripcion_bsas(self):
        '''Descripción buenos aires'''
        self.descripcion = "¡LTAM te invita a conocer las ciudades más bellas de Argentina!\n" \
                           "¿Qué tal una noche de tango con una parrillada o una escapada a\n" \
                           "la Patagonia?\n" \
                           "Aprovecha los vuelos a Buenos Aires, compra tus pasajes ahora mismo\n" \
                           "y disfruta de esta hermosa ciudad."
        return self.descripcion

    def descripcion_cancun(self):
        '''Descripción Cancún'''
        self.descripcion = "¡No te quedes sin volar! Si estás pensando en viajar, " \
                           "te recomendamos\nconocer las playas caribeñas de Cancún y " \
                           "todas sus atracciones.\nAprovecha los vuelos a Cancún, " \
                           "compra ahora tus pasajes y comienza\na disfrutar desde " \
                           "ahora tu próxima aventura."
        return self.descripcion

    def descripcion_rio(self):
        '''Descripción Rio de Janeiro'''
        self.descripcion = "No te puedes perder los increíbles destinos que Brasil te ofrece." \
                           "\nLTAM te invita a recorrer sus playas paradisíacas, ciudades y pueblos" \
                           "\nllenos de alegría. Aprovecha los vuelos a Río de Janeiro, compra ahora\n" \
                           "tus pasajes y disfruta de esta ciudad."
        return self.descripcion

    def descripcion_bogota(self):
        '''Descripción Bogotá'''
        self.descripcion = "LTAM quiere que viajes a los increíbles destinos que Colombia\nte ofrece." \
                           " Con playas hermosas, el país del café te invita a descansar y\ndivertirte." \
                           " Aprovecha los vuelos a Bogotá, compra ahora tus pasajes y \ndisfruta de esta ciudad."
        return self.descripcion

    def descripcion_lima(self):
        '''Descripción Lima'''
        self.descripcion = "LTAM te invita a conocer los increíbles destinos que Perú ofrece." \
                           "\nAprovecha los vuelos a Lima, compra ahora tus pasajes y comienza\na disfrutar " \
                           "de todas las atracciones que esta hermosa ciudad\ntiene para ti."
        return self.descripcion

    def descripcion_montevideo(self):
        '''Descripción Montevideo'''
        self.descripcion = "¿Qué tal disfrutar de un recorrido por Pocitos o encantarte\ncon su " \
                           "exquisita gastronomía? Todo eso y más te lo ofrece Uruguay." \
                           "\nAprovecha los vuelos a Montevideo, compra ahora tus pasajes " \
                           "y disfruta\nde esta ciudad."
        return self.descripcion

    def descripcion_guayaquil(self):
        '''Descripción Punta Cana'''
        self.descripcion = "LTAM te invita a recorrer los increíbles destinos que Ecuador te ofrece. " \
                           "\nVisita la mitad del mundo o las Islas Galápagos y sus especies únicas\n" \
                           "en el planeta. Aprovecha los vuelos a Guayaquil, compra ahora tus\npasajes " \
                           "y disfruta de esta ciudad."
        return self.descripcion

    def descripcion_lapaz(self):
        '''Descripción La Paz'''
        self.descripcion = "LTAM te invita a volar a los increíbles destinos que Bolivia te ofrece." \
                           "\nCulturas únicas incrustadas en paisajes rústicos, llenos de belleza y\n encanto." \
                           "Aprovecha los vuelos a La Paz, compra ahora tus pasajes y\n disfruta de esta ciudad."
        return self.descripcion

    def descripcion_miami(self):
        '''Descripción Miami'''
        self.descripcion = "LTAM te invita a conocer los increíbles destinos que Estados Unidos ofrece." \
                           "\nAprovecha los vuelos a Miami, compra ahora tus pasajes y comienza\n" \
                           "a disfrutar de todas las atracciones que esta hermosa ciudad tiene para ti."
        return self.descripcion

    def descripcion_madrid(self):
        '''Descripción Madrid'''
        self.descripcion = "LTAM te invita a conocer los increíbles destinos que España ofrece." \
                           "\nAprovecha los vuelos a Madrid, compra ahora tus pasajes y comienza a\n " \
                           "disfrutar de todas las atracciones que esta hermosa ciudad tiene para ti."
        return self.descripcion

    def descripcion_paris(self):
        '''Descripción París'''
        self.descripcion = "LTAM te invita a conocer los increíbles destinos que Francia ofrece." \
                           "\nAprovecha los vuelos a París, compra ahora tus pasajes y comienza a\n" \
                           "disfrutar de todas las atracciones que esta hermosa ciudad tiene\npara ti."
        return self.descripcion

    def descripcion_puntacana(self):
        self.descripcion = "¡No te quedes sin volar! Si estás pensando en viajar, te recomendamos\n" \
                           "conocer las playas caribeñas de República Dominicana y todas sus\natracciones." \
                           "Aprovecha los vuelos a Punta Cana, compra ahora tus pasajes y\ncomienza a disfrutar."
        return self.descripcion

class Avion(metaclass=ABCMeta):
    '''Abstracción que representa a un avión'''
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre
