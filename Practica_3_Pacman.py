
import random
#Definicion de clases

"""
Clase jugador, este tendrá: para las posiciones-puntos- movimientos---- usar encapsulamiento
Clase comida, tendrá: posicion,
              y un verificardor que para saber si ya se comio, cantidad de comida que hay
Clase paredes, lo mismo que clase comida

"""
#------------------------
class Comida():
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
        self.isEat = False
        self.icon = "@"
    #Encapsulamiento
    def getIcon(self):
        return self.icon

    def  getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

    def comido(self):
        return self.isEat

    def setEat(self):
        self.isEat = True
#--------------------------
class Pared():
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
        self.isAWall = False
        self.icon = '#'
    #Encapsulamiento
    def getIcon(self):
        return self.icon

    def getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

    def pared(self):
        return self.isAWall

    def setPared(self):
        self.isAWall = True
#-----------------------------

class Player():
    def __init__(self,nombre):
        self.nombre = nombre
        self.posx = 0
        self.posy = 0
        self.puntos = 0
        self.movimientos = 0
        self.comidos = 0
        self.icon = "C"
    # Encapsulamiento
    def getIcon(self):
        return  self.icon

    def getName(self):
        return self.nombre

    def setName(self,nombre):
        self.nombre = nombre

    def getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

    def setPosX(self,posx):
        self.posx = posx

    def setPosY(self,posy):
        self.posy = posy

    def addMov(self):
        self.movimientos = self.movimientos + 1

    def addPuntos(self):
        self.puntos = self.puntos + 5
    def addComdios(self):
        self.comidos = self.comidos + 1
#------------------------------
##Creaciones
def imprimir_tablero(tablero):
    print("".center(50,'-'))

    for fila in tablero:
        print("\t| {0[0]} {0[1]} {0[2]} {0[3]} {0[4]} {0[5]} {0[6]} {0[7]} {0[8]} {0[9]} {0[10]} {0[11]} {0[12]} | ".format(fila))
    print("".center(50,'-'))

def pintar_tablero(lista_comida, lista_pared,jugador):
    tablero = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    ]
    for comida in lista_comida:
        if not comida.comido():
            tablero[comida.getPosX()][comida.getPosY()] = "@"
    for pared in lista_pared:
        tablero[pared.getPosX()][pared.getPosY()] = "#"


    tablero[jugador.getPosX()][jugador.getPosY()] = jugador.getIcon()

    return tablero

def crear_comida(lista_comida,comidaTotales = random.randint(1,int((13*13)*0.4))):
    index = 0
    while index < comidaTotales:
        x_comida = random.randint(0,12)
        y_comida = random.randint(0,12)
        comida_ocupada = False
        for comida in lista_comida:
            if comida.getPosX() == x_comida and comida.getPosY() == y_comida:
                comida_ocupada = True

        if not comida_ocupada:
            crearComida = Comida(x_comida,y_comida)
            lista_comida.append(crearComida)
            index = index + 1

def crear_pared(lista_pared, paredTotales = random.randint(1,int((13*13)*0.3))):
    index = 0
    while index < paredTotales:
        x_pared = random.randint(0,12)
        y_pared = random.randint(0,12)
        pared_ocupada = False
        for pared in lista_pared:
            if pared.getPosY() == x_pared and pared.getPosY() == y_pared:
                pared_ocupada = True
        if not pared_ocupada:
            crearPared = Pared(x_pared,y_pared)
            lista_pared.append(crearPared)
            index = index + 1

def comidaSiguiente(jugador, lista_comida):
    for comida in lista_comida:
        if jugador.getPosX() == comida.getPosX() and jugador.getPosY() == comida.getPosY():
            jugador.addPuntos()
            jugador.addComdios()
            comida.setEat()
            lista_comida.remove(comida)
            return True
    return False

def hayCOmida(lista_comida):
    for comida in lista_comida:
        if not comida.comido:
            return False
    return True

def paredSiguiente(jugador,lista_pared):
    for pared in lista_pared:
        if jugador.getPosX() == pared.getPosX() and jugador.getPosY() + 1 == pared.getPosY():
            pared.setPared()
            return True
    return False

def paredSiguiente2(jugador,lista_pared):
    for pared in lista_pared:
        if jugador.getPosX() == pared.getPosX() and jugador.getPosY() - 1 == pared.getPosY():
            pared.setPared()
            return True
    return False

def paredSiguiente3(jugador,lista_pared):
    for pared in lista_pared:
        if jugador.getPosX() - 1 == pared.getPosX() and jugador.getPosY() == pared.getPosY():
            pared.setPared()
            return True
    return False

