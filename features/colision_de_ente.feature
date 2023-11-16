# language: es

Característica: Colisión de entidades

# Bacterias y antibioticos
  Esquema del escenario: Una bacteria (debil o normal) y un antibiotico colisionan
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (20,20,20,20,antibiotico)
    Y que hay 1 antibiotico en la celda <crash> con poder <poder>
    Y que hay 1 bacteria <tipo> en la celda <crash>
    Cuando se produce la confrontacion
    Entonces deberia haber 1 antibiotico de poder <poder_act> en <crash>
    Y el tablero no deberia tener bacteria <tipo> en <crash>
    Ejemplos:
    |tipo  |crash| poder | poder_act |
    |debil |(2,3)|   4   |     3     |
    |debil |(1,4)|   3   |     2     |
    |debil |(2,3)|   2   |     1     |
    |normal|(1,4)|   5   |     4     | 
    |normal|(2,3)|   3   |     2     |
    |normal|(1,4)|   2   |     1     |  
                       
   Esquema del escenario: Una bacteria fuerte se debilita al tener contacto con un antibiotico
     Dado que el usuario abrio el juego
     Y se creo el juego con los siguientes parametros (20,20,20,20,antibiotico)
     Y que hay 1 antibiotico en la celda <pos> con poder <poder>
     Y que hay 1 bacteria fuerte en la celda <pos>
     Cuando se produce la confrontacion
     Entonces deberia haber 1 antibiotico de poder <poder_act> en <pos>
     Y el tablero deberia tener 1 bacteria debil en <pos>
     Ejemplos:
      |pos  |poder|poder_act|
      |(1,0)|  2  |   1     |
      |(3,3)|  3  |   2     |
      |(4,5)|  4  |   3     |
      |(0,2)|  5  |   4     |
      |(3,1)|  6  |   5     |

   Esquema del escenario: Las bacterias mueren cuando hay mas antibioticos que bacterias en la misma celda
     Dado que el usuario abrio el juego
     Y se creo el juego con los siguientes parametros (20,20,20,20,antibiotico)
     Y que hay 4 antibiotico en la celda <pos> con poder <poder>
     Y que hay 1 bacteria normal en la celda <pos>
     Y que hay 1 bacteria debil en la celda <pos>
     Y que hay 1 bacteria fuerte en la celda <pos>
     Cuando se produce la confrontacion
     Entonces deberia haber 4 antibiotico de poder <poder_act> en <pos>
     Y el tablero no deberia tener bacterias en <pos>
     Ejemplos:
     |pos  |poder|poder_act|
     |(3,1)|  4  |    3    |
     |(2,3)|  3  |    2    | 
     |(4,2)|  2  |    1    |



