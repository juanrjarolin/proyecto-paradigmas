import os
from datetime import datetime, time
os.chdir(os.getcwd() + '/Datos/Archivos') #se define el lugar de trabajo
import ClasesDominios.Vuelo as reserva
import ClasesDominios.Persona as per
from ClaseImplementacion import FuncionesPrincipales as funcion
from ClaseImplementacion import Instanciador_lugares as lugares
from ClaseImplementacion import Instanciador_cabinas as cabinas
from ClasesControladores import Controlardor_vuelo as controlar_vuelo
from ClasesControladores import Controlador_pasajero as controlador_pasajero
from ClaseImplementacion import Instanciador_vuelos as crear
from Datos import Persistencia as persistencia
import ClaseImplementacion.Pantalla as pantalla
import GUI.Instancias as instancias
import GUI.Funciones as func
from tkinter import *
from tkinter.messagebox import askyesno, showinfo, showerror
from GUI import Mostradores as most
maximo_pasajeros = 9
'''@author: Juan Roberto Jarolin Morán'''

class Application:
    '''Abstracción que representa a un aplicación'''
    def __init__(self, master):
        self.master = master
        self.master.title('LTAM Airlines v1.0')
        self.master.geometry("600x500+400+125")
        self.master.resizable(width=False, height=False)
        self.menu_principal = instancias.MiMenu(master)
        #self.entrada = None
        self.crear_interface()

    def crear_interface(self):
        '''Interfaz principal'''
        lb_bienv = instancias.MiLabel(self.master, text='BIENVENIDO AL SISTEMA', font=('sawasdee', 14, 'bold'),
                                       bg='white', fg='blue')
        lb_bienv.pack()

        lb_text = instancias.MiLabel(self.master, text='¡Viajá por el mundo con nuestras mejores ofertas!',
                                     font=('sawasdee', 13), bg='white')
        lb_text.pack()

        text2 = 'Hola, ¿cómo estás?\nEn el menú -Viajes- podrás ver los países disponibles\ncon sus diferentes precios' \
                ' de acuerdo a la\ndisponibilidad de los asientos o cabinas.\nEn el menú -Cabinas-' \
                ' puede ir visualizando los diferentes'
        lb_text2 = instancias.MiLabel(self.master, text=text2, justify=LEFT, bg='white', font=('sawasdee',11,'italic'))
        lb_text2.place(x=165, y=80)

        text3 = '-tipos y servicios que ofrecemos con todas ' \
                'las comodidades. El Premium Business\n(especial), Premium Economy (Intermedia) y Economy (Económica).' \
                'Finalmente,en el\nmenú -Reservas- podrá realizar su reserva de acuerdo' \
                ' a las especificaciones y\nrequerimientos del mismo: ser mayor de 18 años, no exceder la' \
                ' cantidad máxima\nde pasajeros que es 9 (nueve), y elegir el vuelo correspondiente a cada ' \
                'horario.'
        lb_text3 = instancias.MiLabel(self.master, text=text3, justify=LEFT, bg='white',
                                      font=('sawasdee', 11, 'italic'))
        lb_text3.place(x=20, y=195)

        lb_text4 = instancias.MiLabel(self.master, text='Consultas: 021 234 8000', bg='white',
                                      font=('sawasdee',16))
        lb_text4.place(x=63, y=470)

        self.menu_paises()
        self.menu_cabinas()
        self.menu_reservas()

    def menu_paises(self):
        '''Muestra para cada país su descripción'''
        mostrador_p = most.Mostrador() #objeto mostrador de paises
        menu_viajes = instancias.MiMenu(self.menu_principal)
        menu_viajes.add_command(label="Buenos Aires", command=mostrador_p.mostrar_bsas)
        menu_viajes.add_command(label="Rio de Janeiro", command=mostrador_p.mostrar_rio)
        menu_viajes.add_command(label="Montevideo", command=mostrador_p.mostrar_montevideo)
        menu_viajes.add_command(label="La Paz", command=mostrador_p.mostrar_lapaz)
        menu_viajes.add_command(label="Lima", command=mostrador_p.mostrar_lima)
        menu_viajes.add_command(label="Guayaquil", command=mostrador_p.mostrar_guayaquil)
        menu_viajes.add_command(label="Bogotá", command=mostrador_p.mostrar_bogota)
        menu_viajes.add_command(label="Madrid", command=mostrador_p.mostrar_madrid)
        menu_viajes.add_command(label="Miami", command=mostrador_p.mostrar_miami)
        menu_viajes.add_command(label="Punta Cana", command=mostrador_p.mostrar_punta)
        menu_viajes.add_command(label="París", command=mostrador_p.mostrar_paris)
        menu_viajes.add_command(label="Cancún", command=mostrador_p.mostrar_cancun)
        self.menu_principal.add_cascade(label="Viajes", menu=menu_viajes)
        self.master.config(menu=self.menu_principal)

    def menu_cabinas(self):
        '''Muestra cabinas'''
        mostrador_c = most.Mostrador() #objeto mostrador de cabinas
        menu_cabina = instancias.MiMenu(self.menu_principal)
        menu_cabina.add_command(label="Especial", command=mostrador_c.mostrar_cabina_especial)
        menu_cabina.add_command(label="Intermedia", command=mostrador_c.mostrar_cabina_intermedia)
        menu_cabina.add_command(label="Económica", command=mostrador_c.mostrar_cabina_economica)
        self.menu_principal.add_cascade(label="Cabinas", menu=menu_cabina)
        self.master.config(menu=self.menu_principal)

    def menu_reservas(self):
        menu_reserva = instancias.MiMenu(self.menu_principal)
        menu_reserva.add_command(label="Reservar vuelo", command=self.crear_pasajero)
        menu_reserva.add_command(label="Cancelar vuelo", command=self.vent_cancelar_reserva)
        menu_reserva.add_separator()
        menu_reserva.add_command(label="Ver reserva", command=self.ver_reserva)
        self.menu_principal.add_cascade(label="Reserva", menu=menu_reserva)
        self.master.config(menu=self.menu_principal)

    #---------------------------------------------------------------------------------------------------------#

    def ver_reserva(self):
        '''Muestra la reserva hecha'''
        self.root5 = instancias.MiToplevel()
        self.root5.geometry("600x360+400+200")
        self.root5.resizable(width=False, height=False)
        self.root5.configure(bg='white')
        img_avion = PhotoImage(file='avion_ver.gif')
        lb_avion = instancias.MiLabel(self.root5, image=img_avion, fg='blue')
        lb_avion.place(x=0, y=50)
        lbl_cedula = instancias.MiLabel(self.root5, text='Cédula', font=('sawasdee', 15, 'bold'), bg='white')
        lbl_cedula.place(x=340, y=100)

        def ver():
            try:
                cedula = int(txt_ced.get())
                if os.path.isfile(str(cedula) + '.data'):  # busca en el directorio Persistencia la reserva hecha
                    showinfo('Reserva', persistencia.PersistenciaP.load(str(cedula)))#muestra en pantalla
                else:
                    showerror('Mensaje', 'No se ha encontrado su reserva')
            except ValueError:
                showerror('Mensaje', 'Valor incorrecto')

        btb_cancelar = instancias.MiBoton(self.root5, text='Ver Reserva', relief='flat', font='sawasdee',
                                          highlightbackground='blue', command=ver, width=15)
        btb_cancelar.place(x=417, y=140)

        txt_ced = instancias.MiStringVar()
        entrada_cedula = instancias.MiEntry(self.root5, textvariable=txt_ced, show='*')
        entrada_cedula.place(x=415, y=109)
        self.root5.transient(root)
        self.root5.mainloop()

    def vent_cancelar_reserva(self):
        '''Función que cancela una reserva'''
        self.root4 = instancias.MiToplevel()
        self.root4.geometry("640x360+400+200")
        self.root4.configure(bg='white')
        self.root4.resizable(width=False, height=False)

        def cancelar():
            try:
                cedula = int(txt_ced.get())
                if os.path.isfile(str(cedula) + '.data'):  # busca en el directorio Persistencia la reserva hecha
                    if askyesno('Confirmación', '¿Está seguro que desea cancelar su reserva?'):
                        os.remove(str(cedula) + '.data')  # eliminar el archivo
                        showinfo('Mensaje', 'Ha eliminado su reserva')
                else:
                    showerror('Mensaje', 'No se ha encontrado su reserva')
            except ValueError:
                showerror('Mensaje', 'Valor incorrecto')

        img_avion = PhotoImage(file='avion_ver.gif')
        lb_avion = instancias.MiLabel(self.root4, image=img_avion, fg='blue')
        lb_avion.place(x=0, y=50)
        lbl_cedula = instancias.MiLabel(self.root4, text='Cédula', font=('sawasdee', 15, 'bold'), bg='white')
        lbl_cedula.place(x=340, y=100)
        txt_ced = instancias.MiStringVar()
        entrada_cedula = instancias.MiEntry(self.root4, textvariable=txt_ced, show='*')
        entrada_cedula.place(x=415, y=109)
        btb_cancelar = instancias.MiBoton(self.root4, text='Cancelar Reserva', relief='flat', font='sawasdee',
                                          highlightbackground='blue', command=cancelar, width=15)
        btb_cancelar.place(x=417, y=140)
        self.root4.transient(root)
        self.root4.mainloop()

    def instanciar_pasajero(self):
        self.estado = "Correcto"
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        cedula = self.cedula.get()
        fecha = self.fecha_nacimiento.get()
        contacto = self.contacto.get()
        correo = self.correo.get()
        direccion = self.direccion.get()
        nacionalidad = self.nacionalidad.get()

        persona = per.Pasajero(nombre, apellido, fecha, cedula, direccion, contacto, correo, nacionalidad)

        #se crea un objeto controlador
        controlador_p = controlador_pasajero.ControladorPasajero()
        #se crea un objecto 'funcion gui'
        funcion_p = func.FuncionesGui()
        # se valida el nombre de la persona
        if controlador_p.validar_nombre(persona):
            self.txtNombre.configure(highlightbackground='green')
        else:
            self.txtNombre.configure(highlightbackground='red')
            self.estado = "Incorrecto"

        # se valida el apellido de la persona
        if controlador_p.validar_apellido(persona):
            self.txtApellido.configure(highlightbackground='green')
        else:
            self.txtApellido.configure(highlightbackground='red')
            self.estado = "Incorrecto"

        # se valida la cédula de la persona
        if controlador_p.validar_cedula(persona):
            self.txtCedula.configure(highlightbackground='green')
        else:
            self.txtCedula.configure(highlightbackground='red')
            self.estado = "Incorrecto"

        # se valida la fecha de nacimiento de la persona
        if controlador_p.validar_fecha_nacimiento(persona):
            self.txtFecha.configure(highlightbackground='green')
        else:
            self.txtFecha.configure(highlightbackground='red')
            self.estado = "Incorrecto"

        # se valida el contacto de la persona
        if controlador_p.validad_contacto(persona):
            self.txtContacto.configure(highlightbackground='green')
        else:
            self.txtContacto.configure(highlightbackground='red')
            self.estado = "Incorrecto"

        # se valida el correo de la persona
        if controlador_p.validar_correo(persona):
            self.txtCorreo.configure(highlightbackground='green')
        else:
            self.txtCorreo.configure(highlightbackground='red')
            self.estado = "Incorrecto"

        #valida la dirección de la persona
        if controlador_p.validar_direccion(persona):
            self.txtDireccion.configure(highlightbackground='green')
        else:
            self.txtDireccion.configure(highlightbackground='red')
            self.estado = "Incorrecto"

        # se valida la nacionalidad de la persona
        if controlador_p.validar_nacionalidad(persona):
            self.txtNacionalidad.configure(highlightbackground='green')
        else:
            self.txtNacionalidad.configure(highlightbackground='red')
            self.estado = "Incorrecto"

        #si el estaoo de los datos es correcto, la persona pasa a ser un pasajero y se habilita el sgt boton
        if self.estado == "Correcto":
            showinfo('Mensaje', 'Datos correctos')
            self.pasajero = persona
            funcion_p.habilitar_boton(self.btn_siguiente1)
        else:
            funcion_p.deshabilitar_boton(self.btn_siguiente1)

    def verificar_cantidad_pasajero(self):
        #se crea un objeto controlador vuelo
        controlador_v = controlar_vuelo.ControlarVuelo()
        #se crea un objeto funcion verificar
        funcion_v = func.FuncionesGui()
        self.estado = "Correcto" #el estado de la validacion se inicializa a correcto
        try:
            self.adultos = int(self.c_adultos.get())
            self.niños = int(self.c_niños.get())
            self.bebes = int(self.c_bebes.get())
            if controlador_v.controlar_cantidad_personas(self.adultos, self.niños, self.bebes):
                showinfo('Mensaje', 'Cantidad correcta')
                self.cantidad_pasajeros = [self.adultos, self.niños, self.bebes]
                funcion_v.habilitar_boton(self.btn_siguiente2)
            else:
                funcion_v.deshabilitar_boton(self.btn_siguiente2)
        except ValueError:
            showerror('Error', 'Error de valor en cantidad pasajeros ')
            self.estado = 'Incorrecto'
            funcion_v.deshabilitar_boton(self.btn_siguiente2)

    def crear_pasajero(self):
        self.root3 = instancias.MiToplevel()#se crea otra ventana para reservas
        self.root3.geometry("600x370+400+200")
        self.root3.configure(bg='white')
        self.img = PhotoImage(file='atencion.gif')
        self.lb_imagen = instancias.MiLabel(self.root3, image=self.img, bg='white')
        self.lb_imagen.place(x=383, y=110)
        self.titulo = instancias.MiLabel(self.root3, text='BIENVENIDO A RESERVAS ONLINE',
                                    font=('sawasdee',14, 'bold'), bg='white', fg='blue')
        self.titulo.pack()

        self.texto = 'Paso 1. Llene los campos con sus datos personales, su fecha nacimiento debe estar en' \
                ' formato\ndd/mm/aaaa. Una vez verificado sus datos, diríjase al paso 2 que le indicará' \
                ' el sistema.'
        self.lb_info = instancias.MiLabel(self.root3, text=self.texto)
        self.lb_info.place(x=12, y=40)

        #se crea un label nombre y un cuadro texto
        self.nombre = instancias.MiStringVar()
        lbl_nombre= instancias.MiLabel(self.root3, text="Nombre:", font=('sawasdee',12,'bold'), bg='white').place(x=15, y=90)
        self.txtNombre = Entry(self.root3, textvariable=self.nombre)
        self.txtNombre.place(x=175, y=96)

        #se crea un label apellido y un cuadro de texto
        self.apellido = instancias.MiStringVar()
        lbl_apellido = instancias.MiLabel(self.root3, text="Apellido:", font=('sawasdee',12,'bold'), bg='white').place(x=15, y=115)
        self.txtApellido = Entry(self.root3, textvariable=self.apellido)
        self.txtApellido.place(x=175, y=121)

        #se crea un label cédula y un cuadro de texto
        self.cedula = instancias.MiStringVar()
        cedula = instancias.MiLabel(self.root3, text="Cédula:", font=('sawasdee',12,'bold'), bg='white').place(x=15, y=140)
        self.txtCedula = Entry(self.root3, textvariable=self.cedula)
        self.txtCedula.place(x=175, y=146)

        #se crea un label fecha de nacimiento y un cuadro de texto
        self.fecha_nacimiento = instancias.MiStringVar()
        fecha_nacimiento = instancias.MiLabel(self.root3, text="Fecha de nacimiento:", font=('sawasdee',12,'bold'), bg='white').place(x=15, y=165)
        self.txtFecha = Entry(self.root3, textvariable=self.fecha_nacimiento)
        self.txtFecha.place(x=175, y=171)

        #se crea un label contacto y un cuadro de texto
        self.contacto = instancias.MiStringVar()
        self.contacto.set('595')
        contacto = instancias.MiLabel(self.root3, text="Contacto:", font=('sawasdee',12,'bold'), bg='white').place(x=15, y=190)
        self.txtContacto = Entry(self.root3, textvariable=self.contacto)
        self.txtContacto.place(x=175, y=196)

        #se crea un label correo y un cuadro de texto
        self.correo = instancias.MiStringVar()
        correo = instancias.MiLabel(self.root3, text="Correo:", font=('sawasdee',12,'bold'), bg='white').place(x=15, y=215)
        self.txtCorreo = Entry(self.root3, textvariable=self.correo)
        self.txtCorreo.place(x=175, y=221)

        #se crea un label dirección y un cuadro de texto
        self.direccion = instancias.MiStringVar()
        direccion = instancias.MiLabel(self.root3, text="Dirección:", font=('sawasdee',12,'bold'), bg='white').place(x=15, y=240)
        self.txtDireccion = Entry(self.root3, textvariable=self.direccion)
        self.txtDireccion.place(x=175, y=246)

        #se crea un label nacionalidad y un cuadro de texto
        self.nacionalidad = instancias.MiStringVar()
        nacionalidad = instancias.MiLabel(self.root3, text="Nacionalidad:", font=('sawasdee',12,'bold'), bg='white').place(x=15, y=265)
        self.txtNacionalidad = Entry(self.root3, textvariable=self.nacionalidad)
        self.txtNacionalidad.place(x=175, y=271)

        #boton que verifica si los datos ingresados son correctos.
        self.btn_verificar = instancias.MiBoton(self.root3, text='Verificar datos', relief=FLAT, font='sawasdee',
                                                highlightbackground='blue', command=self.instanciar_pasajero)
        self.btn_verificar.place(x=193, y=310)

        #boton que se habilita cuando los datos esten correctos y se pasa a la sigte ventana
        self.btn_siguiente1 = instancias.MiBoton(self.root3, text='Siguiente', relief=FLAT, font='sawasdee',
                                                highlightbackground='blue', state='disabled',
                                                command=self.crear_cant_pasajero)
        self.btn_siguiente1.place(x=425, y=310)

        #root3 es una ventana hija de la ventana root
        self.root3.transient(root)
        self.root3.mainloop()

    def crear_cant_pasajero(self):
        '''Funcion que muestra la cantidad de pasajeros a seleccionar'''
        funcion_c = func.FuncionesGui() #se crea un objeto funcion
        funcion_c.deshabilitar_boton(self.btn_siguiente1)
        self.root6 = instancias.MiToplevel()
        self.root6.geometry("600x370+400+200")
        self.root6.configure(bg='white')

        lb_titulo = instancias.MiLabel(self.root6, text='CANTIDAD DE PASAJEROS',
                                       font=('sawasdee', 14, 'bold'), bg='white', fg='blue')
        lb_titulo.pack()

        self.img_cant = PhotoImage(file='pasajero.gif')
        self.lb_imagen_pasajero = instancias.MiLabel(self.root6, image=self.img_cant, bg='white')
        self.lb_imagen_pasajero.place(x=310, y=105)

        texto = 'Paso 2. Seleccione la cantidad de pasajero. La cantidad máxima de boletas que\n' \
                'puede reservar es nueve.'
        lb_info = instancias.MiLabel(self.root6, text=texto)
        lb_info.place(x=53, y=40)

        lb_adultos = instancias.MiLabel(self.root6, text="Adultos", bg='white', font=('sawasdee',14, 'bold'))
        lb_adultos.place(x=150, y=120)
        lb_niños = instancias.MiLabel(self.root6, text="Niños", bg='white', font=('sawasdee',14, 'bold'))
        lb_niños.place(x=150, y=170)
        lb_bebes = instancias.MiLabel(self.root6, text="Bebes", bg='white', font=('sawasdee',14, 'bold'))
        lb_bebes.place(x=150, y=220)

        self.c_adultos = instancias.MiStringVar()
        self.spin_adulto = Spinbox(self.root6, from_=1, to=9, width=2, textvariable=self.c_adultos)
        self.spin_adulto.place(x=250, y=130)

        self.c_niños = instancias.MiStringVar()
        self.spin_niño = Spinbox(self.root6, from_=0, to=9, width=2, textvariable=self.c_niños)
        self.spin_niño.place(x=250, y=180)

        self.c_bebes = instancias.MiStringVar()
        self.spin_bebes = Spinbox(self.root6, from_=0, to=9, width=2, textvariable=self.c_bebes)
        self.spin_bebes.place(x=250, y=230)

        self.btn_verificar = instancias.MiBoton(self.root6, text='Verificar', relief=FLAT, font='sawasdee',
                                                highlightbackground='blue', command=self.verificar_cantidad_pasajero)
        self.btn_verificar.place(x=340, y=295)

        self.btn_siguiente2 = instancias.MiBoton(self.root6, text='Siguiente', relief=FLAT, font='sawasdee',
                                                 highlightbackground='blue', state='disabled',
                                                 command=self.crear_vuelo)
        self.btn_siguiente2.place(x=445, y=295)

        #la ventana root6 es ventana hija de root3
        self.root6.transient(self.root3)
        self.root6.mainloop()

    def crear_vuelo(self):
        '''Funcion que muestra los paises'''
        funcion_vc = func.FuncionesGui()#se crea una funcion
        funcion_vc.deshabilitar_boton(self.btn_siguiente2)
        self.root7 = instancias.MiToplevel()
        self.root7.geometry("600x370+400+200")
        self.root7.configure(bg='white')

        lb_titulo = instancias.MiLabel(self.root7, text='VUELOS Y CABINAS',
                                       font=('sawasdee', 14, 'bold'), bg='white', fg='blue')
        lb_titulo.pack()

        texto = 'Paso 3. Seleccione el lugar en donde quiere viajar. Para cada lugar se ' \
                'mostrarán los diferentes\nprecios que corresponden a cada cabina.'
        lb_info = instancias.MiLabel(self.root7, text=texto, justify=LEFT, bg='white')
        lb_info.place(x=15, y=35)

        self.p = StringVar()
        self.paises = Spinbox(self.root7, values=('Buenos Aires', 'Bogotá', 'Cancún', 'Miami',
                                              'Rio de Janeiro', 'La Paz', 'Guayaquil', 'Madrid',
                                              'Montevideo', 'Punta Cana', 'Paris', 'Lima'),
                         textvariable=self.p, command=self.reservar_lugar, bg='white', fg='blue', font=('sawasdee',13))
        self.paises.place(x=80, y=100)

        self.img_paises = PhotoImage(file='paises.gif')
        self.lb_paises = instancias.MiLabel(self.root7, image=self.img_paises, bg='white')
        self.lb_paises.place(x=305, y=75)

        self.rdb_cabina_especial = instancias.MiRadioButton(self.root7, text="Especial", state='disabled', bg='white',
                                                            highlightbackground='white', font=('sawasdee',14),
                                                            value=1, command=self.instanciar_cabina_especial)
        self.rdb_cabina_especial.place(x=80, y=150)

        self.rdb_cabina_intermedia = instancias.MiRadioButton(self.root7, text="Intermedia", state='disabled',
                                                              bg='white', highlightbackground='white',
                                                              font=('sawasdee',14),value=2,
                                                              command=self.instanciar_cabina_intermedia)
        self.rdb_cabina_intermedia.place(x=80, y=180)

        self.rdb_cabina_economica = instancias.MiRadioButton(self.root7, text="Económica", state='disabled',
                                                             bg='white', highlightbackground='white',
                                                             font=('sawasdee',14), value=3,
                                                             command=self.instanciar_cabina_economica)
        self.rdb_cabina_economica.place(x=80, y=205)

        lbl_precio = instancias.MiLabel(self.root7, text='Precio en US$', bg='white',
                                               font=('sawasdee',14))
        lbl_precio.place(x=77, y=250)

        self.lbl_monto = instancias.MiLabel(self.root7, font=('sawasdee',14), bg='white')
        self.lbl_monto.place(x=210, y=251)

        self.btn_siguiente3 = instancias.MiBoton(self.root7, text='Siguiente', relief=FLAT, fg='blue', state='disabled',
                                           command=self.mostrar_horarios, font=('sawasdee',14))
        self.btn_siguiente3.place(x=250, y=320)

        self.root7.transient(self.root6)
        self.root7.mainloop()

    def reservar_lugar(self):
        '''Funcion que reserva un lugar'''
        nombre_pais = self.p.get()
        funcion_pr = funcion.FuncionesPrincipales() #objeto de tipo funcion principal
        self.lugar = funcion_pr.reservar_vuelo(nombre_pais)

        if self.lugar.precio.precio_especial == 'No disponible':
            self.rdb_cabina_especial.configure(state='disable')
        else:
            self.rdb_cabina_especial.configure(state='normal')

        if self.lugar.precio.precio_intermedio == 'No disponible':
            self.rdb_cabina_intermedia.configure(state='disabled')
        else:
            self.rdb_cabina_intermedia.configure(state='normal')

        if self.lugar.precio.precio_economico == 'No disponible':
            self.rdb_cabina_economica.configure(state='disabled')
        else:
            self.rdb_cabina_economica.configure(state='normal')

    def instanciar_cabina_especial(self):
        '''Funcion que hace instanciar una cabina especial'''
        cab_especial = cabinas.InstanciadorCabina()
        funcion_h = func.FuncionesGui()
        try:
            self.lbl_monto.configure(text=str(self.lugar.precio.precio_especial))
            self.cabina = cab_especial.instanciar_cabina_especial(self.lugar.precio)
            funcion_h.habilitar_boton(self.btn_siguiente3)
        except AttributeError:
            showerror('Error', 'No ha seleccionado un lugar')

    def instanciar_cabina_intermedia(self):
        cab_intermedia = cabinas.InstanciadorCabina()
        funcion_h = func.FuncionesGui()
        try:
            self.lbl_monto.configure(text=str(self.lugar.precio.precio_intermedio))
            self.cabina = cab_intermedia.instanciar_cabina_intermedia(self.lugar.precio)
            funcion_h.habilitar_boton(self.btn_siguiente3)
        except AttributeError:
            showerror('Error', 'No ha seleccionado un lugar')

    def instanciar_cabina_economica(self):
        cab_economica = cabinas.InstanciadorCabina()
        funcion_h = func.FuncionesGui()
        try:
            self.lbl_monto.configure(text=str(self.lugar.precio.precio_economico))
            self.cabina = cab_economica.instanciar_cabina_economica(self.lugar.precio)
            funcion_h.habilitar_boton(self.btn_siguiente3)
        except AttributeError:
            showerror('Error', 'No ha seleccionado un lugar')

    def reservar(self):
        '''Función que realiza la reserva final'''
        persist = persistencia.PersistenciaP()
        funcion_imp = funcion.FuncionesPrincipales()
        funcion_d = func.FuncionesGui()
        if askyesno('Mensaje', '¿Está seguro que quiere hacer la reserva?'):
            self.reserva_pasajero = reserva.Reserva(self.pasajero, self.lugar, self.cabina,
                                                    self.vuelo, self.cantidad_pasajeros)
            persist.save(str(self.pasajero.cedula), self.reserva_pasajero)
            funcion_imp.imprimir_comprobante(self.reserva_pasajero)
            mensaje_reserva = 'Ha hecho su reserva. Por favor, guarde el comprobante' \
                              ' y presente en la agencia de viajes para su posterior' \
                              ' confirmación. ¡Gracias por utilizar nuestro servicio!'
            showinfo('Confirmación', mensaje_reserva)
            funcion_d.deshabilitar_boton(self.btn_reservar)

    def al_presionar_enter(self, event):
        funcion_hd = func.FuncionesGui() #funcion habilitar deshabilitar
        try:
            num_vuelo = int(self.fecha.get())
            self.vuelo = self.lugar.cant_vuelos[num_vuelo - 1]
            if self.vuelo.habilitado:
                showinfo('Mensaje', 'El vuelo está habilitado')
                funcion_hd.habilitar_boton(self.btn_reservar)
            else:
                showinfo('Mensaje', 'El vuelo no está habilitado')
                funcion_hd.deshabilitar_boton(self.btn_reservar)
        except ValueError:
            self.cuadro_selec.configure(highlightbackground='red')
            showinfo('Corrección', 'No se reconoce el valor')
        except IndexError:
            showinfo('Corrección', 'Fuera de rango')

    def mostrar_info(self):
        showinfo('Mensaje', 'Presione -Enter- para seleccionar el num. de vuelo')

    def mostrar_horarios(self):
        funcion_d = func.FuncionesGui() #funcion deshabilitar
        funcion_d.deshabilitar_boton(self.btn_siguiente3)
        self.vuelo = None
        self.root2 = instancias.MiToplevel()
        self.root2.geometry("640x360+400+200")
        img2 = PhotoImage(file="vuelo.gif")
        widget2 = instancias.MiLabel(self.root2, image=img2)
        widget2.place(x=-130, y=-200)

        lbl_titulo = instancias.MiLabel(self.root2, text='HORARIOS', font=('bold', 14))
        lbl_titulo.pack()

        texto = 'Para seleccionar el horario fíjese en el estado del vuelo'
        lbl_sub_titulo = instancias.MiLabel(self.root2, text=texto)
        lbl_sub_titulo.pack()

        lbl_codigo = instancias.MiLabel(self.root2, text='Código', fg='blue',
                                        font=('Arial', 13))
        lbl_codigo.place(x=40, y=54)

        lbl_transporte = instancias.MiLabel(self.root2, text='Transporte', fg='blue',
                                            font=('Arial', 13))
        lbl_transporte.place(x=165, y=54)

        lbl_horario = instancias.MiLabel(self.root2, text='Horario', fg='blue',
                                         font=('Arial', 13))
        lbl_horario.place(x=295, y=54)

        lbl_fecha = instancias.MiLabel(self.root2, text='Fecha', fg='blue',
                                       font=('Arial', 13))
        lbl_fecha.place(x=425, y=54)

        lbl_estado = instancias.MiLabel(self.root2, text='Estado', fg='blue',
                                        font=('Arial', 13))
        lbl_estado.place(x=550, y=54)

        self.btn_reservar = instancias.MiBoton(self.root2, text='Reservar', cursor='hand2', state='disabled',
                                               command=self.reservar)  # funcion impl
        self.btn_reservar.place(x=280, y=320)

        y_estado = 80  # eje y
        conta = 1  # contador num vuelo
        controlador_v = controlar_vuelo.ControlarVuelo()

        for vuelo in self.lugar.cant_vuelos:
            ahora = datetime.now()
            hora_actual = time(ahora.hour, ahora.minute, ahora.second)
            controlador_v.controlar_partida(hora_actual, vuelo)
            muestra_vuelo = instancias.MiLabel(self.root2, text=str(vuelo))
            muestra_vuelo.place(x=40, y=y_estado)
            muestra_nro_vuelo = instancias.MiLabel(self.root2, text=str(conta), fg='blue')
            muestra_nro_vuelo.place(x=15, y=y_estado)
            y_estado = y_estado + 30
            conta += 1

        lbl_selec = instancias.MiLabel(self.root2, text='Ingrese el número de vuelo (1-7)')
        lbl_selec.place(x=15, y=300)

        btn_ayuda = instancias.MiBoton(self.root2, text='info', bitmap='info', command=self.mostrar_info)
        btn_ayuda.place(x=240, y=296)
        self.fecha = instancias.MiStringVar()
        self.cuadro_selec = Entry(self.root2, textvariable=self.fecha, width=2)
        self.cuadro_selec.place(x=217, y=299)
        self.cuadro_selec.bind('<Return>', self.al_presionar_enter)

        self.root2.transient(self.root7)
        self.root2.mainloop()

root = Tk()
root.configure(bg='white')
img = PhotoImage(file="inicio.gif")
widget = Label(root, image=img, bg='white')
widget.place(x=20, y=65)
img2 = PhotoImage(file='inicio2.gif')
widget2 = instancias.MiLabel(root, image=img2)
widget2.place(x=63, y=300)
app = Application(root)
root.mainloop()
