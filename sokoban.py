print("hola")


class Sokoban:
    """
    componentes

    0 - Caja
    1 - Pared
    2 - personaje
    3 - Camino
    4 - Meta
    5 - Personaje_meta
    6 - Caja_meta

    Reglas validas para moverse (Arriba, Derecha, Abajo, Izquierda)

    00 - Muneco, camino → [2,3] → [3,2]
    01 - Muneco, camino
    02 - Muneco, caja, camino
    03 - Muneco, caja, meta
    04 - Muneco, caja_meta, camino
    05 - Muneco, caja_meta, meta

    06 - Muneco_meta, camino
    07 - Muneco_meta, camino
    08 - Muneco_meta, caja, camino
    09 - Muneco_meta, caja, meta
    10 - Muneco_meta, caja_meta, camino
    11 - Muneco_meta, caja_meta, meta

    Derecha → muneco_calumna + 1
    Izquierda → muneca_columna - 1
    Abajo → muneco_fila + 1
    Arriba muneco_fila - 1
    """

    caja = 0
    pared = 1
    muneco = 2
    espacio = 3
    meta = 4
    personaje_meta = 5
    caja_meta = 6

    mapa = [
        [1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
        [1, 3, 3, 3, 3, 3, 3, 3, 3, 1],
        [1, 3, 3, 0, 3, 2, 3, 3, 3, 1],
        [1, 3, 3, 3, 3, 3, 3, 3, 3, 1],
        [1, 3, 3, 3, 3, 3, 3, 4, 3, 1],
        [1, 3, 3, 3, 3, 3, 3, 3, 3, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
    ]
    #posicón incial del personaje en el mapa
    personaje_fila = 2
    personaje_columna = 5

    def __init__(self): #inicia la clase
        pass

    def imprimirMapa(self):  #imprime el mapa completo
        for fila in self.mapa:
            print(fila)

    def posicionpersonaje(self): #define la posición del personaje
        for fila in range(len(self.mapa)):
            for col in range(len(self.mapa[fila])):
                if self.mapa[fila][col] == 2:
                    self.personaje_fila = fila
                    self.personaje_columna = col

    #personaje espacio
    def moverDerecha(self):
        print("mover derecha")
        #personaje espacio [2,3 ➔ 3, 2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 3:
            print("derecha - personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 2  
            self.personaje_columna = self.personaje_columna + 1
        #personaje,meta [2,4 ➔ 3,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            print("derecha - personaje, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 5  
            self.personaje_columna = self.personaje_columna + 1
        #personaje, caja, espacio [2,0,3 ➔ 3,2,0]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 3 :
            print("derecha - personaje,caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 2
            self.mapa[self.personaje_fila][self.personaje_columna +2] = 0  
            self.personaje_columna = self.personaje_columna + 1

    
    def moverIzquierda(self):
        #personaje, espacio [2,3 🠔 3,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 3:
            print("izquierda - personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 2
            self.personaje_columna = self.personaje_columna - 1
        #personaje,meta [5,3 🠔  4,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
            print("derecha - personaje, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5  
            self.personaje_columna = self.personaje_columna - 1

    def moverArriba(self):
        #personaje, espacio [2,3 🠕 3,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 3:
            print("arriba - personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 2
            self.personaje_fila = self.personaje_fila - 1
        #personaje,meta [2,4 🠕 3,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            print("arriba - personaje, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5  
            self.personaje_fila = self.personaje_fila - 1

    def moverAbajo(self):
        #personaje, espacio [2,3 🠗 3,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 3:
            print("abajo - personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 2
            self.personaje_fila = self.personaje_fila + 1

    #personaje,meta

        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            print("derecha - personaje, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 2  
            self.personaje_columna = self.personaje_columna + 1

    
    def jugar(self):
        self.imprimirMapa()  # Call the map
        self.posicionpersonaje()  # Update the character position for new map
        instructiones = "d-derecha, a-izquierda, w-arriba, s-abajo"  # Instructions
        print(instructiones)  # Print the instructions
        while True:  # Infinite loop
            self.imprimirMapa()  # Call the printMap method
            moverse = input("Moverse a: ")  # Ask for the move
            if moverse == "a":  # If the move is left
                self.moverIzquierda()  # Call moveLeft rules
            elif moverse == "d":  # If the move is right
                self.moverDerecha()  # Call moveRight rules
            elif moverse == "w":  # If the move is up
                self.moverArriba()  # Call moveUp rules
            elif moverse == "s":  # If the move is down
                self.moverAbajo()  # Call moveDown rules
            elif moverse == "q":  # If the move is quit
                break  # Game quit


juego = Sokoban()
juego.jugar()