# Bacterias y bacteriófagos
  Esquema del escenario: Una bacteria se cruza con un bacteriofago
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (20,20,20,20,bacteriofago)
    Y se configuro los parametros avanzados con (3,3,3,<mov_explosion>,4,4,0.1,4)
    Y que hay 1 bacteria <tipo> en la celda <crash>
    Y que hay 1 bacteriofago en la celda <crash> con poder de infeccion <poder>
    Cuando se produce la confrontacion
    Entonces  deberia haber 1 bacteria infectada de grado <grado> en <crash>
    Y el tablero no deberia tener bacteriofagos en <crash>

    Ejemplos:
    |crash  |mov_explosion  |poder|grado|tipo  |
    |(3,3)  |     4         |3    |3    |normal|
    |(1,3)  |     5         |4    |4    |normal|
    |(0,1)  |     6         |2    |2    |normal|
    |(5,2)  |     8         |3    |3    |fuerte|
    |(5,4)  |     10        |7    |7    |fuerte|

   Esquema del escenario: Una bacteria infectada no le ocurre nada cuando se cruza con un bacteriófago
     Dado que el usuario abrio el juego
     Y se creo el juego con los siguientes parametros (20,20,20,20,bacteriofago)
     Y se configuro los parametros avanzados con (3,3,3,8,4,8,0.1,4)
     Y que hay 1 bacteria infectada en la celda <pos> con grado de infeccion <grado>
     Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
     Cuando se produce la confrontacion
     Entonces deberia haber 1 bacteria infectada de grado <grado> en <pos>
     Y deberia haber 1 bacteriofago con poder de infeccion <poder> en <pos>
     Ejemplos:
     |pos   |poder|grado|
     |(3,3) |6    |1    |
     |(1,1) |4    |3    |
     |(2,4) |4    |3    |
     |(3,3) |3    |1    |
     |(1,1) |1    |1    |
     |(2,4) |1    |5    |

  Esquema del escenario: Una bacteria es infectada por dos bacteriófagos y sobrevive al encuentro
     Dado que el usuario abrio el juego
     Y se creo el juego con los siguientes parametros (20,20,20,20,bacteriofago)
     Y se configuro los parametros avanzados con (3,3,3,<mov_explosion>,4,8,0.1,4)
     Y que hay 1 bacteria <tipo> en la celda <pos>
     Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
     Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder2>
     Cuando se produce la confrontacion
     Entonces deberia haber 1 bacteria infectada de grado <grado> en <pos>
     Ejemplos:
     |pos    |mov_explosion  |poder|poder2|grado|tipo  |
     |(3,3)  |       4       |1    |2     |3    |normal|
     |(3,4)  |       4       |1    |1     |2    |fuerte|
     |(1,4)  |       6       |3    |2     |5    |normal|
     |(3,4)  |       7       |2    |4     |6    |fuerte|
     |(5,5)  |       8       |4    |3     |7    |normal|

  Esquema del escenario: Una bacteria es infectada por dos bacteriófagos y explota
     Dado que el usuario abrio el juego
     Y se creo el juego con los siguientes parametros (20,20,20,20,bacteriofago)
     Y se configuro los parametros avanzados con (3,3,3,<mov_explosion>,<virus_pos_expl>,<poder_infec_ini>,0.1,4)
     Y que hay 1 bacteria <tipo> en la celda <pos>
     Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
     Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder2>
     Cuando se produce la confrontacion
     Entonces deberia haber <virus_pos_expl> bacteriofago con poder de infeccion <poder_infec_ini> en <pos>
     Ejemplos:
     |pos    |mov_explosion  |virus_pos_expl|poder_infec_ini  |poder|poder2|tipo  |
     |(3,3)  |      4        |      4       |      4          |3    |2     |normal|
     |(3,4)  |      4        |      8       |      2          |2    |2     |fuerte|
     |(1,4)  |      6        |      6       |      4          |4    |4     |normal|
     |(3,4)  |      8        |      3       |      3          |5    |3     |fuerte|

  Esquema del escenario: Sobrepoblación de bacterias se cruzan con un bacteriofago
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (20,20,20,20,bacteriofago)
    Y se configuro los parametros avanzados con (3,3,3,4,4,4,0.1,<cant_sobrepoblacion>)
    Y que hay <cant_sobrepoblacion> bacteria <tipo> en la celda <pos>
    Y que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
    Cuando se produce la confrontacion
    Entonces deberia haber 1 bacteria infectada de grado <grado> en <pos>
    Ejemplos:
    |pos  |cant_sobrepoblacion|poder|grado|tipo  |
    |(3,3)|         2         |3    |3    |normal|
    |(0,0)|         4         |3    |3    |fuerte|
    |(1,4)|         6         |2    |2    |normal|
    |(4,1)|         7         |1    |1    |fuerte|
    |(5,5)|         8         |1    |1    |normal|


  Esquema del escenario: Sobrepoblación con bacterias del mismo tipo
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (20,20,20,20,<modo>)
    Y se configuro los parametros avanzados con (3,3,3,4,4,4,0.1,<cant_sobrepoblacion>)
    Y que hay <cant_sobrepoblacion> bacteria <tipo> en la celda <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 1 bacteria <tipo> en <pos>

    Ejemplos:
    |pos  |modo        |cant_sobrepoblacion|tipo     |
    |(3,3)|antibiotico |         4         |fuerte   |
    |(0,0)|antibiotico |         4         |normal   |
    |(1,4)|antibiotico |         6         |debil    |
    |(4,1)|bacteriofago|         7         |fuerte   |
    |(5,5)|bacteriofago|         8         |normal   |
    |(2,2)|bacteriofago|         8         |infectada|

  Esquema del escenario: Sobrepoblación de bacterias fuerte  y normales
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (20,20,20,20,antibiotico)
    Y se configuro los parametros avanzados con (3,3,3,4,4,4,0.1,<cant_sobrepoblacion>)
    Y que hay <cant_normales> bacteria normal en la celda <pos>
    Y que hay <cant_fuertes> bacteria fuerte en la celda <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 1 bacteria en <pos>

    Ejemplos:
    |pos  |cant_sobrepoblacion|cant_normales|cant_fuertes|
    |(3,3)|         4         |2            |2           |
    |(0,0)|         4         |4            |3           |
    |(1,4)|         6         |3            |3           |
    |(4,1)|         7         |5            |5           |
    |(5,5)|         8         |4            |4           |

  Esquema del escenario: Sobrepoblación de bacterias fuerte/normales con bacterias debiles/infectadas
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (20,20,20,20,<modo>)
    Y se configuro los parametros avanzados con (3,3,3,4,4,4,0.1,<cant_sobrepoblacion>)
    Y que hay <cant_vencedor> bacteria <tipo_vencedor> en la celda <pos>
    Y que hay <cant_perdedor> bacteria <tipo_perdedor> en la celda <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 1 bacteria <tipo_vencedor> en <pos>

    Ejemplos:
    |pos  |modo        |cant_sobrepoblacion|cant_vencedor|cant_perdedor|tipo_vencedor|tipo_perdedor|
    |(3,3)|antibiotico |         4         |2            |2            |  normal     |  debil      |
    |(0,0)|bacteriofago|         4         |1            |3            |  normal     |  infectada  |
    |(1,4)|antibiotico |         6         |3            |3            |  fuerte     |  debil      |
    |(4,1)|bacteriofago|         7         |5            |5            |  fuerte     |  infectada  |
