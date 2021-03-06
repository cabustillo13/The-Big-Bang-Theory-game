from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random 
import sys 


class Window(QMainWindow): 

    def __init__(self): 
        super().__init__() 

        ############################
        ### TITULO DE LA VENTANA ###
        ############################
        
        # Titulo de la ventana 
        self.setWindowTitle("Juego The Big Bang Theory ") 

        # Dimensiones (coordenada x,coordenada , ancho, alto)
        self.setGeometry(100, 100, 320, 470) 

        # Llamando a los componentes 
        self.UiComponents() 

        # Mostrar todos los widgets 
        self.show() 

    # Metodo para los componentes 
    def UiComponents(self): 

        # Contador 
        self.counter = -1

        # Elegir una variable 
        self.choice = 0
        
        ###########################
        ### TITULO DE LA IMAGEN ###
        ###########################
        
        # Titulo de la imagen 
        head = QLabel("Spock Lagarto", self) 

        # Dimensiones del encabezado del titulo de la imagen 
        head.setGeometry(20, 10, 280, 60) 

        # Fuentes 
        font = QFont('Monospace', 15) 
        font.setBold(True) 
        font.setItalic(True) 
        font.setUnderline(True) 

        # Definir el tipo de fuente del titulo de la imagen 
        head.setFont(font) 

        # Definir la alineacion de fuente del titulo de la imagen 
        head.setAlignment(Qt.AlignCenter) 

        # Definir el color de fuente del titulo de la imagen
        color = QGraphicsColorizeEffect(self) 
        color.setColor(Qt.darkRed) 
        head.setGraphicsEffect(color) 

        ##############################
        ### SUBTITULO DE LA IMAGEN ###
        ##############################
        
        # Titulo de la imagen 
        subhead = QLabel("Piedra Papel Tijera", self) 

        # Dimensiones del encabezado del titulo de la imagen 
        subhead.setGeometry(20, 40, 280, 60) 

        # Definir el tipo de fuente del titulo de la imagen 
        subhead.setFont(font) 

        # Definir la alineacion de fuente del titulo de la imagen 
        subhead.setAlignment(Qt.AlignCenter) 

        # Definir el color de fuente del titulo de la imagen
        color = QGraphicsColorizeEffect(self) 
        color.setColor(Qt.darkRed) 
        subhead.setGraphicsEffect(color)
        
        ############################
        ###     PIE DE IMAGEN    ###
        ############################
        
        # Pie de la imagen 
        footer = QLabel("https://github.com/cabustillo13", self) 

        # Dimensiones del pie de la imagen 
        footer.setGeometry(20, 410, 280, 60) 

        # Fuentes 
        fontFooter = QFont('Monospace', 10) 
        fontFooter.setBold(True) 
        fontFooter.setItalic(True) 
        fontFooter.setUnderline(True)

        # Definir el tipo de fuente del pie de la imagen 
        footer.setFont(fontFooter) 

        # Definir la alineacion de fuente del pie de la imagen 
        footer.setAlignment(Qt.AlignCenter) 

        # Definir el color de fuente del pie de la imagen
        color = QGraphicsColorizeEffect(self) 
        color.setColor(Qt.darkRed) 
        footer.setGraphicsEffect(color)
        
        ###########################
        ###         VRS         ###
        ###########################

        # Crear un label vrs para que se muestre en la pantalla 
        self.vs = QLabel("vrs", self) 

        # Definiendo la posicion del label vrs 
        self.vs.setGeometry(145, 110, 30, 50) 

        # Fuentes
        fontvrs = QFont('Monospace', 12)
        fontvrs.setBold(True)
        fontvrs.setUnderline(False) 
        fontvrs.setItalic(False) 
        self.vs.setFont(fontvrs) 

        ###################################
        ## TICK MOSTRAR ELECCION USUARIO ##
        ###################################
        
        # Crear label para eleccion del usuario 
        self.user = QLabel("YO", self) 

        # Definir dimensiones 
        self.user.setGeometry(50, 100, 70, 70) 
        self.user.setStyleSheet("border : 2px solid black; background : white;") 

        # Definir alineacion 
        self.user.setAlignment(Qt.AlignCenter) 

        #######################################
        ## TICK MOSTRAR ELECCION COMPUTADORA ##
        #######################################

        # Crear label para eleccion computadora 
        self.computer = QLabel("CPU", self) 

        # Definir dimensiones 
        self.computer.setGeometry(200, 100, 70, 70) 
        self.computer.setStyleSheet("border : 2px solid black; background : white;") 

        # Definir alineacion 
        self.computer.setAlignment(Qt.AlignCenter) 

        #####################
        ## LABEL RESULTADO ##
        #####################

        # Devolver resultado de etiqueta 
        self.result = QLabel(self) 

        # Definir las dimensiones del label resultado 
        self.result.setGeometry(25, 200, 270, 50) 

        # Definir fuente 
        self.result.setFont(QFont('Monospace', 14)) 

        # Definir alineacion 
        self.result.setAlignment(Qt.AlignCenter) 

        # Definir posicion y color del borde 
        self.result.setStyleSheet("border : 2px solid black; background : white;") 

        ###############
        ## 5 BOTONES ##
        ###############

        # Creacion de los botones para spock, lagarto, tijera, piedra y papel 
        self.rock = QPushButton("Piedra", self) 
        self.rock.setGeometry(30, 270, 80, 35) 

        self.paper = QPushButton("Papel", self) 
        self.paper.setGeometry(120, 270, 80, 35) 

        self.scissor = QPushButton("Tijera", self) 
        self.scissor.setGeometry(210, 270, 80, 35) 
        
        self.lagarto = QPushButton("Lagarto", self) 
        self.lagarto.setGeometry(70, 320, 80, 35)

        self.spock = QPushButton("Spock", self) 
        self.spock.setGeometry(160, 320, 80, 35)

        # Agregarle acciones a los botones 
        self.rock.clicked.connect(self.rock_action) 
        self.paper.clicked.connect(self.paper_action) 
        self.scissor.clicked.connect(self.scissor_action) 
        self.lagarto.clicked.connect(self.lagarto_action)
        self.spock.clicked.connect(self.spock_action)

        #################
        ## BOTON RESET ##
        #################
        
        # Crear un boton push para resetear el juego 
        game_reset = QPushButton("Reset", self) 

        # Definir dimensiones 
        game_reset.setGeometry(100, 370, 120, 50) 

        # Definir efectos del color
        color = QGraphicsColorizeEffect(self) 
        color.setColor(Qt.red) 
        game_reset.setGraphicsEffect(color) 

        # Agregarle un accion al boton del reset 
        game_reset.clicked.connect(self.reset_action) 

        ###########
        ## TIMER ##
        ###########
        
        # Crear el objeto timer 
        timer = QTimer(self) 

        # Agregarle accion al timer 
        timer.timeout.connect(self.showTime) 

        # Comenzar el timer 
        timer.start(1000) 

