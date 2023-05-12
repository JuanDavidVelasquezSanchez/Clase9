import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton
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
        self.ladoIzquierdo = QFormLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("Informacion del Cliente")

        #Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andale Mono", 20))

        #le ponemos color de texto y margenes:
        self.letrero1.setStyleSheet("color: white;")

        #Agregamos el letrero en la primera fila:
        self.ladoIzquierdo.addRow(self.letrero1)

        #hacemos el letrero
        self.letrero2 = QLabel()

        #Establcemos el ancho del label
        self.letrero2.setFixedWidth(340)

        #Le escribimos el texto
        self.letrero2.setText("por favor ingresar la informacion del cliente"
                              "\nen el formulario de abajo, los campos marcados"
                              "\ncon asteriscos son obligatorios.")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andale Mono", 10))

        #Le ponemos color de texto y imagen
        self.letrero2.setStyleSheet("color: white; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid white;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")
        
        #agregamos el letrero en la fila siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)

        #Hacemos el campo para ingresar el nombre:
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        #Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        #Hacemos el campo de usuario:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        #Agregamos esto en el formulario:
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        #Hacemos el campo para ingresar password:
        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        #Agregamos esto en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password)

        # Hacemos el campo para ingresar password:
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        #Agregamos esto a el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password2)

        #Hacemos el campo para ingresar documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        #agregamos esto a el formulario:
        self.ladoIzquierdo.addRow("Documento", self.documento)

        #hacemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        #Agregamos esto a el formulario:
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        #hacemos el boton para registrar los datos:
        self.botonRegistrar = QPushButton("Registrar")

        #Especificamos el ancho del boton:
        self.botonRegistrar.setFixedWidth(90)

        #le ponemos los estilos:
        self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        #Hacemos el boto para limpiar los datos:
        self.botonLimpiar = QPushButton("Limpiar")

        #Establecemos el ancho:
        self.botonLimpiar.setFixedWidth(90)

        # le ponemos los estilos:
        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        #Agregamso los dos botones al layout ladoIzquierdo:
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        # Agregamos el layoutIzquierdo el layout horizontal
        self.horizontal.addLayout(self.ladoIzquierdo)


        #-------------------OJO IMPORTANTE PONER LA FINAL------------
        self.fondo.setLayout(self.horizontal)


    #Hacemos el metodo de botonLimpiar:
    def accion_botonLimpiar(self):
        pass

    #Metodo del boton registrar
    def accion_botonRegistrar(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec_())