def paredSiguiente4(jugador,lista_pared):
    for pared in lista_pared:
        if jugador.getPosX() + 1 == pared.getPosX() and jugador.getPosY() == pared.getPosY():
            pared.setPared()
            return True
    return False

def movimiento(jugador,lista_comida,lista_pared):
    #Crear comida
    #crear_items(lista_comida,lista_pared)
    crear_comida(lista_comida)
    crear_pared(lista_pared)
    #Imprimir el tablero
    tablero = pintar_tablero(lista_comida,lista_pared,jugador)
    imprimir_tablero(tablero)
    print(f'Cantidad de comida creada {len(lista_comida)}---cantidad de paredes creadas {len(lista_pared)}')
    print("""
                _______________________________
                Movimientos
                -------------------------------
                A - Izquierda
                W - Arriba
                S - Abajo
                D - Derecha
                E - Salir
                -------------------------------
                @ - Comida 5 puntos
                # - No se puede mover
                ------------------------------
                Gana al obtener 40 pts
                -------------------------------
                Ingrese una opción...
    """)

    while True:
        tecla = input("Ingrese su movimiento: ")
        #Hacia la derecha
        if tecla == "d":
            comidaS = comidaSiguiente(jugador,lista_comida)
            paredS = paredSiguiente(jugador, lista_pared)
            if comidaS:
                jugador.setPosY(jugador.getPosY() + 1)
                jugador.addMov()
                print(f'-JUGADOR {jugador.getName()} - PUNTOS {jugador.puntos} - MOVIMIENTOS {jugador.movimientos} - COMIDA OBTENIDA {jugador.comidos} - COMIDA RESTANTE {len(lista_comida)}')
                tablero = pintar_tablero(lista_comida, lista_pared, jugador)
                imprimir_tablero(tablero)
            elif paredS:
                print(f'-JUGADOR {jugador.getName()} - PUNTOS {jugador.puntos} - MOVIMIENTOS {jugador.movimientos} - COMIDA OBTENIDA {jugador.comidos} - COMIDA RESTANTE {len(lista_comida)}')
                tablero = pintar_tablero(lista_comida, lista_pared, jugador)
                imprimir_tablero(tablero)
            else:
                jugador.setPosY(jugador.getPosY() + 1)
                jugador.addMov()
                print(f'-JUGADOR {jugador.getName()} - PUNTOS {jugador.puntos} - MOVIMIENTOS {jugador.movimientos} - COMIDA OBTENIDA {jugador.comidos} - COMIDA RESTANTE {len(lista_comida)}')
                tablero = pintar_tablero(lista_comida, lista_pared, jugador)
                imprimir_tablero(tablero)
        #Hacia la izquierda
        if tecla == "a":
            comidaS = comidaSiguiente(jugador,lista_comida)
            paredS2 = paredSiguiente2(jugador, lista_pared)
            if comidaS:
                jugador.setPosY(jugador.getPosY() - 1)
                jugador.addMov()
                print(f'-JUGADOR {jugador.getName()} - PUNTOS {jugador.puntos} - MOVIMIENTOS {jugador.movimientos} - COMIDA OBTENIDA {jugador.comidos} - COMIDA RESTANTE {len(lista_comida)}')
                tablero = pintar_tablero(lista_comida, lista_pared, jugador)
                imprimir_tablero(tablero)
            elif paredS2:
                print(f'-JUGADOR {jugador.getName()} - PUNTOS {jugador.puntos} - MOVIMIENTOS {jugador.movimientos} - COMIDA OBTENIDA {jugador.comidos} - COMIDA RESTANTE {len(lista_comida)}')
                tablero = pintar_tablero(lista_comida, lista_pared, jugador)
                imprimir_tablero(tablero)
            else:
                jugador.setPosY(jugador.getPosY() - 1)
                jugador.addMov()
                print(f'-JUGADOR {jugador.getName()} - PUNTOS {jugador.puntos} - MOVIMIENTOS {jugador.movimientos} - COMIDA OBTENIDA {jugador.comidos} - COMIDA RESTANTE {len(lista_comida)}')
                tablero = pintar_tablero(lista_comida, lista_pared, jugador)
                imprimir_tablero(tablero)
        #Hacia arriba
        if tecla == "w":
            comidaS = comidaSiguiente(jugador, lista_comida)
            paredS3 = paredSiguiente3(jugador, lista_pared)
            if comidaS:
                jugador.setPosX(jugador.getPosX() - 1)
                jugador.addMov()
                print(
                    f'-JUGADOR {jugador.getName()} - PUNTOS {jugador.puntos} - MOVIMIENTOS {jugador.movimientos} - COMIDA OBTENIDA {jugador.comidos} - COMIDA RESTANTE {len(lista_comida)}')
                tablero = pintar_tablero(lista_comida, lista_pared, jugador)
                imprimir_tablero(tablero)
            elif paredS3:
                print(
                    f'-JUGADOR {jugador.getName()} - PUNTOS {jugador.puntos} - MOVIMIENTOS {jugador.movimientos} - COMIDA OBTENIDA {jugador.comidos} - COMIDA RESTANTE {len(lista_comida)}')
                tablero = pintar_tablero(lista_comida, lista_pared, jugador)
                imprimir_tablero(tablero)
            else:
                jugador.setPosX(jugador.getPosX() - 1)
                jugador.addMov()
                print(
                    f'-JUGADOR {jugador.getName()} - PUNTOS {jugador.puntos} - MOVIMIENTOS {jugador.movimientos} - COMIDA OBTENIDA {jugador.comidos} - COMIDA RESTANTE {len(lista_comida)}')
                tablero = pintar_tablero(lista_comida, lista_pared, jugador)
                imprimir_tablero(tablero)
        #Hacia abajo
        if tecla == "s":
            comidaS = comidaSiguiente(jugador, lista_comida)
            paredS4 = paredSiguiente4(jugador, lista_pared)
            if comidaS:
                jugador.setPosX(jugador.getPosX() + 1)
                jugador.addMov()
                print(
                    f'-JUGADOR {jugador.getName()} - PUNTOS {jugador.puntos} - MOVIMIENTOS {jugador.movimientos} - COMIDA OBTENIDA {jugador.comidos} - COMIDA RESTANTE {len(lista_comida)}')
                tablero = pintar_tablero(lista_comida, lista_pared, jugador)
                imprimir_tablero(tablero)
            elif paredS4:
                print(
                    f'-JUGADOR {jugador.getName()} - PUNTOS {jugador.puntos} - MOVIMIENTOS {jugador.movimientos} - COMIDA OBTENIDA {jugador.comidos} - COMIDA RESTANTE {len(lista_comida)}')
                tablero = pintar_tablero(lista_comida, lista_pared, jugador)
                imprimir_tablero(tablero)
            else:
                jugador.setPosX(jugador.getPosX() + 1)
                jugador.addMov()
                print(
                    f'-JUGADOR {jugador.getName()} - PUNTOS {jugador.puntos} - MOVIMIENTOS {jugador.movimientos} - COMIDA OBTENIDA {jugador.comidos} - COMIDA RESTANTE {len(lista_comida)}')
                tablero = pintar_tablero(lista_comida, lista_pared, jugador)
                imprimir_tablero(tablero)
        if tecla == "e":
            print("Has salido del la partida")
            break
        if jugador.puntos >= 40 or len(lista_comida)==0:
            print("PARTIDA TERMINADA")
            print(
                f'-JUGADOR {jugador.getName()} - PUNTOS {jugador.puntos} - MOVIMIENTOS {jugador.movimientos} - COMIDA OBTENIDA {jugador.comidos}')
            jugadores_en_partida.append(jugador)
            #Cleaning
            del lista_comida[:]
            del lista_pared[:]
            break





#FUNCINALIDAD-------------------
def iniciar_juego():

    while True:
        menu = """
                _______________________________
                Bienvenidos a Pac man en Python
                -------------------------------
                1. Iniciar Juego
                2. Tabla de posiciones
                3. Salir
                -------------------------------
                Ingrese una opción...
            """
        print(menu)
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            print("Iniciando Juego...")
            name = str(input("Ingrese su nombre:  "))
            jugadorMain = Player(name)

            #Llamamos el metodo
            movimiento(jugadorMain,lista_comida,lista_pared)

        if opcion == 2:
            print("Tabla de posiciones...")
            jugadores_en_partida.sort(key=lambda x: x.movimientos)
            first_three = jugadores_en_partida[:3]
            for jugador in first_three:
                print(f'Jugador - {jugador.getName()} - Movimientos {jugador.movimientos} - Puntos {jugador.puntos}')
        if opcion == 3:
            print("Espero te hayas divertido...")
            break


#Arreglos globales
lista_comida = []
lista_pared = []
jugadores_en_partida = []
iniciar_juego()

#python Practica_3_Pacman.py