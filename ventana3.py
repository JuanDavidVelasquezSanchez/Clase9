import sys
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton, QApplication
from PyQt5 import QtGui

from cliente import Cliente



class Ventana3(QMainWindow):

    # hacer el metodo de construccion de la ventana
    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)

        # creamos un atributo que guarde la ventana anterior
        self.ventanaAnterior = anterior

        #poner el titulo
        self.setWindowTitle("Usuarios Registrados")

        # poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/bag.png'))

        # establecemos las propiedades del ancho y el alto
        self.ancho = 900
        self.alto = 600

        # establecemos el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # hacer que la ventana se vea en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.top())

        # fijar el alto y el ancho de la ventana
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        # definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/Paisaje.png')

        # definimos la imagen de fonodo
        self.fondo.setPixmap(self.imagenFondo)

        # establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # establecemos la ventana fondo como la venta central
        self.setCentralWidget(self.fondo)

        # abrimos el archivo en modo lectura
        self.file = open('datos/clientes.txt', 'rb' )

        # lista vacia para guardar usuarios
        self.usuarios = []

        # recorremos el archivo linea por linea
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")
            if linea == '':
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
                # metemos el objetivo a la lista de usuarios
                self.usuarios.append(u)

            # cerramos el archivo:
            self.file.close()

            self.numeroUsuarios = len(self.usuarios)

            # contador de elementos
            self.contador = 0

            # establecemos la distrubucion de los elemnetos en el layout vertical
            self.vertical = QVBoxLayout()

            # hacemos el letrero
            self.letrero1 = QLabel()

            # le escribimos el texto
            self.letrero1.setText("Usuarios Registrados")

            # le asignamos el tipo de letra
            self.letrero1.setFont(QFont("Andale Mono", 20))

            # le ponemos el color de texto y m,argenes
            self.letrero1.setStyleSheet("color: 000080;")

            # agregamos el letrero en la primera fila
            self.vertical.addWidget(self.letrero1)

            # ponemos un espacio despues
            self.vertical.addStretch()

            # creamos un scroll
            self.scrollArea = QScrollArea()

            # hacemos que el scroll se adaote a diferentes tamaños
            self.scrollArea.setWidgetResizable(True)

            # creamos una tabla
            self.tabla = QTableWidget

            # definimos el numero de columnas que tendra la tabla
            self.tabla.setColumnCount(11)

            # definimos el ancho de cada columna
            self.tabla.setColumnWidth(0,150)
            self.tabla.setColumnWidth(1,150)
            self.tabla.setColumnWidth(2, 150)
            self.tabla.setColumnWidth(3, 150)
            self.tabla.setColumnWidth(4, 150)
            self.tabla.setColumnWidth(5, 150)
            self.tabla.setColumnWidth(6, 150)
            self.tabla.setColumnWidth(7, 150)
            self.tabla.setColumnWidth(8, 150)
            self.tabla.setColumnWidth(9, 150)
            self.tabla.setColumnWidth(10, 150)

            # definimos el texto de la cabecera
            self.tabla.setHorizontalHeaderLabels(['Nombre', 'Usuario', 'Password', 'Documento', 'Correo', 'Pregunta 1', 'Respuesta 1', 'Preunta 2', 'Respuesta 2', 'Pregunta 3', 'Respuesta 3'])

            # establecemos el numero de filas
            self.tabla.setRowCount(self.numeroUsuarios)

            # Llamamos la tabla
            for u in self.usuarios:
                self.tabla.setItem(self.contador,0, QTableWidgetItem(u.nombreCompleto))
                self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
                self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.password))
                self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
                self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
                self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
                self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
                self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta2))
                self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
                self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.pregunta3))
                self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
                self.contador += 1

            # metemos la tabla en el scroll
            self.scrollArea.setWidget(self.tabla)

            # metemos el layout vertical en el scroll}
            self.vertical.addWidget(self.scrollArea)

            # pomemos un espacio depues
            self.vertical.addStretch()

            # --------- BOTON VOLVER ------
            # Hacemos el boton volver para devolvernos a la ventana anterior:
            self.botonVolver = QPushButton("Volver")

            # Establece el ancho del boton:
            self.botonVolver.setFixedWidth(90)

            # Le ponemos los estilos:
            self.botonVolver.setStyleSheet("background-color: #008B45;"
                                           "color: #FFFFFF;"
                                           "padding: 10px;"
                                           "margin-top: 10px;"
                                           )

            # Hacemos que el boton botonContinuar tenga su metodo:
            self.botonVolver.clicked.connect(self.metodo_accionVolver)

            # Metemos en el layout vertical el botonVolver:
            self.vertical.addWidget(self.botonVolver)

            # -------- OJO IMPORTANTE PONER AL FINAL -------

            # Indicamos que el layout principal del fondo es horizontal:
            self.fondo.setLayout(self.vertical)

            def metodo_accionVolver(self):
                self.hide()
                self.ventanaAnterior.show()


if __name__== '__main__':

    app = QApplication(sys.argv)

    ventana3 = Ventana3

    ventana3.show()

    sys.exit(app.exec_())


    py





