# language: es

Característica: Movimientos de una entidad

#1
  Esquema del escenario: Un ente tiene una cantidad de movimientos permitidos determinados por su posicion
    Dado que hay 1 <ente> en la celda <x>
    Cuando se obtienen los posibles movimientos desde la celda <x>
    Entonces tiene <n> posibles de movimiento
    # En un tablero de tamaño 30x50
    Ejemplos:
      |ente              |x      |n    |
      |antibiotico       |(0,0)  |3    |
      |bacteriofago      |(0,49) |3    |
      |bacteria normal   |(29,0) |3    |
      |bacteria debil    |(29,49)|3    |
      |bacteria fuerte   |(0,20) |5    |
      |bacteria infectada|(15,0) |5    |
      |antibiotico       |(29,25)|5    |
      |bacteriofago      |(15,49)|5    |
      |bacteria normal   |(10,20)|8    |

#2
  Esquema del escenario: Un ente se mueve de posicion a una celda contigua
    Dado que hay 1 <nombre> en la celda <x>
    Cuando un <ente> se mueve desde la celda <x> a una celda aleatoria
    Entonces la celda <x> del <ente> es contigua a la celda destino
    
    Ejemplos:
      |nombre            |x       |ente |
      |antibiotico       |(0,0)   |a    |
      |bacteriofago      |(15,0)  |v    |
      |bacteria normal   |(10,20) |b    |
      |bacteria debil    |(2,4)   |d    |
      |bacteria fuerte   |(10,20) |f    |
      |bacteria infectada|(15,0)  |i    |
