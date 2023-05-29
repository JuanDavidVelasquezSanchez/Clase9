import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication
from PyQt5 import QtGui

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

        




        #-------- OJO IMPORTANTE PONER AL FINAL -------
        
        # Indicamos que el layout principal del fondo es horizontal:
        self.fondo.setLayout(self.vertical)


if __name__== '__main__':

    app = QApplication(sys.argv)

    ventana2 = Ventana2

    ventana2.show()

    sys.exit(app.exec_())

