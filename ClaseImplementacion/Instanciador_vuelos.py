from datetime import datetime, time
import ClaseImplementacion.Instanciador_Aviones as aviones
import ClasesDominios.Vuelo as vuelo

class InstaciadorVuelos:
    '''Abstracción que representa un instanciador de vuelo'''
    def __init__(self):
        self.vuelos = 0
        self.instanciador_a = aviones.InstanciadorAviones()

    def instanciar_vuelo(self):
        fecha = datetime.now().date()

        avion1 = self.instanciador_a.instanciar_Alitalia222()
        avion2 = self.instanciador_a.instanciar_airbus330()
        avion3 = self.instanciador_a.instanciar_airbus880()
        avion4 = self.instanciador_a.instanciar_Alitalia333()
        avion5 = self.instanciador_a.instanciar_Alitalia455()
        avion6 = self.instanciador_a.instanciar_boeing777()
        avion7 = self.instanciador_a.instanciar_boeing787()

        hora1 = time(7, 0, 0)
        hora2 = time(9, 0, 0)
        hora3 = time(10, 0, 0)
        hora4 = time(13, 0, 0)
        hora5 = time(15, 0, 0)
        hora6 = time(17, 10, 0)
        hora7 = time(23, 50, 0)

        vuelo1 = vuelo.Vuelo('AZW 28', avion1, fecha, hora1)
        vuelo2 = vuelo.Vuelo('AQT 20', avion2, fecha, hora2)
        vuelo3 = vuelo.Vuelo('TER 22', avion3, fecha, hora3)
        vuelo4 = vuelo.Vuelo('AQS 28', avion4, fecha, hora4)
        vuelo5 = vuelo.Vuelo('AEW 10', avion5, fecha, hora5)
        vuelo6 = vuelo.Vuelo('ADR 33', avion6, fecha, hora6)
        vuelo7 = vuelo.Vuelo('QQA 54', avion7, fecha, hora7)

        self.vuelos = [vuelo1, vuelo2, vuelo3, vuelo4, vuelo5, vuelo6, vuelo7]

        return self.vuelos