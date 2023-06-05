import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QApplication, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout

from cliente import Cliente


class Ventana4(QMainWindow):

    # Hacer el metodo de construccion de la ventana
    def __init__(self, anterior, cedula):
        super(Ventana4,self).__init__(None)

        self.ventanaAnterior = anterior
        self.cedulaUsuario = cedula

        self.setWindowTitle("Editar Usuario")

        #poner el icono
        self.setWindowIcon(QtGui.QIcon("imagenes/Bolsito.png"))

        #Estabelcemos las propiedaesd de ancho y alto
        self.ancho = 900
        self.alto = 600

        #Establecer el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        #Hacer que la ventana se vea en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        #Fijar el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        #Establecemos el fondo principal
        self.fondo = QLabel(self)

        self.fondo.setStyleSheet("background-color: #FFFFF0")

        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()

        #Le ponemos las margenes
        self.horizontal.setContentsMargins(30,30,30,30)

        #------------------ LAYOUT IZQUIERDO -----------------

        #Creamos el layout del lado izquierdo
        self.ladoIzquierdo = QFormLayout()

        #Hacemos el letrero
        self.letrero1 = QLabel()

        self.letrero1.setText("Editar Cliente")

        self.letrero1.setFont(QFont("Andale Mono", 20))

        self.letrero1.setStyleSheet("color: #FFFFFF;"
                                    "background-color: #FF8C00")

        #Le agregamos el letrero en la primera fila
        self.ladoIzquierdo.addRow(self.letrero1)

        #Hacemos el letrero 2
        self.letrero2 = QLabel()

        #Establecemos el ancho del label
        self.letrero2.setFixedWidth(340)

        #Le escribimos el texto
        self.letrero2.setText("Por favor ingrese la informacion del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asteriscoson obligatorios.")

        #Le asignamos el tipo de letras
        self.setFont(QFont("Andale Mono", 10))

        #Le ponemos el color alas margenes
        self.letrero2.setStyleSheet("color: #FFFFFF; background-color: #FF8C00; margin-bottom: 40px;"
                                    "margin-top: 20pc;"
                                    "padding-bottom: 10px;"
                                    "border: 2px; solid #FFFFFF;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.ladoIzquierdo.addRow(self.letrero2)

        #Hacemos el campo para ingeresar el nombre
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        #Agregamos estos al formualrio
        self.ladoIzquierdo.addRow("Nombre Completo*",self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Password*", self.password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Password*", self.password2)

        #Hacemos el campo para el documento
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        #Lo agregamos al formulario
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Correo*", self.correo)

        #--------------BOTON EDITAR--------------------

        #Hacemos el boton para registrar los datos
        self.botonEditar = QPushButton("Editar")

        self.botonEditar.setFixedWidth(90)

        #Le  ponemos estilos
        self.botonEditar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;")

        self.botonEditar.clicked.connect(self.accion_botonEditar)

        #-------------BOTON LIMPIAR-------------------

        #Hacemos el boton para limpiar los datos
        self.botonLimpiar = QPushButton("Limpiar")

        self.botonLimpiar.setFixedWidth(90)

        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoIzquierdo.addRow(self.botonEditar, self.botonLimpiar)

        #----------------BOTON ELIMINAR-----------------

        self.botonEliminar = QPushButton("Eliminar")

        self.botonEliminar.setFixedWidth(90)

        self.botonEliminar.setStyleSheet("background-color: #008B45;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 10px;")

        self.botonEliminar.clicked.connect(self.accion_botonEliminar)

        self.ladoIzquierdo.addRow(self.botonEliminar)

        #----------------BOTON VOLVER-----------------

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(90)

        self.botonVolver.setStyleSheet("background-color: #008B45;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 10px;")
        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        self.ladoIzquierdo.addRow(self.botonVolver)


        #Agergamos el layout izquierdo al layout horizontal
        self.horizontal.addLayout(self.ladoIzquierdo)

        #--------------- LAYOUT DERECHO -------------------

        #Cremaos el layout lado derecho
        self.ladoDerecho = QFormLayout()

        self.ladoDerecho.setContentsMargins(100,0,0,0)

        #Hacemos el letrero
        self.letrero3 = QLabel()

        self.letrero3.setText("Editar recuperar contraseña")

        self.letrero3.setFont(QFont("Andale Mono", 20))

        self.letrero3.setStyleSheet("color: #FFFFFF;"
                                    "background-color: #FF8C00;")

        self.ladoDerecho.addRow(self.letrero3)

        #HACEMOS EL LETRERO 4

        self.letrero4 = QLabel()

        self.letrero4.setFixedWidth(400)
        self.letrero4.setText("Por favor ingrese la informacion para recuperar"
                             "\nla contraseña. Los campos marcados"
                             "\ncon asterisco son obligatorios.")

        self.letrero4.setFont(QFont("Andale Mono", 10))

        self.letrero4.setStyleSheet("color: #FFFFFF; background-color: #FF8C00; margin-bottom: 40px;"
                                    "margin-top: 20pc;"
                                    "padding-bottom: 10px;"
                                    "border: 2px; solid #FFFFFF;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.ladoDerecho.addRow(self.letrero4)

        #-----1
        self.labelPregunta1 = QLabel("Pregunta de verificacion 1*")

        self.ladoDerecho.addRow(self.labelPregunta1)

        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta1)

        self.labelPregunta1 = QLabel("Respuesta de verificacion 1*")

        self.ladoDerecho.addRow(self.labelPregunta1)

        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta1)

        #----2
        self.labelPregunta2 = QLabel("Pregunta de verificacion 2*")

        self.ladoDerecho.addRow(self.labelPregunta2)

        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta2)

        self.labelPregunta2 = QLabel("Respuesta de verificacion 2*")

        self.ladoDerecho.addRow(self.labelPregunta2)

        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta2)

        #--------3
        self.labelPregunta3 = QLabel("Pregunta de verificacion 3*")

        self.ladoDerecho.addRow(self.labelPregunta3)

        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta3)

        self.labelPregunta3 = QLabel("Respuesta de verificacion 3*")

        self.ladoDerecho.addRow(self.labelPregunta3)

        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta3)


        self.horizontal.addLayout(self.ladoDerecho)



        #------------------- OJO IMPORTANTE PONER AL FINAL ----------------------------

        #Indicamos que el layout principal del fondo es el horizontal
        self.fondo.setLayout(self.horizontal)

        #----------------CREAMOS LA VENTANA DIALOGO------------------
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        self.ventanaDialogo.resize(300, 150)

        #Creamos el boton para aceptar

        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")

        self.mensaje.setStyleSheet("bacground-color: #008b45; color: #FFFFFF; padding: 10px;")

        self.vertical.addWidget(self.mensaje)

        self.vertical.addWidget(self.opciones)

        self.ventanaDialogo.setLayout(self.vertical)

        #Llamamos el metodo para que se carguen los datos en el formulario
        self.cargar_datos()


    def accion_botonEditar(self):

        #Variable para controlar que se han ingresado los datos correctos:
        self.datosCorrectos = True

        #Establecemos el titulo de la ventana
        self.ventanaDialogo.setWindowTitle("Formulario de Edicion")

        #Validamos que los passwords sean iguales
        if (
                self.password.text() != self.password2.text()

        ):
            self.datosCorrectos = False

            #Escribimos el texto explicativo
            self.mensaje.setText("Los passwords no son iguales")

            #Hacemos que la ventana dialogo se vea
            self.ventanaDialogo.exec_()

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            #Escribimos el texto explicativo
            self.mensaje.setText("Debe seleccionar un usuario con documento valido")
            self.mensaje.setStyleSheet("color: #000000;")

            self.ventanaDialogo.exec_()

            self.metodo_botonVolver()

        #Si los datos estan correctos
        if self.datosCorrectos:

            #Abrimos el archivo en modo lectura
            self.file = open('datos/clientes.txt', 'rb')

            #Lista vacia para guardar los usuarios
            usuarios = []

            #Iteramos sobre el archivo linea por linea
            while self.file:
                linea = self.file.readline().decode('UTF-8')

                lista = linea.split(";")

                if linea == '':
                    break

                u = Cliente(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10],
                )

                usuarios.append(u)

            self.file.close()

            existeDocumento = False


            for u in usuarios:
                if int(u.documento) == self.cedulaUsuario:

                    u.usuario = self.usuario.text()
                    u.password = self.password.text()
                    u.correo = self.correo.text()
                    u.pregunta1 = self.pregunta1.text()
                    u.respuesta1 = self.respuesta1.text()
                    u.pregunta2 = self.pregunta2.text()
                    u.respuesta2 = self.respuesta2.text()
                    u.pregunta3 = self.pregunta3.text()
                    u.respuesta3 = self.respuesta3.text()
                    existeDocumento = True
                    break

            if(
                    not existeDocumento
            ):
                self.mensaje.setText("No existe un usuario con ese documento:\n"
                                    + str(self.cedulaUsuario))

                #Hacemos que la ventana de dialgo se vea
                self.ventanaDialogo.exec_()


            self.file = open('datos/clientes.txt', 'wb')

            #Recorremos las lista de ususarios
            #Para guardar usuarios por usuario en el archivo
            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.password + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))

            self.file.close()

            #Si existe un suuario con este documento
            # Y si se edito correctamente
            if (
                    existeDocumento
            ):

                self.mensaje.setText("Usuario actualizado correctamente!")
                self.mensaje.setStyleSheet("color: #000000;")

                #HAcemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()

                self.accion_botonLimpiar()
                self.metodo_botonVolver()

            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

    def accion_botonLimpiar(self):

        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    def accion_botonEliminar(self):

        self.datosCorrectos = True

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''

        ):
            self.datosCorrectos = False

            #Escribimos el texto exolicativo
            self.mensaje.setText("Debe seleccionar un usuario con documento valido!")
            self.mensaje.setStyleSheet("color: #000000;")

            self.ventanaDialogo.exec_()
            self.metodo_botonVolver()

        if self.datosCorrectos:

            #controlamos si vamos a eliminar
            self.eliminar = False

            self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

            self.ventanaDialogoEliminar.resize(300, 150)

            self.ventanaDialogoEliminar.setWindowModality(Qt.ApplicationModal)

            #Creamos un layout vertical
            self.verticalEliminar = QVBoxLayout()

            self.mensajeEliminar = QLabel("¿Estas seguro que desea eliminar este registro de usuario?")

            self.mensajeEliminar.setStyleSheet("background-color: #008B45; color: # FFFFFF; padding: 10px;")

            self.verticalEliminar.addWidget(self.mensajeEliminar)

            #Agregamoos las opcion es de aceptar y cancelar de la ventana
            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)

            #Agregamos las opciones de los botones
            self.verticalEliminar.addWidget(self.opcionesBox)

            self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)

            #Hacemos que la ventana de dialogo se vea
            self.ventanaDialogoEliminar.exec_()

        if self.eliminar:
            #Abrimos el archivo de modo lectura
            self.file = open('datos/clientes.txt', 'rb')

            #Lsita vacia para guardar usuarios
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                #Obtenemos del string una lista con 11 datos separados por ;
                lista = linea.split(";")

                if linea == '':
                    break

                u = Cliente(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10],
                )

                usuarios.append(u)

            self.file.close()

            existeDocumento = False

            for u in usuarios:
                if int(u.documento) == self.cedulaUsuario:
                    #Eliminamos los usuarios de la lista de usuarios
                    usuarios.remove(u)
                    existeDocumento = True
                    #Paramos el for
                    break


            self.file = open('datos/clientes.txt', 'wb')

            #Recorremos la lsita de usuarios
            # Para guardar los usuarios restantes del archivo
            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.password + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))

            self.file.close()

            if (
                existeDocumento
            ):
                #Escribimos el texto explicativo
                self.mensaje.setText("Usuario eliminado exitosamente!")
                self.mensaje.setStyleSheet("color: #000000;")

                #Hacemos que la ventana dialogo se vea
                self.ventanaDialogo.exec_()

                self.accion_botonLimpiar()

                self.metodo_botonVolver()

    def ok_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogoEliminar.close()

    def metodo_botonVolver(self):

        self.hide()
        self.ventanaAnterior.show()

    def cargar_datos(self):

        #Abrimos el archivo en modo lectura
        self.file = open('datos/clientes.txt', 'rb')

        #Lista vacia para guardar los usuarios
        usuarios = []


        #Iteramos sobre el archvio linea por linea
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            #Obtenemos del string una lista con 11 datos sepparados por ;
            lista = linea.split(";")

            if linea == '':
                break
            #Creamos un objeto tipo cliente llamado u
            #y le pasamos los elemnetos de la lista
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
            )
            #Metemos el obejto en la lista de usuarios
            usuarios.append(u)

        self.file.close()

        #En este punto tenemos la lista de usuarios con todos los usuarios

        existeDocumento = False

        #Buscamos en la lista de usuarios por usuarios si existe la cedula
        #Es la cedula seleccionada de la ventana anterior
        for u in usuarios:
            #Comparamos el documento ingresado
            #Si corresponde con el documento, es el usuario correcto
            if int(u.documento) == self.cedulaUsuario:
                #Mostramos los datos en le formulario
                self.nombreCompleto.setText(u.nombreCompleto)
                #Hacemos que el nombre no se peuda editar
                self.nombreCompleto.setReadOnly(True)
                self.usuario.setText(u.usuario)
                self.password.setText(u.password)
                self.password2.setText(u.password)
                self.documento.setText(u.documento)
                #Hacemos que el documento no se pueda editar
                self.documento.setReadOnly(True)
                self.correo.setText(u.correo)
                self.pregunta1.setText(u.pregunta1)
                self.respuesta1.setText(u.respuesta1)
                self.pregunta2.setText(u.pregunta2)
                self.respuesta2.setText(u.respuesta2)
                self.pregunta3.setText(u.pregunta3)
                self.respuesta3.setText(u.respuesta3)
                #Indicamos que encontramos el documento
                existeDocumento = True
                #paramos el for
                break

        if (
                not existeDocumento
        ):
            #Escribmios el texto explicativo
            self.mensaje.setText("No existe un usuario con ese documento:\n"
                                 + str(self.cedulaUsuario))

            #Hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

            self.metodo_botonVolver()




if __name__== '__main__':

    app = QApplication(sys.argv)

    ventana4 = Ventana4()

    ventana4.show()

    sys.exit(app.exec_())
































