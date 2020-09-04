import ClaseImplementacion.Instanciador_vuelos as vuelos
import ClasesDominios.Vuelo as vuelo
class InstanciadorLugares:
    '''Abstracción que representa a un instanciador de lugar'''
    def __init__(self):
        self.instanciador_v = vuelos.InstaciadorVuelos()

    def instanciar_bsas(self):
        '''Función que crea el lugar buenos aires y la cantidad de vuelos disponibles'''
        precio1 = vuelo.Precio(266, "No disponible", 500)
        buenos_aires = vuelo.Lugar('Buenos Aires', 'Ministro Pistorini', precio1)
        buenos_aires.cant_vuelos = self.instanciador_v.instanciar_vuelo()
        return buenos_aires

    def instanciar_rio(self):
        '''Función que crea el lugar de rio de janeiro y la cantidad de vuelos disponibles'''
        precio2 = vuelo.Precio(289, "No disponible", 635)
        rio = vuelo.Lugar('Rio de Janeiro', 'Galeão', precio2)
        rio.descripcion_rio()
        rio.cant_vuelos = self.instanciador_v.instanciar_vuelo()

        return rio

    def instanciar_cancun(self):
        '''Función que crea el lugar de Cancún México y la cantidad de vuelos disponibles'''
        precio3 = vuelo.Precio(728, "No disponible", 2058)
        cancun = vuelo.Lugar('Cancún', 'Benito Juárez', precio3)
        cancun.descripcion_cancun()
        cancun.cant_vuelos = self.instanciador_v.instanciar_vuelo()

        return cancun

    def instanciar_bogota(self):
        '''Función que crea el lugar de Bogotá Colombia y la cantidad de vuelos disponibles'''
        precio4 = vuelo.Precio(481, "No disponible", 1661)
        bogota = vuelo.Lugar('Bogotá', 'El Dorado', precio4)
        bogota.descripcion_bogota()
        bogota.cant_vuelos = self.instanciador_v.instanciar_vuelo()

        return bogota

    def instanciar_lima(self):
        '''Función que crea el lugar de Lima Perú'''
        precio5 = vuelo.Precio(250, "No disponible", 925)
        lima = vuelo.Lugar('Lima', 'Jorge Chávez', precio5)
        lima.descripcion_lima()
        lima.cant_vuelos = self.instanciador_v.instanciar_vuelo()

        return lima

    def instanciar_punta(self):
        '''Función que crea el lugar de Punta Cana República Dominicana'''
        precio6 = vuelo.Precio(135, 792, 1912)
        punta = vuelo.Lugar('Punta Cana', 'Las Américas', precio6)
        punta.descripcion_puntacana()
        punta.cant_vuelos = self.instanciador_v.instanciar_vuelo()

        return  punta

    def instanciar_madrid(self):
        '''Función que crea el lugar de Madrid España'''
        precio7 = vuelo.Precio(1189, "No disponible", 3709)
        madrid = vuelo.Lugar('Madrid', 'Adolfo Suárez', precio7)
        madrid.descripcion_madrid()
        madrid.cant_vuelos = self.instanciador_v.instanciar_vuelo()

        return madrid

    def instanciar_paris(self):
        '''Función que crea el lugar de París Francia'''
        precio8 = vuelo.Precio(1038, "No disponible", 3632)
        paris = vuelo.Lugar('París', 'París-Charles de Gaulle', precio8)
        paris.descripcion_paris()
        paris.cant_vuelos = self.instanciador_v.instanciar_vuelo()

        return paris

    def instanciar_montevideo(self):
        '''Función que crea el lugar de Montevideo Uruguay'''
        precio9 = vuelo.Precio(191, "No disponible", 602)
        monte = vuelo.Lugar('Montevideo', 'Carrasco', precio9)
        monte.descripcion_montevideo()
        monte.cant_vuelos = self.instanciador_v.instanciar_vuelo()

        return monte

    def instanciar_guayaquil(self):
        '''Función que crea el lugar de Guayaquil Ecuador'''
        precio10 = vuelo.Precio(398, "No disponible", 1153)
        guayaquil = vuelo.Lugar('Guayaquil', 'José Joaquín de Olmedo', precio10)
        guayaquil.descripcion_guayaquil()
        guayaquil.cant_vuelos = self.instanciador_v.instanciar_vuelo()

        return guayaquil

    def instanciar_lapaz(self):
        '''Función que crea el lugar de La Paz Bolivia'''
        precio11 = vuelo.Precio(209, "No disponible", "No disponible")
        lapaz = vuelo.Lugar('La Paz', 'El Alto', precio11)
        lapaz.descripcion_lapaz()
        lapaz.cant_vuelos = self.instanciador_v.instanciar_vuelo()

        return lapaz

    def instanciar_miami(self):
        '''Función que crea el lugar de Miami Estados Unidos'''
        precio12 = vuelo.Precio(841, "No disponible", 3277)
        miami = vuelo.Lugar('Miami', 'Miami', precio12)
        miami.descripcion_miami()
        miami.cant_vuelos = self.instanciador_v.instanciar_vuelo()

        return miami