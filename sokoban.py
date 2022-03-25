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

  def imprimirMapa(self): #imprime el mapa completo 
    for fila in self.mapa:
      print(fila)
  
  
juego = Sokoban()
juego.imprimirMapa()