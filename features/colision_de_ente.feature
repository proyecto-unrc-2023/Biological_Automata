# language: es

Característica: Colisión de entidades

# Bacterias y antibioticos
  Esquema del escenario: Cuando un antibitico y una bacteria (debil o normal) colisionan, ambos desaparecen
    Dado que hay 1 antibiotico en la celda <crash>
    Y que hay 1 bacteria <tipo> en la celda <crash>
    Cuando se produce la confrontacion
    Entonces el tablero no deberia tener antibioticos en <crash>
    Y el tablero no deberia tener bacteria <tipo> en <crash>
    Ejemplos:
    |tipo  |crash|
    |debil |(2,3)|
    |normal|(1,4)|

   Esquema del escenario: Una bacteria fuerte se debilita al tener contacto con un antibiotico
     Dado que hay 1 antibiotico en la celda <pos>
     Y que hay 1 bacteria fuerte en la celda <pos>
     Cuando se produce la confrontacion
     Entonces el tablero no deberia tener antibioticos en <pos>
     Y el tablero deberia tener 1 bacteria debil en <pos>
     Ejemplos:
      |pos  |
      |(3,2)|
      |(1,0)|
      |(3,3)|
      |(4,5)|
      |(0,2)|
      |(3,1)|

   Esquema del escenario: Las bacterias mueren cuando hay mas antibioticos que bacterias en la misma celda
     Dado que hay 4 antibiotico en la celda <pos>
     Y que hay 1 bacteria normal en la celda <pos>
     Y que hay 1 bacteria debil en la celda <pos>
     Y que hay 1 bacteria fuerte en la celda <pos>
     Cuando se produce la confrontacion
     Entonces el tablero no deberia tener antibioticos en <pos>
     Y el tablero no deberia tener bacterias en <pos>
     Ejemplos:
     |pos  |
     |(3,1)|
     |(2,3)|
     |(4,2)|



# Bacterias y bacteriófagos
  Esquema del escenario: Una bacteria se cruza con un bacteriofago
    Dado que hay 1 bacteria <tipo> en la celda <crash>
    Y que hay 1 bacteriofago en la celda <crash> con poder de infeccion <poder>
    Cuando se produce la confrontacion
    Entonces  deberia haber 1 bacteria infectada de grado <grado> en <crash>
    Y el tablero no deberia tener bacteriofagos en <crash>

    Ejemplos:
    |crash  |poder|grado|tipo  |
    |(3,3)  |3    |3    |normal|
    |(1,3)  |2    |2    |normal|
    |(0,1)  |1    |1    |normal|
    |(5,2)  |3    |3    |fuerte|

   Esquema del escenario: Una bacteria infectada no le ocurre nada cuando se cruza con un bacteriófago
     Dado que hay 1 bacteria infectada en la celda <pos> con grado de infeccion <grado>
     Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
     Cuando se produce la confrontacion
     Entonces deberia haber 1 bacteria infectada de grado <grado> en <pos>
     Y deberia haber 1 bacteriofago con poder de infeccion <poder> en <pos>
     Ejemplos:
     |pos  |poder|grado|
     |(3,3)|4    |1    |
     |(1,1)|3    |2    |
     |(2,4)|2    |2    |

  Esquema del escenario: Una bacteria es infectada por dos bacteriófagos y sobrevive al encuentro
     Dado que hay 1 bacteria <tipo> en la celda <pos>
     Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
     Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder2>
     Cuando se produce la confrontacion
     Entonces deberia haber 1 bacteria infectada de grado <grado> en <pos>
     Ejemplos:
     |pos    |poder|poder2|grado|tipo  |
     |(3,3)  |1    |2     |3    |normal|
     |(3,4)  |1    |1     |2    |fuerte|
     |(1,4)  |2    |1     |3    |normal|
     |(3,4)  |1    |1     |2    |fuerte|

  Esquema del escenario: Una bacteria es infectada por dos bacteriófagos y explota
     Dado que hay 1 bacteria <tipo> en la celda <pos>
     Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
     Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder2>
     Cuando se produce la confrontacion
     Entonces deberia haber 4 bacteriofago con poder de infeccion 4 en <pos>
     Ejemplos:
     |pos    |poder|poder2|tipo  |
     |(3,3)  |2    |2     |normal|
     |(3,4)  |4    |1     |fuerte|
     |(1,4)  |3    |1     |normal|
     |(3,4)  |1    |3     |fuerte|

  Esquema del escenario: Sobrepoblación de bacterias se cruzan con un bacteriofago
    Dado que hay 4 bacteria <tipo> en la celda <pos>
    Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
    Cuando se produce la confrontacion
    Entonces deberia haber 1 bacteria infectada de grado <grado> en <pos>
    Ejemplos:
    |pos  |poder|grado|tipo  |
    |(3,3)|3    |3    |normal|
    |(1,4)|2    |2    |fuerte|
    |(4,1)|1    |1    |normal|
