# language: es

Característica: Movimientos de una entidad

#1
  Esquema del escenario: Un ente tiene una cantidad de movimientos permitidos determinados por su posicion
    Dado que hay 1 <ente> en la celda <x>
    Cuando se obtienen los posibles movimientos desde la celda <x>
    Entonces deberia tener <n> posibles de movimiento
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

 Esquema del escenario: Cuando las bacterias se mueven aumenta en 1 su cantidad de movimientos
  Dado que hay 1 bacteria <tipo> con <mov> movimientos en <pos>
  Cuando se mueve 1 bacteria <tipo> de la celda <pos> a <end>
  Entonces deberia haber 1 bacteria <tipo> con <mov_act> movimientos en <end>

  Ejemplos:
     |tipo  |mov |pos   |end   |mov_act|
     |normal| 0  |(5,0) |(5,1) |1      |
     |debil | 4  |(1,2) |(2,3) |5      |
     |fuerte| 2  |(2,3) |(2,4) |3      |
     |normal| 1  |(5,0) |(5,1) |2      |
     |debil | 3  |(1,2) |(2,3) |4      |
     |fuerte| 0  |(2,3) |(2,4) |1      |

 Esquema del escenario: El grado de infeccion aumenta con los movimientos
   Dado que hay 1 bacteria infectada en la celda <pos> con grado de infeccion <grado>
   Cuando se mueve 1 bacteria infectada de la celda <pos> a <end>
   Entonces deberia haber 1 bacteria infectada de grado <grado_act> en <end>

  #  Y deberia tener un <cualidad> de infeccion de <poder>]

   Ejemplos:
     |pos   |end   |grado  |grado_act|
     |(5,0) |(5,1) |1      |2        |
     |(1,2) |(2,3) |2      |3        |
     |(2,3) |(2,4) |3      |4        |


 Esquema del escenario: El poder de infeccion disminuye con los movimientos
   Dado que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
   Cuando se mueve 1 bacteriofago de la celda <pos> a <end>
   Entonces deberia haber 1 bacteriofago con poder de infeccion <poder_act> en <end> 


   Ejemplos:
     |pos   |end   |poder  |poder_act|
     |(5,0) |(5,1) |4      |3        |
     |(1,2) |(2,3) |2      |1        |
     |(5,0) |(5,1) |3      |2        |
