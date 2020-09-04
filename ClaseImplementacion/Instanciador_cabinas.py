import ClasesDominios.Cabina as cabina

class InstanciadorCabina:
    '''Abstracción que representa a un instanciador de cabina'''
    def __init__(self):
        self.cabina_especial = 0
        self.cabina_intermedia = 0
        self.cabina_economica = 0

    def instanciar_cabina_especial(self, precio):
        '''Función que instancia un tipo de cabina'''
        if precio.precio_especial == 'No disponible':
            return False
        else:
            self.cabina_especial = cabina.CabinaEspecial(precio.precio_especial, 'Especial')
            return self.cabina_especial

    def instanciar_cabina_economica(self, precio):
        '''Función que instancia un tipo de cabina'''
        if precio.precio_economico == 'No disponible':
            return False
        else:
            self.cabina_economica = cabina.CabinaEconomica(precio.precio_economico, 'Económica')
            return self.cabina_economica

    def instanciar_cabina_intermedia(self, precio):
        '''Función que instancia un tipo de cabina'''
        if precio.precio_intermedio == 'No disponible':
            return False
        else:
            self.cabina_intermedia = cabina.CabinaIntermedia(precio.precio_intermedio, 'Intermedia')
            return self.cabina_intermedia