# Metodo para mostrar el tiempo
    def showTime(self): 

        # Si el valor del contador es - 1 
        if self.counter == -1: 
            pass

        # Sino es -1 
        else: 

            # Asignar el valor del contador al label
            if (self.counter !=0):
                self.computer.setText(str(self.counter))
                self.user.setText("YO")
            else:
                self.computer.setText(" ")
                self.user.setText(" ")
                
            if self.counter == 0: 
                self.comp_choice = random.randint(1, 5) 

                # Si el CPU elige 1 
                if self.comp_choice == 1: 

                    # Asignar la imagen de la piedra al label del CPU 
                    self.computer.setStyleSheet("border-image : url(Imagenes/piedra.png);") 

                elif self.comp_choice == 2: 
                    # Asignar la imagen del papel al label del CPU 
                    self.computer.setStyleSheet("border-image : url(Imagenes/papel.png);")
                    
                elif self.comp_choice == 3: 
                    # Asignar la imagen de la tijera al label del CPU 
                    self.computer.setStyleSheet("border-image : url(Imagenes/tijera.png);")
                    
                elif self.comp_choice == 4: 
                    # Asignar la imagen del lagarto al label del CPU 
                    self.computer.setStyleSheet("border-image : url(Imagenes/lagarto.png);")

                else: 
                    # Asignar la imagen de spock al label del CPU 
                    self.computer.setStyleSheet("border-image : url(Imagenes/spock.png);") 

                # Definir quien gano 
                self.who_won() 

            # Decremento del valor del contador 
            self.counter -= 1

# Metodo para la accion de la piedra
    def rock_action(self): 

        # Definir la eleccion como un 1 
        self.choice = 1

        # Asignar la imagen de la piedra al label del usuario 
        self.user.setStyleSheet("border-image : url(Imagenes/piedra.png);") 

        # Asignar el valor del contador a 3 
        self.counter = 3

        # Deshabilitar el boton push 
        self.rock.setDisabled(True) 
        self.paper.setDisabled(True) 
        self.scissor.setDisabled(True)
        self.lagarto.setDisabled(True)
        self.spock.setDisabled(True)

# Metodo para la accion del papel
    def paper_action(self): 

        # Definir la eleccion como un 2 
        self.choice = 2

        # Asignar la imagen del papel al label del usuario 
        self.user.setStyleSheet("border-image : url(Imagenes/papel.png);") 

        # Haciendo el contador como 3 
        self.counter = 3

        # Deshabilitar el boton push 
        self.rock.setDisabled(True) 
        self.paper.setDisabled(True) 
        self.scissor.setDisabled(True) 
        self.lagarto.setDisabled(True)
        self.spock.setDisabled(True)

