import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication
from PyQt5 import QtGui

class Ventana1(QMainWindow):

    #Hacer el metodo de contruccion de la ventana
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        #Poner el titulo
        self.setWindowTitle("Formulario de Registro")

        #Poner el icono
        self.setWindowIcon(QtGui.QIcon("imagenes/Bolsito.png"))

        #Propiedadesd e acnho y alto
        self.ancho = 900
        self.alto = 600

        #Estabelemos el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        #Hacer que la ventana se vea en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        #Fijar el acnho y alto de la ventana
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        #Estabelcemos el fondo principal
        self.fondo = QLabel(self)

        #Definimos la imgane de fondo
        self.imagenFondo = QPixmap("imagenes/Paisaje.png")

        #Definimso ala imagen de fondo
        self.fondo.setPixmap(self.imagenFondo)

        #Estabelcemos el modo la escalar la imagen
        self.fondo.setScaledContents(True)

        #Hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        #Estabelcemos la ventana de fondo con la ventana central
        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()

        #Le ponemos las margenes
        self.horizontal.setContentsMargins(30,30,30,30)

        #--------------LAYOUT IZQUIERDO-------------------

        #Creamos el layout de lado izquierdo
        #self.ladoIzquierdo = QFormLayout()

        #self.letrero1 = QLabel()

        #self.letrero1.setText("Informacion del Cliente")

        #Le asignamos el tipo de letra
        #self.letrero1.setFont(QFont("Andale Mono", 20))

        #-------------------OJO IMPORTANTE PONER LA FINAL------------
        self.fondo.setLayout(self.horizontal)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec_())
