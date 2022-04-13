print("hola")


class Sokoban:
    """
    Reglas para moverse (Arriba, Derecha, Abajo, Izquierda)

    0 - Muneco, camino
    1 - Muneco, camino
    2 - Muneco, caja, camino
    3 - Muneco, caja, meta
    4 - Muneco, caja_meta, camino
    5 - Muneco, caja_meta, meta
    6 - Muneco_meta, camino
    7 - Muneco_meta, camino
    8 - Muneco_meta, caja, camino
    9 - Muneco_meta, caja, meta
    0 - Muneco_meta, caja_meta, camino
    1 - Muneco_meta, caja_meta, meta
    """
    
    #Componentes
    caja = 0
    pared = 1
    personaje = 2
    espacio = 3
    meta = 4
    personaje_meta = 5
    caja_meta = 6

    mapa = [
        [1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
        [1, 3, 3, 3, 3, 3, 3, 3, 3, 1],
        [1, 3, 3, 0, 3, 2, 3, 0, 3, 1],
        [1, 3, 3, 3, 3, 3, 3, 3, 3, 1],
        [1, 3, 3, 0, 3, 3, 4, 4, 3, 1],
        [1, 3, 3, 3, 3, 3, 4, 4, 3, 1],
        [1, 3, 3, 3, 3, 3, 3, 3, 3, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
    ]
    #posicón incial del personaje en el mapa
    personaje_fila = 0
    personaje_columna = 0

    def __init__(self): #inicia la clase
        pass

    def imprimirMapa(self):  #imprime el mapa completo
        for fila in self.mapa: #para todas las filas del mapa
            print(fila)

    def posicionpersonaje(self): #define la posición del personaje
        for fila in range(len(self.mapa)): #obtiene numero de filas en el mapa
            for col in range(len(self.mapa[fila])): #obtiene numero de columnas en el mapa
                if self.mapa[fila][col] == 2: #indica el valor de personaje
                    self.personaje_fila = fila #actualiza la posición del personaje en la fila
                    self.personaje_columna = col #actualiza la posición del personaje en columna

    #definimos los movimientos
                    
    def moverDerecha(self): #define reglas para movimientos a la derecha
        #1 personaje espacio [2,3 ➔ 3, 2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 3:
            print("derecha - personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 2  
            self.personaje_columna = self.personaje_columna + 1
        #2 personaje,meta [2,4 ➔ 3,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            print("derecha - personaje, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 5  
            self.personaje_columna += 1
        #3 personaje, caja, espacio [2,0,3 ➔ 3,2,0]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 3 :
            print("derecha - personaje,caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 2
            self.mapa[self.personaje_fila][self.personaje_columna +2] = 0  
            self.personaje_columna = self.personaje_columna + 1
        #4 personaje, caja, meta (2,0,4 ➔ 3,2,6)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4 :
            print("derecha - personaje,caja,meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 2
            self.mapa[self.personaje_fila][self.personaje_columna +2] = 6  
            self.personaje_columna = self.personaje_columna + 1   
        #5 personaje, caja_meta, espacio (2,6,3 ➔ 3,5,0)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 3 :
            print("derecha - personaje,caja_meta,espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna +2] = 0  
            self.personaje_columna = self.personaje_columna + 1 
        #6 personaje,caja_meta, meta (2,6,4 ➔ 3,5,6)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4 :
            print("derecha - personaje,caja_meta,meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna +2] = 6  
            self.personaje_columna = self.personaje_columna + 1 
        #7 personaje_meta, espacio (5,3 ➔ 4,2)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 3:
            print("derecha - personaje, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 2  
            self.personaje_columna += 1
        #8 personaje_meta, meta (5,4 ➔ 4,5)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            print("derecha - personaje_meta, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 5  
            self.personaje_columna += 1
        #9 personaje_meta, caja, espacio (5,0,3 ➔ 4,2,0)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 3 :
            print("derecha - personaje_meta,caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 2
            self.mapa[self.personaje_fila][self.personaje_columna +2] = 0  
            self.personaje_columna = self.personaje_columna + 1
        #10 personaje_meta, caja, meta (5,0,4 ➔ 4,2,6)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4 :
            print("derecha - personaje_meta,caja,meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 2
            self.mapa[self.personaje_fila][self.personaje_columna +2] = 6  
            self.personaje_columna = self.personaje_columna + 1
        #11 personaje_meta, caja_meta, espacio (5,6,3 ➔ 4,5,0)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 3 :
            print("derecha - personaje_meta,caja_meta,espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna +2] = 0  
            self.personaje_columna = self.personaje_columna + 1
        #12 personaje_meta, caja_meta, meta (5,6,4 ➔ 4,5,6)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4 :
            print("derecha - personaje_meta,caja_meta,meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna +1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna +2] = 6  
            self.personaje_columna = self.personaje_columna + 1
        
    def moverIzquierda(self):  #define reglas para movimientos a la izquierda
        #1personaje, espacio [2,3 🠔 3,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 3:
            print("izquierda - personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 2
            self.personaje_columna -= 1
        #2personaje,meta [5,3 🠔  4,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
            print("izquierda - personaje, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5  
            self.personaje_columna = self.personaje_columna - 1
        #3personaje, caja, espacio [0, 2, 3 🠔 3,0,2]   
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 3 :
            print("izquierda - personaje,caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna -1] = 2
            self.mapa[self.personaje_fila][self.personaje_columna -2] = 0  
            self.personaje_columna = self.personaje_columna - 1
        #4 personaje, caja, meta (2,0,4 🠔 3,2,6)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4 :
            print("izquierda - personaje,caja,meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna -1] = 2
            self.mapa[self.personaje_fila][self.personaje_columna -2] = 6  
            self.personaje_columna = self.personaje_columna - 1 
        #5 personaje, caja_meta, espacio (0,5,3 🠔 3,6,2)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 3 :
            print("izquierda - personaje,caja_meta,espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3 
            self.mapa[self.personaje_fila][self.personaje_columna -1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna -2] = 0  
            self.personaje_columna = self.personaje_columna - 1 
        #6 personaje,caja_meta, meta (6,5,3 🠔 4,6,2) 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4 :
            print("izquierda - personaje,caja_meta,meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3 
            self.mapa[self.personaje_fila][self.personaje_columna -1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna -2] = 6  
            self.personaje_columna = self.personaje_columna - 1 
        #7 personaje_meta, espacio (2,4 🠔 3,5)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 3:
            print("izquierda - personaje_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 2  
            self.personaje_columna = self.personaje_columna - 1
        #8 personaje_meta, meta (5,4 🠔 4,5)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
            print("izquierda - personaje_meta, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5 
            self.personaje_columna = self.personaje_columna - 1
        #9 personaje_meta, caja, espacio (0,2,4 🠔 3,0,5)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 3 :
            print("izquierda - personaje_meta, caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna -1] = 2
            self.mapa[self.personaje_fila][self.personaje_columna -2] = 0  
            self.personaje_columna = self.personaje_columna - 1
        #10 personaje_meta, caja, meta (6,2,4 🠔 4,0,5)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4 :
            print("izquierda - personaje_meta, caja, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna -1] = 2
            self.mapa[self.personaje_fila][self.personaje_columna -2] = 6  
            self.personaje_columna = self.personaje_columna - 1
        #11 personaje_meta, caja_meta, espacio (0,5,4 🠔 3,6,5)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 3 :
            print("izquierda - personaje_meta, caja_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna -1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna -2] = 0  
            self.personaje_columna = self.personaje_columna - 1
        #12 personaje_meta, caja_meta, meta (6,5,4 🠔 4,6,5)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4 :
            print("izquierda - personaje_meta, caja_meta, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna -1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna -2] = 6  
            self.personaje_columna = self.personaje_columna - 1
        
    def moverArriba(self):  #define reglas para movimientos arriba
        #1 personaje, espacio [2,3 🠕 3,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 3:
            print("arriba - personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 2
            self.personaje_fila = self.personaje_fila - 1
        #2 personaje,meta [2,4 🠕 3,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            print("arriba - personaje, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5  
            self.personaje_fila = self.personaje_fila - 1
        #3 personaje, caja, espacio [2,0,3 🠕 3,2,0]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 3:
            print("arriba - personaje,caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 0  
            self.personaje_fila = self.personaje_fila - 1
        #4 personaje, caja, meta (2,0,4  🠕 3,2,6)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4 :
            print("arriba - personaje,caja,meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6  
            self.personaje_fila = self.personaje_fila - 1
        #5 personaje, caja_meta, espacio (2,6,3  🠕 3,5,0)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 3 :
            print("arriba - personaje,caja_meta,espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 0  
            self.personaje_fila = self.personaje_fila - 1
        #6 personaje,caja_meta, meta (2,6,4 🠕 3,5,6)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4 :
            print("arriba - personaje,caja_meta,meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6 
            self.personaje_fila = self.personaje_fila - 1 
        #7 personaje_meta, espacio (5,3 🠕 4,2)
        if self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 3:
            print("arriba - personaje_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 2
            self.personaje_fila = self.personaje_fila - 1
        #8 personaje_meta, meta (5,4 🠕 4,5)
        if self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            print("arriba - personaje_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.personaje_fila = self.personaje_fila - 1
        #9 personaje_meta, caja, espacio (5,0,3 🠕 4,2,0)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 3 :
            print("arriba - personaje_meta, caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 0  
            self.personaje_fila = self.personaje_fila - 1
        #10 personaje_meta, caja, meta (5,0,4 🠕 4,2,6)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4 :
            print("arriba - personaje_meta, caja, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6  
            self.personaje_fila = self.personaje_fila - 1
        #11 personaje_meta, caja_meta, espacio (5,6,3 🠕 4,5,0)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 3 :
            print("arriba - personaje_meta, caja_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 0  
            self.personaje_fila = self.personaje_fila - 1
        #12 personaje_meta, caja_meta, meta (5,6,4 🠕 4,5,6)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4 :
            print("arriba - personaje_meta, caja_meta, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6  
            self.personaje_fila = self.personaje_fila - 1
    def moverAbajo(self):  #define reglas para movimientos abajo
        #1personaje, espacio [2,3 🠗 3,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 3:
            print("abajo - personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 2
            self.personaje_fila = self.personaje_fila + 1
        #2personaje,meta [2,4 🠗 3,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            print("abajo - personaje, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3 
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5  
            self.personaje_fila = self.personaje_fila + 1
        #3personaje, caja, espacio [2,0,3 🠗 3,2,0]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 3 :
            print("abajo - personaje,caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 0 
            self.personaje_fila = self.personaje_fila + 1
        #4 personaje, caja, meta (2,0,4 🠗 3,2,6)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4 :
            print("abajo - personaje,caja,meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6  
            self.personaje_fila = self.personaje_fila + 1
        #5 personaje, caja_meta, espacio (2,6,3  🠗 3,5,0)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 3 :
            print("abajo - personaje,caja_meta,espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 0 
            self.personaje_fila = self.personaje_fila + 1
        #6 personaje,caja_meta, meta (2,6,4 🠗 3,5,6)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4 :
            print("abajo - personaje,caja_meta,meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6 
            self.personaje_fila = self.personaje_fila + 1
        #7 personaje_meta, espacio (5,3 🠗 4,2)
        if self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 3:
            print("abajo - personaje_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 2
            self.personaje_fila = self.personaje_fila + 1
        #8 personaje_meta, meta (5,4 🠗 4,5)
        if self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            print("abajo - personaje_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.personaje_fila = self.personaje_fila + 1
        #9 personaje_meta, caja, espacio (5,0,3 🠗 4,2,0)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 3 :
            print("abajo - personaje_meta, caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 0  
            self.personaje_fila = self.personaje_fila + 1
        #10 personaje_meta, caja, meta (5,0,4 🠗 4,2,6)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4 :
            print("abajo - personaje_meta, caja, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6  
            self.personaje_fila = self.personaje_fila + 1
        #11 personaje_meta, caja_meta, espacio (5,6,3 🠗 4,5,0)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 3 :
            print("abajo - personaje_meta, caja_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 0  
            self.personaje_fila = self.personaje_fila + 1
        #12 personaje_meta, caja_meta, meta (5,6,4 🠗 4,5,6)
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4 :
            print("abajo - personaje_meta, caja_meta, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6  
            self.personaje_fila = self.personaje_fila + 1
        
    #definimos el juego       

    """
    POWERUP: 
    Doble salto, solo cuando tenemos [personaje, espacio] en cualquier dirección
    """
    def dobleSaltoDerecha(self):
        #POWERUP personaje, espacio [2,3 ➔ 3, 2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 3:
            print("derecha doble salto - personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3  
            self.mapa[self.personaje_fila][self.personaje_columna +2] = 2  
            self.personaje_columna = self.personaje_columna + 2
    def dobleSaltoIzquierda(self):
        #POWERUP personaje, espacio [2,3 🠔 3,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 3:
            print("doble salto izquierda - personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2
            self.personaje_columna -= 2
    def dobleSaltoArriba(self):
        #POWERUP personaje, espacio [2,3 🠕 3,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 3:
            print("doble salto arriba - personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 2
            self.personaje_fila = self.personaje_fila - 2
    def dobleSaltoAbajo(self):
        #POWERUP personaje, espacio [2,3 🠗 3,2]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 2 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 3:
            print(" doble salto abajo - personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 2
            self.personaje_fila = self.personaje_fila + 2

    #Definimos el juego
    def jugar(self):
        self.imprimirMapa()  # Llama al mapa
        self.posicionpersonaje()  # Localiza la posicón del personaje en el mapa
        instructiones = "d-derecha, a-izquierda, w-arriba, s-abajo"  # Instructiones
        print(instructiones) 
        while True:  # Bucle infinito
            self.imprimirMapa()  #Llama al metodo imprimirMapa
            moverse = input("Moverse a: ")  #Pregunta hacia donde moverse
            if moverse == "a":  # si se desea moverse a la izquiera
                self.moverIzquierda()  # Call moveLeft rules
            elif moverse == "d":  #se se desea moverse a la derecha
                self.moverDerecha()  # Call moveRight rules
            elif moverse == "w":  #Moverse Arriba
                self.moverArriba()  # Call moveUp rules
            elif moverse == "s":  # Moverse abajo
                self.moverAbajo()  # Call moveDown rules
            elif moverse == "l":
                self.dobleSaltoDerecha()
            elif moverse == "i":
                self.dobleSaltoArriba()
            elif moverse == "k":
                self.dobleSaltoAbajo()
            elif moverse == "j":
                self.dobleSaltoIzquierda()
            elif moverse == "q":  # If the move is quit
                break  # Game quit


juego = Sokoban()
juego.jugar()
