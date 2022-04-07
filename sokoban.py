print("hola")

class Sokoban:
    """
    componentes

    0 - Cajas
    1 - Paredes
    2 - Muneco
    3 - Camino
    4 - Metas
    5 - Muneco_meta
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
    Izquierda → muneca_columna + 1
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
        [1,1,1,1,1,1,1,1,1],
        [1,3,3,3,3,3,3,3,1],
        [1,3,3,3,3,2,3,3,1],
        [1,3,3,3,3,3,3,3,1],
        [1,3,3,3,3,3,3,3,1],
        [1,1,1,1,1,1,1,1,1],
    ]
#posicón incial del muñeco en el mapa
    personaje_fila = 2
    personaje_columna = 5

    def __init__(self):
        pass

    def imprimirMapa(self): #imprime el mapa completo 
        for fila in self.mapa:
            print(fila)

    def posicionpersonaje(self):
        for fila in range(len(self.mapa)):  
            for col in range(len(self.mapa[fila])): 
                if self.mapa[fila][col] == 2: 
                    self.personaje_fila = fila
                    self.personaje_columna = col


    def moverDerecha(self):
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 3:

            self.mapa[self.personaje_fila][self.personaje_columna] = 3  # put floor character last position
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 2  # move the character to next position
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
                self.moveUp()  # Call moveUp rules
            elif moverse == "s":  # If the move is down
                self.moveDown()  # Call moveDown rules
            elif moverse == "q":  # If the move is quit
                break  # Game quit




juego = Sokoban()
juego.jugar()


  
