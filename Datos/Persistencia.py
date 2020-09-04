import pickle
class PersistenciaP:
    '''Abstracción que representa a una persistencia pickle'''
    def __init__(self):
        pass

    @classmethod
    def save(cls, fileName, data):
        '''Función que guarda la reserva del usuario'''
        try:
            with open(fileName + '.data', 'wb') as mydata:
                pickle.dump(data, mydata)
        except pickle.PickleError as err:
            print(str(err))

    @classmethod
    def load(cls, fileName):
        '''Función que carga la reserva o deserializa los datos ingresados'''
        try:
            with open(fileName + '.data', 'rb') as readData:
                return pickle.load(readData)
        except pickle.PickleError as err2:
            print(str(err2))