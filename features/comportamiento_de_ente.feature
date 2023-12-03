# language: es

Característica: Comportamiento de las entidades

  Esquema del escenario: Una bacteria normal o fuerte se reproduce
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (1,20,0,3,<modo>)
    Y se configuro los parametros avanzados con (<mov_reproduccion>,3,3,3,3,3,0.1,4)
    Y que hay 1 bacteria <tipo> con <mov_reproduccion> movimientos en <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 2 bacterias en <pos>

    Ejemplos:

      |pos  |tipo  |  modo      |mov_reproduccion|
      |(1,2)|normal|antibiotico |        3       |
      |(5,3)|normal|bacteriofago|        6       |
      |(5,3)|normal|antibiotico |        24      |
      |(1,2)|fuerte|bacteriofago|        50      |
      |(5,0)|fuerte|antibiotico |        72      |
      |(2,1)|fuerte|bacteriofago|        41      |

  Esquema del escenario: Una bacteria normal se reproduce con un 0% de probabilidad de mutacion
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (1,20,0,3,<modo>)
    Y se configuro los parametros avanzados con (<mov_reproduccion>,3,3,3,3,3,0.0,4)
    Y que hay 1 bacteria <tipo> con <mov_reproduccion> movimientos en <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 2 bacteria <tipo> en <pos>

    Ejemplos:

      |pos  |tipo  |  modo      |mov_reproduccion|
      |(1,2)|normal|antibiotico |        3       |
      |(1,2)|fuerte|antibiotico |        3       |
      |(2,4)|normal|bacteriofago|        6       |
      |(2,4)|fuerte|bacteriofago|        6       |
      |(4,0)|normal|antibiotico |        20      | 
      |(4,0)|fuerte|antibiotico |        20      |   

  Esquema del escenario: Una bacteria normal se reproduce con un 100% de probabilidad de mutacion
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (1,20,0,3,<modo>)
    Y se configuro los parametros avanzados con (<mov_reproduccion>,3,3,3,3,3,1.0,4)
    Y que hay 1 bacteria <tipo> con <mov_reproduccion> movimientos en <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 1 bacteria <tipo> en <pos>
    Y el tablero deberia tener 1 bacteria <tipo_contrario> en <pos>

    Ejemplos:

      |pos  |tipo  |tipo_contrario|  modo      |mov_reproduccion|
      |(1,2)|normal|    fuerte    |antibiotico |        3       |
      |(2,4)|normal|    fuerte    |bacteriofago|        6       |
      |(5,3)|fuerte|    normal    |antibiotico |        14      |
      |(4,0)|fuerte|    normal    |bacteriofago|        20      |  


 Esquema del escenario: Una bacteria debil no se reproduce
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (1,20,0,3,antibiotico)
    Y se configuro los parametros avanzados con (<mov_reproduccion>,<mov_recuperacion>,3,3,3,3,0.1,4)
    Y que hay 1 bacteria debil con <cant_intermedia> movimientos en <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 1 bacteria debil en <pos>

    Ejemplos:
      |pos  |mov_reproduccion|mov_recuperacion|cant_intermedia|
      |(1,2)|     3          |      5         |      4        |
      |(4,4)|     7          |      14        |      10       |
      |(2,5)|     12         |      24        |      16       |
      |(0,3)|     17         |      45        |      32       |
      |(3,1)|     24         |      62        |      54       |

  Esquema del escenario: Bacterias debiles se recuperan
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (1,20,0,3,antibiotico)
    Y se configuro los parametros avanzados con (3,<mov_recuperacion>,3,3,3,3,0.1,4)
    Y que hay 1 bacteria debil con <mov_recuperacion> movimientos en <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 1 bacteria fuerte en <pos>

    Ejemplos:
      |pos   | mov_recuperacion |
      |(5,0) |        2         |      
      |(1,2) |        5         |    
      |(0,4) |        8         |     
      |(2,4) |        13        |
      |(1,0) |        17        |
      |(3,3) |        22        |

  Esquema del escenario: Una bacteria infectada explota generando bacteriofagos
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (1,20,0,3,bacteriofago)
    Y se configuro los parametros avanzados con (3,3,3,<grado_explosion>,<cant_explosion>,<poder_inf_ini>,0.1,4)
    Dado que hay 1 bacteria infectada en la celda <pos> con grado de infeccion <grado_explosion>
    Cuando se produce la confrontacion
    Entonces deberia haber <cant_explosion> bacteriofago con poder de infeccion <poder_inf_ini> en <pos> 
    
    Ejemplos:
      |pos   | grado_explosion | cant_explosion | poder_inf_ini   |
      |(4,0) |       4         |       4        |       4         |
      |(2,0) |       5         |       4        |       3         |
      |(3,3) |       8         |       6        |       2         |

  Esquema del escenario: Los bacteriofagos desaparecen cuando quedan con poder de infeccion 0
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (1,20,0,3,bacteriofago)
    Dado que hay <cant> bacteriofago en la celda <pos> con poder de infeccion 0
    Cuando se produce la confrontacion
    Entonces el tablero no deberia tener bacteriofago en <pos>

    Ejemplos:
      |pos   | cant |
      |(5,0) |  1   |
      |(1,2) |  2   |  
      |(3,0) |  3   |
      |(2,4) |  4   |
      |(0,3) |  5   |

  Esquema del escenario: Los antibioticos desaparecen cuando quedan con poder 0
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (1,20,0,3,antibiotico)
    Dado que hay <cant> antibiotico en la celda <pos> con poder 0
    Cuando se produce la confrontacion
    Entonces el tablero no deberia tener antibioticos en <pos>

    Ejemplos:
      |pos   | cant |
      |(5,0) |  1   |
      |(1,2) |  2   |  
      |(3,0) |  3   |
      |(2,4) |  4   |
      |(0,3) |  5   |

