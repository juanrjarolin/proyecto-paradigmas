from abc import ABCMeta, abstractmethod
class Cabina(metaclass=ABCMeta):
    '''Abstracción que representa a una cabina'''

    def __init__(self, precio, nombre):
        self.precio = precio
        self.nombre = nombre

    def __str__(self):
        return 'Precio: ' + str(self.precio) + ' US$' + '\n' + 'Cabina: ' + self.nombre

    def max_pasajeros(self, pasajero):
        self.cant_pasajeros =  pasajero.bebes + pasajero.niños + pasajero.adultos
        return self.cant_pasajeros

    @abstractmethod
    def descripcion_cabina(self):
        pass

class CabinaEspecial(Cabina, metaclass=ABCMeta): #Clase Premium Business, el mejor servicio para el pasajero
    '''Abstracción que representa a una cabina especial'''
    def __init__(self, precio, nombre):
        Cabina.__init__(self, precio, nombre)
        self.bienvenida = ""
        self.desc_1 = ""
        self.desc_2 = ""
        self.desc_3 = ""
        self.ficha_tecnica1 = ""
        self.ficha_tecnica2 = ""
        self.ficha_tecnica3 = ""

    @classmethod
    def descripcion_cabina(self):
        self.bienvenida = "Relájate en asientos de última generación que se convierten en cama." \
                     " Disfruta el más cálido servicio a bordo y deléitate con una carta\nde alta cocina diseñada" \
                     " por destacados chefs y vinos escogidos por el sommelier más premiado de Sudamérica." \
                     "\n¡Prepárate a vivir la experiencia Premium Business!"

        #Descripcion 1
        self.desc_1= "Esta clase ha sido especialmente diseñada para que tu vuelo se transforme " \
                "en un verdadero descanso. El rediseño de la cabina y los asientos\n-cama harán " \
                "que disfrutes de un sueño perfecto y placentero."

        self.ficha_tecnica1 = "Los asientos bajan a una posición 100% horizontal, transformándose en una cama" \
                         " de 23 pulgadas de ancho por 73 de largo.\nLa distancia entre asientos se aumentó" \
                         " a 74 pulgadas, un 32% más por pasajero, muy por encima de lo ofrecido\n" \
                         " por otras líneas aéreas."

        #descripcion 2
        self.desc_2 = "Déjate cautivar con el sistema de entretenimiento de última\n generación y disfruta del placer" \
                 " de una buena película o\npieza de música el que sumado a una atención personalizada\nhacen de esta"\
                 "clase una experiencia inolvidable."

        self.ficha_tecnica2 = "Cada asiento cuenta con una pantalla de alta resolución de 15,4\npulgadas y un sistema de" \
                         " audio-video que se puede usar libremente.\nÉste cuenta con un repertorio de 110 películas" \
                         "- 12 estrenos\n8 hits recientes, 10 latinas, 10 infantiles y 70 clásicos" \
                         "\nde todos los tiempos" \
                         "-, 42 programas de TV, 3 series con temporada\ncompleta, más de 1000 CD’s de música" \
                         " y 25 juegos."

        #descripcion 3
        self.desc_3 = "En Premium Business recibirás un nivel de servicio que muy pocas\naerolíneas en el mundo" \
                 " pueden entregar.Se trata de un nuevo concepto de viaje\nbasado en lo que los pasajeros" \
                 " más valoran en sus vuelos: el cuidado del descanso\ny un servicio de excelencia." \
                 "Encántate con la calidez de los tripulantes y\nsorpréndete con el exquisito menú" \
                 " y fantástica carta de vinos."

        self.ficha_tecnica3 = "Contamos con un menú especialmente elaborado por reconocido chefs, que incorpora" \
                         "\nproductos naturales característicos de esta región sudamericana." \
                         "\nAdemás, tenemos una selección de los más nobles vinos de esta zona del mundo\n" \
                         "elaborada por el único Master Sommelier en Latinoamérica, Héctor Vergara."

