from tkinter import *
from tkinter.messagebox import showinfo
from GUI import Instancias as instancias
from ClasesDominios import Vuelo as vuelo
from ClaseImplementacion import Instanciador_lugares as lugares
from ClasesDominios import Cabina as cabina
from ClaseImplementacion import Instanciador_cabinas as inst
class Mostrador:
    def __init__(self):
        self.lugar = lugares.InstanciadorLugares()

    def crear_interfaz(self, ventana, texto):
        ventana.geometry("600x530+400+125")
        ventana.resizable(width=False, height=False)
        self.lbl_titulo = instancias.MiLabel(ventana, text=texto, font=('Arial', 15), fg='blue', relief=FLAT)
        self.lbl_titulo.pack()

    def mostrar_bsas(self):
        '''Función que muestra descripción del lugar buenos aires'''
        descripcion = vuelo.Lugar.descripcion_bsas(self)
        self.img = PhotoImage(file='buenos.gif')
        text1 = 'Bienvenido a Buenos Aires - Argentina'
        self.img = PhotoImage(file='buenos.gif')
        master1 = Toplevel()
        self.lb_imagen = instancias.MiLabel(master1, image=self.img)
        self.crear_interfaz(master1, text1)
        self.lb_imagen.place(x=-1, y=-1)
        pais = self.lugar.instanciar_bsas()
        self.lb_descripcion = instancias.MiLabel(master1, text=descripcion, font=('Arial', 13,'italic'),
                                                 justify=LEFT)
        self.lb_descripcion.place(x=27, y=30)
        self.mostrar_precio = instancias.MiLabel(master1, text=str(pais.precio), justify=LEFT, font=('Arial',13),
                                                 relief=SUNKEN)
        self.mostrar_precio.place(x=27, y=440)

    def mostrar_rio(self):
        '''Función que crea el lugar de rio de janeiro y la cantidad de vuelos disponibles'''
        descripcion = vuelo.Lugar.descripcion_rio(self)
        master2 = Toplevel()
        self.img = PhotoImage(file='rio.gif')
        self.lb_imagen = instancias.MiLabel(master2, image=self.img)
        self.lb_imagen.place(x=-800, y=-90)
        text1 = 'Bienvenido a Rio de Janeiro - Brasil'
        self.crear_interfaz(master2, text1)
        pais = self.lugar.instanciar_rio()
        self.lb_descripcion = instancias.MiLabel(master2, text=descripcion, font=('Arial', 13,'italic'),
                                                 justify=LEFT)
        self.lb_descripcion.place(x=27, y=30)
        self.mostrar_precio = instancias.MiLabel(master2, text=str(pais.precio), justify=LEFT, font=('Arial', 13),
                                                 relief=SUNKEN)
        self.mostrar_precio.place(x=27, y=440)

    def mostrar_cancun(self):
        '''Función que crea el lugar de Cancún México y la cantidad de vuelos disponibles'''
        descripcion = vuelo.Lugar.descripcion_cancun(self)
        master3 = Toplevel()
        self.img = PhotoImage(file='cancun.gif')
        self.lb_imagen = instancias.MiLabel(master3, image=self.img)
        self.lb_imagen.place(x=-100, y=-1)
        text1 = 'Bienvenido a Cancún - México'
        self.crear_interfaz(master3, text1)
        pais = self.lugar.instanciar_cancun()
        self.lb_descripcion = instancias.MiLabel(master3, text=descripcion, font=('Arial', 13, 'italic'),
                                                 justify=LEFT)
        self.lb_descripcion.place(x=27, y=30)
        self.mostrar_precio = instancias.MiLabel(master3, text=str(pais.precio), justify=LEFT, font=('Arial', 13),
                                                 relief=SUNKEN)
        self.mostrar_precio.place(x=27, y=440)

    def mostrar_bogota(self):
        '''Función que crea el lugar de Bogotá Colombia y la cantidad de vuelos disponibles'''
        descripcion = vuelo.Lugar.descripcion_bogota(self)
        master4 = Toplevel()
        self.img = PhotoImage(file='bogota.gif')
        self.lb_imagen = instancias.MiLabel(master4, image=self.img)
        self.lb_imagen.place(x=-1, y=-1)
        text1 = 'Bienvenido a Bogotá - Colombia'
        self.crear_interfaz(master4, text1)
        pais = self.lugar.instanciar_bogota()
        self.lb_descripcion = instancias.MiLabel(master4, text=descripcion, font=('Arial', 13, 'italic'),
                                                 justify=LEFT)
        self.lb_descripcion.place(x=27, y=30)
        self.mostrar_precio = instancias.MiLabel(master4, text=str(pais.precio), justify=LEFT, font=('Arial', 13),
                                                 relief=SUNKEN)
        self.mostrar_precio.place(x=27, y=440)

    def mostrar_lima(self):
        '''Función que crea el lugar de Lima Perú'''
        descripcion = vuelo.Lugar.descripcion_lima(self)
        master5 = Toplevel()
        self.img = PhotoImage(file='lima.gif')
        self.lb_imagen = instancias.MiLabel(master5, image=self.img)
        self.lb_imagen.place(x=-200, y=-50)
        text1 = 'Bienvenido a Lima - Perú'
        self.crear_interfaz(master5, text1)
        pais = self.lugar.instanciar_lima()
        self.lb_descripcion = instancias.MiLabel(master5, text=descripcion, font=('Arial', 13),
                                                 justify=LEFT)
        self.lb_descripcion.place(x=40, y=30)
        self.mostrar_precio = instancias.MiLabel(master5, text=str(pais.precio), justify=LEFT, font=('Arial', 13),
                                                 relief=SUNKEN)
        self.mostrar_precio.place(x=27, y=440)

    def mostrar_punta(self):
        '''Función que crea el lugar de Punta Cana República Dominicana'''
        descripcion = vuelo.Lugar.descripcion_puntacana(self)
        master8 = Toplevel()
        self.img = PhotoImage(file='punta.gif')
        self.lb_imagen = instancias.MiLabel(master8, image=self.img)
        self.lb_imagen.place(x=-900, y=-1000)
        text1 = 'Bienvenido a Punta Cana - República Dominicana'
        pais = self.lugar.instanciar_punta()
        self.crear_interfaz(master8, text1)
        self.lb_descripcion = instancias.MiLabel(master8, text=descripcion, font=('Arial', 13,'italic'),
                                                 justify=LEFT)
        self.lb_descripcion.place(x=10, y=30)
        self.mostrar_precio = instancias.MiLabel(master8, text=str(pais.precio), justify=LEFT, font=('Arial', 13),
                                                 relief=SUNKEN)
        self.mostrar_precio.place(x=27, y=440)

    def mostrar_madrid(self):
        '''Función que crea el lugar de Madrid España'''
        descripcion = vuelo.Lugar.descripcion_madrid(self)
        master12 = Toplevel()
        self.img = PhotoImage(file='madrid.gif')
        self.lb_imagen = instancias.MiLabel(master12, image=self.img)
        self.lb_imagen.place(x=-1, y=-1)
        text1 = 'Bienvenido a Madrid - España'
        pais = self.lugar.instanciar_madrid()
        self.crear_interfaz(master12, text1)
        self.lb_descripcion = instancias.MiLabel(master12, text=descripcion, font=('Arial', 13, 'italic'),
                                                 justify=LEFT)
        self.lb_descripcion.place(x=25, y=30)
        self.mostrar_precio = instancias.MiLabel(master12, text=str(pais.precio), justify=LEFT, font=('Arial', 13),
                                                 relief=SUNKEN)
        self.mostrar_precio.place(x=27, y=440)

    def mostrar_paris(self):
        '''Función que crea el lugar de París Francia'''
        descripcion = vuelo.Lugar.descripcion_paris(self)
        master9 = Toplevel()
        self.img = PhotoImage(file='paris.gif')
        self.lb_imagen = instancias.MiLabel(master9, image=self.img)
        self.lb_imagen.place(x=-50, y=-1)
        text1 = 'Bienvenido a París - Francia'
        self.crear_interfaz(master9, text1)
        pais = self.lugar.instanciar_paris()
        self.lb_descripcion = instancias.MiLabel(master9, text=descripcion, font=('Arial', 13, 'italic'),
                                                 justify=LEFT)
        self.lb_descripcion.place(x=30, y=30)
        self.mostrar_precio = instancias.MiLabel(master9, text=str(pais.precio), justify=LEFT, font=('Arial', 13),
                                                 relief=SUNKEN)
        self.mostrar_precio.place(x=27, y=440)

    def mostrar_montevideo(self):
        '''Función que crea el lugar de Montevideo Uruguay'''
        descripcion = vuelo.Lugar.descripcion_montevideo(self)
        master6 = Toplevel()
        self.img = PhotoImage(file='monte.gif')
        self.lb_imagen = instancias.MiLabel(master6, image=self.img)
        self.lb_imagen.place(x=-100, y=0)
        text1 = 'Bienvenido a Montevideo - Uruguay'
        self.crear_interfaz(master6, text1)
        pais = self.lugar.instanciar_montevideo()
        self.lb_descripcion = instancias.MiLabel(master6, text=descripcion, font=('Arial', 13,'italic'),
                                                 justify=LEFT)
        self.lb_descripcion.place(x=25, y=30)
        self.mostrar_precio = instancias.MiLabel(master6, text=str(pais.precio), justify=LEFT, font=('Arial', 13),
                                                 relief=SUNKEN)
        self.mostrar_precio.place(x=27, y=440)

    def mostrar_guayaquil(self):
        '''Función que crea el lugar de Guayaquil Ecuador'''
        descripcion = vuelo.Lugar.descripcion_guayaquil(self)
        master10 = Toplevel()
        self.img = PhotoImage(file='guaya.gif')
        self.lb_imagen = instancias.MiLabel(master10, image=self.img)
        self.lb_imagen.place(x=-100, y=0)
        text1 = 'Bienvenido a Guayaquil - Ecuador'
        self.crear_interfaz(master10, text1)
        pais = self.lugar.instanciar_guayaquil()
        self.lb_descripcion = instancias.MiLabel(master10, text=descripcion, font=('Arial', 13, 'italic'),
                                                 justify=LEFT)
        self.lb_descripcion.place(x=25, y=30)
        self.mostrar_precio = instancias.MiLabel(master10, text=str(pais.precio), justify=LEFT, font=('Arial', 13),
                                                 relief=SUNKEN)
        self.mostrar_precio.place(x=27, y=440)

    def mostrar_lapaz(self):
        '''Función que crea el lugar de La Paz Bolivia'''
        descripcion = vuelo.Lugar.descripcion_lapaz(self)
        master7= Toplevel()
        self.img = PhotoImage(file='paz.gif')
        self.lb_imagen = instancias.MiLabel(master7, image=self.img)
        self.lb_imagen.place(x=-100, y=0)
        text1 = 'Bienvenido a La Paz - Bolivia'
        self.crear_interfaz(master7, text1)
        pais = self.lugar.instanciar_lapaz()
        self.lb_descripcion = instancias.MiLabel(master7, text=descripcion, font=('Arial', 13, 'italic'),
                                                 justify=LEFT)
        self.lb_descripcion.place(x=35, y=30)
        self.mostrar_precio = instancias.MiLabel(master7, text=str(pais.precio), justify=LEFT, font=('Arial', 13),
                                                 relief=SUNKEN)
        self.mostrar_precio.place(x=27, y=440)

    def mostrar_miami(self):
        '''Función que crea el lugar de Miami Estados Unidos'''
        descripcion = vuelo.Lugar.descripcion_miami(self)
        master11 = Toplevel()
        self.img = PhotoImage(file='miami.gif')
        self.lb_imagen = instancias.MiLabel(master11, image=self.img)
        self.lb_imagen.place(x=-1, y=-1)
        text1 = 'Bienvenido a Miami - EE.UU'
        self.crear_interfaz(master11, text1)
        pais = self.lugar.instanciar_miami()
        self.lb_descripcion = instancias.MiLabel(master11, text=descripcion, font=('Arial', 13, 'italic'),
                                                 justify=LEFT)
        self.lb_descripcion.place(x=10, y=30)
        self.mostrar_precio = instancias.MiLabel(master11, text=str(pais.precio), justify=LEFT, font=('Arial', 13),
                                                 relief=SUNKEN)
        self.mostrar_precio.place(x=27, y=440)

    @classmethod
    def mostrar_cabina_especial(cls):
        cabina.CabinaEspecial.descripcion_cabina()
        ventana_especial = instancias.MiToplevel()
        cls.img_especial = PhotoImage(file='especial.gif')
        cls.lb_imagen_especial = instancias.MiLabel(ventana_especial, image=cls.img_especial)
        cls.lb_imagen_especial.place(x=-1, y=-1)

        ventana_especial.geometry('1000x600+200+80')
        ventana_especial.configure(background='white')

        lb_titulo = instancias.MiLabel(ventana_especial, text='BIENVENIDO A LA EXPERIENCIA PREMIUM BUSINESS',
                                       font=('Arial', 14, 'bold'), fg='blue').pack()
        lb_bienvenida = instancias.MiLabel(ventana_especial, text=cabina.CabinaEspecial.bienvenida, justify=LEFT,)
        lb_bienvenida.place(x=20, y=30)

        lb_tit_desc1 = instancias.MiLabel(ventana_especial, text='MÁS QUE DORMIR, ES DESCANSAR', font=('Arial',13),
                                          fg='blue')
        lb_tit_desc1.place(x=20, y=80)

        lb_desc_1 = instancias.MiLabel(ventana_especial, text=cabina.CabinaEspecial.desc_1, justify=LEFT,)
        lb_desc_1.place(x=20, y=100)

        lb_tit_ficha = instancias.MiLabel(ventana_especial, text='-FICHA TÉCNICA', font=('Arial',13),
                                            fg='blue')
        lb_tit_ficha.place(x=20, y=130)

        lb_ficha1 = instancias.MiLabel(ventana_especial, text=cabina.CabinaEspecial.ficha_tecnica1, justify=LEFT)
        lb_ficha1.place(x=20, y=150)

        lb_tit_desc2 = instancias.MiLabel(ventana_especial, text='MÁS QUE PASATIEMPOS, ES ENTRETENCIÓN EXCLUSIVA',
                                          font=('Arial',13), fg='blue')
        lb_tit_desc2.place(x=20, y=180)
        lb_desc_2 = instancias.MiLabel(ventana_especial, text=cabina.CabinaEspecial.desc_2, justify=LEFT)
        lb_desc_2.place(x=20,y=200)
        lb_tit_ficha = instancias.MiLabel(ventana_especial, text='-FICHA TÉCNICA', font=('Arial', 13),
                                           fg='blue')
        lb_tit_ficha.place(x=20, y=260)

        lb_ficha2 = instancias.MiLabel(ventana_especial, text=cabina.CabinaEspecial.ficha_tecnica2,justify=LEFT)
        lb_ficha2.place(x=20, y=280)

        lb_tit_desc3 = instancias.MiLabel(ventana_especial, text='MÁS QUE DETALLES, ES CALIDAD', font=('Arial',13),
                                          fg='blue')
        lb_tit_desc3.place(x=20, y=368)
        lb_desc_2 = instancias.MiLabel(ventana_especial, text=cabina.CabinaEspecial.desc_3, justify=LEFT)
        lb_desc_2.place(x=20, y=390)

        lb_tit_ficha = instancias.MiLabel(ventana_especial, text='-FICHA TÉCNICA', font=('Arial', 13),
                                          fg='blue')
        lb_tit_ficha.place(x=20, y=463)
        lb_ficha3 = instancias.MiLabel(ventana_especial, text=cabina.CabinaEspecial.ficha_tecnica3, justify=LEFT)
        lb_ficha3.place(x=20, y=485)
        ventana_especial.mainloop()

    @classmethod
    def mostrar_cabina_intermedia(cls):
        cabina.CabinaIntermedia.descripcion_cabina()
        ventana_intermedia = instancias.MiToplevel()
        cls.img_especial = PhotoImage(file='intermedia.gif')
        cls.lb_imagen_especial = instancias.MiLabel(ventana_intermedia, image=cls.img_especial)
        cls.lb_imagen_especial.place(x=-1, y=-1)

        ventana_intermedia.geometry('1000x600+200+80')
        ventana_intermedia.configure(background='white')

        lb_titulo = instancias.MiLabel(ventana_intermedia, text='BIENVENIDO A LA EXPERIENCIA PREMIUM ECONOMY',
                                       font=('Arial', 14, 'bold'), fg='blue').pack()

        lb_tit_desc1 = instancias.MiLabel(ventana_intermedia, text='MAYOR ESPACIO PARA TU COMODIDAD', font=('Arial', 13),
                                          fg='blue')
        lb_tit_desc1.place(x=20, y=30)

        lb_desc_1 = instancias.MiLabel(ventana_intermedia, text=cabina.CabinaIntermedia.desc_1, justify=LEFT, )
        lb_desc_1.place(x=20, y=50)

        lb_tit_ficha = instancias.MiLabel(ventana_intermedia, text='-FICHA TÉCNICA', font=('Arial', 13),
                                          fg='blue')
        lb_tit_ficha.place(x=20, y=80)

        lb_ficha1 = instancias.MiLabel(ventana_intermedia, text=cabina.CabinaIntermedia.ficha_tecnica, justify=LEFT)
        lb_ficha1.place(x=20, y=100)

        lb_tit_desc2 = instancias.MiLabel(ventana_intermedia, text='ENTRETENCIÓN EXCLUSIVA',
                                          font=('Arial', 13), fg='blue')
        lb_tit_desc2.place(x=20, y=160)
        lb_desc_2 = instancias.MiLabel(ventana_intermedia, text=cabina.CabinaIntermedia.desc_2, justify=LEFT)
        lb_desc_2.place(x=20, y=182)

        lb_tit_desc3 = instancias.MiLabel(ventana_intermedia, text='CUIDAMOS TU TIEMPO', font=('Arial', 13),
                                          fg='blue')
        lb_tit_desc3.place(x=20, y=255)
        lb_desc_2 = instancias.MiLabel(ventana_intermedia, text=cabina.CabinaIntermedia.desc_3, justify=LEFT)
        lb_desc_2.place(x=20, y=275)

        ventana_intermedia.mainloop()

    @classmethod
    def mostrar_cabina_economica(cls):
        cabina.CabinaEconomica.descripcion_cabina()
        ventana_economica = instancias.MiToplevel()
        cls.img_especial = PhotoImage(file='economica.gif')
        cls.lb_imagen_especial = instancias.MiLabel(ventana_economica, image=cls.img_especial)
        cls.lb_imagen_especial.place(x=-1, y=-1)

        ventana_economica.geometry('1000x600+200+80')
        ventana_economica.configure(background='white')

        lb_titulo = instancias.MiLabel(ventana_economica, text='BIENVENIDO A LA EXPERIENCIA ECONOMY',
                                       font=('Arial', 14, 'bold'), fg='blue').pack()

        lb_tit_desc1 = instancias.MiLabel(ventana_economica, text='AMBIENTE Y COMODIDAD',
                                          font=('Arial', 13),
                                          fg='blue')
        lb_tit_desc1.place(x=20, y=30)

        lb_desc_1 = instancias.MiLabel(ventana_economica, text=cabina.CabinaEconomica.desc_1, justify=LEFT, )
        lb_desc_1.place(x=20, y=50)

        lb_tit_desc2 = instancias.MiLabel(ventana_economica,
                                          text='VUELOS MÁS CORTOS GRACIAS A NUESTRO ENTRETENIMIENTO A BORDO',
                                          font=('Arial', 13), fg='blue')
        lb_tit_desc2.place(x=20, y=95)
        lb_desc_2 = instancias.MiLabel(ventana_economica, text=cabina.CabinaEconomica.desc_2, justify=LEFT)
        lb_desc_2.place(x=20, y=115)

        lb_tit_desc3 = instancias.MiLabel(ventana_economica, text='CALIDAD EN SERVICIO', font=('Arial', 13),
                                          fg='blue')
        lb_tit_desc3.place(x=20, y=145)
        lb_desc_2 = instancias.MiLabel(ventana_economica, text=cabina.CabinaEconomica.desc_3, justify=LEFT)
        lb_desc_2.place(x=20, y=165)

        lb_tit_ficha = instancias.MiLabel(ventana_economica, text='-FICHA TÉCNICA', font=('Arial', 13),
                                          fg='blue')
        lb_tit_ficha.place(x=20, y=195)

        lb_ficha1 = instancias.MiLabel(ventana_economica, text=cabina.CabinaEconomica.ficha_tecnica, justify=LEFT)
        lb_ficha1.place(x=20, y=215)

        ventana_economica.mainloop()