# Metodo para la accion de la tijera
    def scissor_action(self): 

        # Definir la eleccion como un 3 
        self.choice = 3

        # Asignar la imagen de la tijera al label del usuario 
        self.user.setStyleSheet("border-image : url(Imagenes/tijera.png);") 

        # Haciendo el contador como 3 
        self.counter = 3

        # Deshabilitar el boton push 
        self.rock.setDisabled(True) 
        self.paper.setDisabled(True) 
        self.scissor.setDisabled(True)
        self.lagarto.setDisabled(True)
        self.spock.setDisabled(True)

# Metodo para la accion del lagarto
    def lagarto_action(self): 

        # Definir la eleccion como un 4 
        self.choice = 4

        # Asignar la imagen del lagarto al label del usuario 
        self.user.setStyleSheet("border-image : url(Imagenes/lagarto.png);") 

        # Haciendo el contador como 3 
        self.counter = 3

        # Deshabilitar el boton push 
        self.rock.setDisabled(True) 
        self.paper.setDisabled(True) 
        self.scissor.setDisabled(True)
        self.lagarto.setDisabled(True)
        self.spock.setDisabled(True)

# Metodo para la accion del spock
    def spock_action(self): 

        # Definir la eleccion como un 5 
        self.choice = 5

        # Asignar la imagen del spock al label del usuario 
        self.user.setStyleSheet("border-image : url(Imagenes/spock.png);") 

        # Haciendo el contador como 3 
        self.counter = 3

        # Deshabilitar el boton push 
        self.rock.setDisabled(True) 
        self.paper.setDisabled(True) 
        self.scissor.setDisabled(True)
        self.lagarto.setDisabled(True)
        self.spock.setDisabled(True)

# Metodo para la accion del reset
    def reset_action(self): 

        # Hacer el label del resultado como nulo 
        self.result.setText("") 

        # Reestablecer el valor del contador 
        self.counter = -1

        # Deshabilitar el boton push 
        self.rock.setEnabled(True) 
        self.paper.setEnabled(True) 
        self.scissor.setEnabled(True)
        self.lagarto.setEnabled(True)
        self.spock.setEnabled(True)

        # Remover las imagenes del label del CPU y usuario 
        self.user.setStyleSheet("border-image : null;") 
        self.computer.setStyleSheet("border-image : null;") 

# Metodo para definir quien gano
    def who_won(self): 

        # Si hubo empate 
        if self.choice == self.comp_choice: 

            # Mostrar el label del resultado 
            self.result.setText("Empate") 

        else: 
            # Distintas situaciones para definir quien gana 
            
            # El usuario elige piedra  
            if self.choice == 1: 
                # CPU elige papel o spack
                if (self.comp_choice == 2) or (self.comp_choice == 5): 
                    # Asignar texto a un label del resultado
                    self.result.setText("EL CPU GANÓ ¯\_(ツ)_/¯") 
                else: 
                    self.result.setText("YO GANÉ") 

            # El usuario elige papel 
            elif self.choice == 2: 
                # CPU elige tijera o lagarto
                if (self.comp_choice == 3) or (self.comp_choice == 4): 
                    # Asignar texto a un label del resultado 
                    self.result.setText("EL CPU GANÓ ¯\_(ツ)_/¯") 
                else: 
                    self.result.setText("YO GANÉ") 

            # El usuario elige tijera 
            elif self.choice == 3: 
                # CPU elige spock o piedra
                if (self.comp_choice == 5) or (self.comp_choice == 1): 
                    # Asignar texto a un label del resultado 
                    self.result.setText("EL CPU GANÓ ¯\_(ツ)_/¯") 
                else: 
                    self.result.setText("YO GANÉ")

            # El usuario elige lagarto 
            elif self.choice == 4 : 
                # CPU elige piedra o tijera
                if (self.comp_choice == 1)  or (self.comp_choice == 3): 
                    # Asignar texto a un label del resultado 
                    self.result.setText("EL CPU GANÓ ¯\_(ツ)_/¯") 
                else: 
                    self.result.setText("YO GANÉ") 
                    
            # El usuario elige spock 
            elif self.choice == 5 : 
                # CPU elige piedra 
                if (self.comp_choice == 2)  or (self.comp_choice == 4): 
                    # Asignar texto a un label del resultado 
                    self.result.setText("EL CPU GANÓ ¯\_(ツ)_/¯") 
                else: 
                    self.result.setText("YO GANÉ") 
                    
# Crear una app pyqt5  
App = QApplication(sys.argv) 

# Crear una instancia de nuestra ventada 
window = Window() 

# Run la app 
sys.exit(App.exec()) 
 


#Bibliografia: https://www.geeksforgeeks.org/pyqt5-rock-paper-and-scissor-game/
