import ClasesDominios.Vuelo as vuelo

class InstanciadorAviones:
    '''Abstracción que representa a un instanciador de aviones'''
    def __init__(self):
        pass

    def instanciar_airbus330(self):
        '''Función que crea el tipo de avión airbus 330'''
        airbus330 = vuelo.Avion('Airbus 330')
        return airbus330

    def instanciar_boeing777(self):
        '''Función que crea el tipo de avión boeing 777'''
        boeing777 = vuelo.Avion('Boeing 777')
        return boeing777

    def instanciar_airbus880(self):
        '''Función que crea el tipo de avión Airbus 880'''
        airbus880 = vuelo.Avion('Airbus 880')
        return airbus880

    def instanciar_boeing787(self):
        '''Función que crea el tipo de avión Boeing 787'''
        boeing787 = vuelo.Avion('Boeing 787')
        return boeing787

    def instanciar_Alitalia222(self):
        '''Función que crea el tipo de avión Alitalia 222'''
        alitalia222 = vuelo.Avion('Alitalia 222')
        return alitalia222

    def instanciar_Alitalia333(self):
        '''Función que crea el tipo de avión Alitalia 333'''
        alitalia333 = vuelo.Avion('Alitalia 333')
        return alitalia333

    def instanciar_Alitalia455(self):
        '''Función que crea el tipo de avión Alitalia 455'''
        alitalia455 = vuelo.Avion('Alitalia 455')
        return alitalia455