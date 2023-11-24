# language: es

Característica: Movimientos de una entidad

 Esquema del escenario: Cuando las bacterias se mueven aumenta en 1 su cantidad de movimientos
  Dado se creo el juego con los siguientes parametros (20,20,20,20,<modo>) 
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
   Dado se creo el juego con los siguientes parametros (20,20,20,20,bacteriofago)  
   Y que hay 1 bacteria infectada en la celda <pos> con grado de infeccion <grado>
   Cuando se mueve 1 bacteria infectada de la celda <pos> a <end>
   Entonces deberia haber 1 bacteria infectada de grado <grado_act> en <end>

   Ejemplos:
     |pos   |end   |grado  |grado_act|
     |(5,0) |(5,1) |1      |2        |
     |(1,2) |(2,3) |2      |3        |
     |(2,3) |(2,4) |3      |4        |


 Esquema del escenario: El poder de infeccion disminuye con los movimientos
   Dado se creo el juego con los siguientes parametros (20,20,20,20,bacteriofago) 
   Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
   Cuando se mueve 1 bacteriofago de la celda <pos> a <end>
   Entonces deberia haber 1 bacteriofago con poder de infeccion <poder_act> en <end> 

   Ejemplos:
     |pos   |end   |poder  |poder_act|
     |(5,0) |(5,1) |4      |3        |
     |(1,2) |(2,3) |2      |1        |
     |(5,0) |(5,1) |3      |2        |
