print("hola")

class Sokoban:
  """
  Definimos los componentes

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

  mapa = [
    [1,1,1,1,1,1,1,1,1],
    [1,3,3,3,3,3,3,3,1],
    [1,3,3,3,3,2,3,3,1],
    [1,3,3,3,3,3,3,3,1],
    [1,3,3,3,3,3,3,3,1],
    [1,1,1,1,1,1,1,1,1],
  ]
  #posicón incial del muñeco en el mapa
  muneco_fila = 2
  muneco_columna = 5

  def __init__(self):
    pass
  
  def imprimirMapa(self): #imprime el mapa completo 
    for fila in self.mapa:
      print(fila)

  def posicionmuneco(self):
        for f in range(len(self.map)):  
            for c in range(len(self.map[f])): 
                if self.map[f][c] == 0: 
                    self.muneco_fila = f
                    self.muneco_columna = c 


   def moverDerecha(self):
        if (
            self.mapa[self.muneco_fila][self.muneco_columna] == 2
            and self.map[self.muneco_fila][self.muneco_columna + 1] == 1
        ): 
            self.map[self.muneco_fila][self.muneco_columna] = 1  
            self.map[self.muneco_fila][self.muneco_columna + 1] = 0  
            self.muneco_columna = self.muneco_columna + 1 
          
      
juego = Sokoban()
juego.imprimirMapa()

  