class CabinaIntermedia(Cabina, metaclass=ABCMeta): #Clase Premium Economy, exclusivo para viaje de negocios
    '''Abstracción que representa a una cabina tipo intermedia'''
    def __init__(self, precio, nombre):
        Cabina.__init__(self, precio, nombre)
        self.desc_1 = ""
        self.desc_2 = ""
        self.desc_3 = ""
        self.ficha_tecnica = ""

    @classmethod
    def descripcion_cabina(self):
        #Descripcion 1
        self.desc_1 = "Descubre nuestra Premium Economy, la clase que responde a lo más valorado por los pasajeros" \
                 " que viajan por negocios: aprovechar al máximo su tiempo.\nEn esta cabina exclusiva" \
                 " y de atención preferente, encontrarás todo el espacio y comodidad que necesitas para tu viaje."

        self.ficha_tecnica = "Es una cabina exclusiva y con atención preferente para sólo 12 personas. Posee butacas" \
                         " de cuero y\nun asiento central cuyo respaldo se convierte en mesa" \
                         " para que obtengas un mayor espacio y\ncomodidad especial para un computador portátil." \
                         " Además, posee mayor reclinación y espacio entre\nasientos para máxima comodidad."

        # Descripcion 2
        self.desc_2 = "Para una mayor comodidad, algunos de nuestros aviones que cuentan con esta cabina" \
                 "\ntienen una conexión universal para cargar la batería de computadores, iPod, reproductor de DVD" \
                 "\no juegos electrónicos. Además del moderno sistema de entretenimiento a bordo con" \
                 "\npantallas generales y canales individuales de audio, está disponible una amplia" \
                 "\nselección de revistas y diarios."

        # Descripcion 3
        self.desc_3 = "Esta clase fue especialmente diseñada para responder a lo que los\npasajeros de negocios" \
                 " más valoran en los vuelos de corta duración:\nel cuidado de su tiempo y un servicio de excelencia." \
                 "En esta clase podrás\naprovechar todas las ventajas de un servicio Premium," \
                 " volando en Economy:\nacceso a salones VIP asiento en primeras filas con el asiento" \
                 "\ncentral bloqueado, Check-in y embarque preferente, desembarque y salida\nde equipaje preferente" \
                 "servicio a bordo de Premium Business, acumulación\nde kms." \
                 " Mayor franquicia de equipaje (3 piezas de 23 kgs. cada una)."

class CabinaEconomica(Cabina, metaclass=ABCMeta):
    '''Abstracción que representa a una cabina tipo económica'''
    def __init__(self, precio, nombre):
        Cabina.__init__(self, precio, nombre)
        self.desc_1 = ""
        self.desc_2 = ""
        self.desc_3 = ""
        self.ficha_tecnica = ""

    @classmethod
    def descripcion_cabina(self):
        #Descripción 1
        self.desc_1 = "Descubre nuestra clase Economy, que con sus tapices renovados, mayor entretenimiento" \
                 " y la más cálida atención, creará toda una experiencia\nde vuelo para recordar. " \
                 "Disfruta de los asientos con diseño ergonómico, reclinables y con apoya-cabeza\najustable," \
                 " pensados únicamente en tu comodidad."

        # Descripción 2
        self.desc_2 = "A veces son muchas horas de viaje que te separan de tu destino, pero cuando todo el vuelo" \
                 " ha sido pensado para ti, el tiempo y la distancia desaparecen.\n" \
                 "Sorpréndete y disfruta del sistema de entretenimiento individual con música, videos y juegos" \
                 " para todos los gustos."

        # Descripción 3
        self.desc_3 = "Desde los simples detalles de nuestra atención, como una sonrisa, queremos transmitirte" \
                 " nuestro propósito permanente de ofrecerte el mejor servicio a bordo.\n" \
                 "Además disfruta de los sabores, olores y colores que fueron especialmente elegidos en las comidas" \
                 " y snacks de la clase Economy."

        self.ficha_tecnica = "El sistema de entretenimiento a bordo está disponible en nuestros aviones " \
                             "Alitalia 222, Boeing 777 y Airbus 330."

        return '\n\n3. BIENVENIDO A LA EXPERIENCIA ECONOMY' + '\n\n>>AMBIENTE Y COMODIDAD<<'\
               + self.desc_1 + '\n\n>>VUELOS MÁS CORTOS GRACIAS A NUESTRO ENTRETENIMIENTO A BORDO<<' + self.desc_2 \
               +'\n\n' + '>>CALIDAD EN SERVICIO<<' + self.desc_3 + '\n' + 'FICHA TÉCNICA' + self.ficha_tecnica