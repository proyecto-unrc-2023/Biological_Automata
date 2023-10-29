# language: es

Característica: Movimientos de una entidad

  #Esquema del escenario: Un ente tiene una cantidad de movimientos permitidos determinados por su posicion
  #  Dado que el usuario abrio el juego
  #  Y los parametros iniciales del juego son (20,20,20,20,<modo>)
  #  Y que hay 1 <ente> en la celda <x>
  #  Cuando se obtienen los posibles movimientos desde la celda <x>
  #  Entonces deberia tener <n> posibles de movimiento

  #  Ejemplos:
  #    |ente              |x      |n    | modo       |
  #    |antibiotico       |(0,0)  |3    |antibiotico |
  #    |bacteriofago      |(0,49) |3    |bacteriofago|
  #    |bacteria normal   |(29,0) |3    |antibiotico |
  #    |bacteria debil    |(29,49)|3    |antibiotico |
  #    |bacteria fuerte   |(0,20) |5    |antibiotico |
  #    |bacteria infectada|(15,0) |5    |bacteriofago|
  #    |antibiotico       |(29,25)|5    |antibiotico |
  #    |bacteriofago      |(15,49)|5    |bacteriofago|
  #    |bacteria normal   |(10,20)|8    |bacteriofago|

  #Esquema del escenario: Un ente se mueve de posicion a una celda contigua
  #  Dado que el usuario abrio el juego
  #  Y los parametros iniciales del juego son (20,20,20,20,<modo>)
  #  Y que hay 1 <nombre> en la celda <x>
  #  Cuando un <ente> se mueve desde la celda <x> a una celda aleatoria
  #  Entonces la celda <x> del <ente> es contigua a la celda destino
    
  #  Ejemplos:
  #    |nombre            |x       |ente | modo       |
  #    |antibiotico       |(0,0)   |a    |antibiotico |
  #    |bacteriofago      |(15,0)  |v    |bacteriofago|
  #    |bacteria normal   |(10,20) |b    |bacteriofago|
  #    |bacteria debil    |(2,4)   |d    |antibiotico |
  #    |bacteria fuerte   |(10,20) |f    |antibiotico |
  #    |bacteria infectada|(15,0)  |i    |bacteriofago|

 Esquema del escenario: Cuando las bacterias se mueven aumenta en 1 su cantidad de movimientos
  Dado que el usuario abrio el juego
  Y los parametros iniciales del juego son (20,20,20,20,<modo>) 
  Y que hay 1 bacteria <tipo> con <mov> movimientos en <pos>
  Cuando se mueve 1 bacteria <tipo> de la celda <pos> a <end>
  Entonces deberia haber 1 bacteria <tipo> con <mov_act> movimientos en <end>

  Ejemplos:
     |tipo  |mov |pos   |end   |mov_act|   modo     |
     |normal| 0  |(5,0) |(5,1) |1      |antibiotico |
     |debil | 4  |(1,2) |(2,3) |5      |antibiotico |
     |fuerte| 2  |(2,3) |(2,4) |3      |antibiotico |
     |normal| 1  |(5,0) |(5,1) |2      |bacteriofago|
     |debil | 3  |(1,2) |(2,3) |4      |antibiotico |
     |fuerte| 0  |(2,3) |(2,4) |1      |bacteriofago|

 Esquema del escenario: El grado de infeccion aumenta con los movimientos
   Dado que el usuario abrio el juego
   Y los parametros iniciales del juego son (20,20,20,20,bacteriofago) 
   Y que hay 1 bacteria infectada en la celda <pos> con grado de infeccion <grado>
   Cuando se mueve 1 bacteria infectada de la celda <pos> a <end>
   Entonces deberia haber 1 bacteria infectada de grado <grado_act> en <end>

   Ejemplos:
     |pos   |end   |grado  |grado_act|
     |(5,0) |(5,1) |1      |2        |
     |(1,2) |(2,3) |2      |3        |
     |(2,3) |(2,4) |3      |4        |


 Esquema del escenario: El poder de infeccion disminuye con los movimientos
   Dado que el usuario abrio el juego
   Y los parametros iniciales del juego son (20,20,20,20,bacteriofago) 
   Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
   Cuando se mueve 1 bacteriofago de la celda <pos> a <end>
   Entonces deberia haber 1 bacteriofago con poder de infeccion <poder_act> en <end> 


   Ejemplos:
     |pos   |end   |poder  |poder_act|
     |(5,0) |(5,1) |4      |3        |
     |(1,2) |(2,3) |2      |1        |
     |(5,0) |(5,1) |3      |2        |
