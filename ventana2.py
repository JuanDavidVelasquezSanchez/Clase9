import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication, QScrollArea, QWidget, \
    QGridLayout, QButtonGroup, QPushButton
from PyQt5 import QtGui

from cliente import Cliente

import math


class Ventana2(QMainWindow):

    #Hacemos el motodo para construir la ventana:
    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)

        #Creamos un atributo que guarde la ventana anterior:
        self.ventanaAnterior  = anterior

        #Ponemos el titulo:
        self.setWindowTitle("Usuarios Registrado")

        #Poner el icono:
        self.setWindowIcon(QtGui.QIcon('imagenes/Bolsito.png'))

        #Establecemos las propiedades de alto y ancho:
        self.ancho = 900
        self.alto = 600

        #Establecer el ancho y alto:
        self.resize(self.ancho, self.alto)

        #Hacer que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        #Fijar el ancho y el alto:
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        #Establecemos el fondo principal:
        self.fondo = QLabel(self)

        #Definimos la imagen de fondo:
        self.imagenFondo = QPixmap('imagenes/Paisaje.png')

        #Definimos la imagen de fondo:
        self.fondo.setPixmap(self.imagenFondo)

        #Establecemos el modo para escalar la imagen:
        self.fondo.setScaledContents(True)

        #Hacemos que se adapte el tamaño de la imagen:
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        #Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        #Establecemos  la distribuccion de los elementos en layout vertical:
        self.vertical = QVBoxLayout()

        #Hacemos el letrero:
        self.letrero1 = QLabel()

        #Le escribimso el texto
        self.letrero1.setText("Usuarios Registrados")

        #Le asignamos el tipo de letra:
        self.letrero1.setFont(QFont("Andale Mono", 20))

        #Le ponemos color de texto y margenes:
        self.letrero1.setStyleSheet("color: white;")

        #Agregamos el letrero a al primera fila:
        self.vertical.addWidget(self.letrero1)

        #Ponemos un espacio despues:
        self.vertical.addStretch()
        
        #Creamos un scroll:
        self.scrollArea = QScrollArea()
        
        #Le ponemos transparente el fondo del scroll:
        self.scrollArea.setStyleSheet("background-color: transparent;")

        #Hacemos que el scroll se adapte a diferentes tamaños:
        self.scrollArea.setWidgetResizable(True)

        #Hacemos una ventana contenedora para cada celda:
        self.contenedora = QWidget()

        #Vamos a crear un layout de grid para poner una cuadricula de elementos:
        self.cuadricula = QGridLayout(self.contenedora)

        #Metemos la ventana contenedora en un scroll:
        self.scrollArea.setWidget(self.contenedora)

        #Metemos el layout vertical en el scroll:
        self.vertical.addWidget(self.scrollArea)

        #Abrimos el archivo en modo lectura:
        self.file = open('datos/clientes.txt', 'rb')

        #Lista vacia para guardar los usuarios:
        self.usuarios = []

        #Recorremos el archivo, linea por linea:
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            #obtenemos del string una lista con 11 datos separados por ;
            lista = linea.split(";")
            #Se para si ya no hay mas registros en el archivo
            if linea == '':
                break
            #Creamos un objeto tipo cliente llamado u
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
            #metemos el objeto en la lista de usuarios:
            self.usuarios.append(u)

        #cerramos el archivo
        self.file.close()

        #En este punto tenemos la lista de usuarios con todos los usuarios:

        #Obtenemos el numero de usuarios registrados:
        #consultamos el tamaño de la lista usuarios:
        self.numeroUsuarios = len(self.usuarios)

        #contador de elementos para controlar a los usuarios en la lista de fila por columna:
        self.contador = 0

        #Definimos la cantidad de elementos a mostrar por columna:
        self.elementosPorColumna = 3

        #Calculamos el numero de filas:
        #Redondeamos al entero superior + 1, dividimos por elementosPorColumnas:
        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        #controlamso todos los botones por una variable:
        self.botones = QButtonGroup()

        #Definimos que el controlador de los botones
        #debe agrupar a todos los controladores internos:
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna+1):

                #Validamos que se estan ingresando la cantidad de usuarios correctos:
                if self.contador < self.numeroUsuarios:

                    #En cada celda de la cadricula va un ventana:
                    self.ventanaAuxiliar = QWidget()

                    #Se determina su alto y su ancho
                    self.ventanaAuxiliar.setFixedWidth(200)
                    self.ventanaAuxiliar.setFixedHeight(100)

                    #Creamos un layout vertical para cada elemento de la cuadricula:
                    self.verticalCuadricula = QVBoxLayout()

                    #Creamos un boton para cada usuario  mostrando su cedula:
                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)

                    #Establecemos el ancho del boton:
                    self.botonAccion.setFixedWidth(150)

                    #Le ponemos los estilos:
                    self.botonAccion.setStyleSheet("background-color: #008B45;"
                                                   "color: #FFFFFF;"
                                                   "padding: 10px;"
                                                   )

                    #Metemos el boton en el layout vertical para que se vea:
                    self.verticalCuadricula.addWidget(self.botonAccion)

                    #Agregamos el boton del grupo, con su cedula como id:
                    self.botones.addButton(self.botonAccion,int(self.usuarios[self.contador].documento))

                    #Agregamos un espacio en blanco:
                    self.verticalCuadricula.addStretch()

                    # A la ventanale asignamos el layout vertical:
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)

                    # A la cuadricula le agregamos la ventana en la fila y columna actual:
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)

                    #Aumentamos el contador:
                    self.contador += 1

        #Establecemos el metodo para que funcione todos los botones:
        self.botones.idClicked.connect(self.metodo_accionBotones)

        #--------- BOTON VOLVER ------
        #Hacemos el boton volver para devolvernos a la ventana anterior:
        self.botonVolver = QPushButton("Volver")

        #Establece el ancho del boton:
        self.botonVolver.setFixedWidth(90)

        #Le ponemos los estilos:
        self.botonVolver.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;"
                                       )

        #Hacemos que el boton botonContinuar tenga su metodo:
        self.botonVolver.clicked.connect(self.metodo_accionVolver)

        #Metemos en el layout vertical el botonVolver:
        self.vertical.addWidget(self.botonVolver)

        #-------- OJO IMPORTANTE PONER AL FINAL -------
        
        # Indicamos que el layout principal del fondo es horizontal:
        self.fondo.setLayout(self.vertical)

    #Metodo para controlar las acciones de los botones:
    def metodo_accionBotones(self, cedulaUsuario):
        print(cedulaUsuario)

    def metodo_accionVolver(self):
        self.hide()
        self.ventanaAnterior.show()


if __name__== '__main__':

    app = QApplication(sys.argv)

    ventana2 = Ventana2

    ventana2.show()

    sys.exit(app.exec_())

