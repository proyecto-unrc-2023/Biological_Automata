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

  Esquema del escenario: Los bacteriofagos desaparecen cuando queda con poder de infeccion 0
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

  Esquema del escenario: Los antibioticos desaparecen cuando queda con poder 0
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


  Esquema del escenario: Las bacterias salen del spawn y luego se reproducen
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (1,20,0,3,<modo>)
    Y se configuro los parametros avanzados con (<mov_reproduccion>,3,3,4,4,4,0.1,4)
    Y se coloco el spawn de bacterias en (0,0)
    Y se coloco el spawn de la otra entidad en (11,16)
    Y el usuario inicio el juego
    Cuando ha pasado <turnos> turno de juego
    Entonces deberian quedar 0 bacterias por salir del spawn
    Y el tablero deberia quedar con <b_en_tablero> bacterias

    Ejemplos:

    |  modo          |mov_reproduccion|turnos | b_en_tablero |
    |  antibiotico   |        5       |   5   |      1       |
    |  bacteriofago  |        5       |   6   |      2       |
    |  antibiotico   |        5       |   11  |      4       |
    |  bacteriofago  |        9       |   10  |      2       |
    |  antibiotico   |        16      |   17  |      2       |
    |  bacteriofago  |        16      |   33  |      4       |    

  Esquema del escenario: Los bacteriofagos salen del spawn y desaparecen si no encuentran bacterias
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (0,10,<cant_v>,<frec_v>,bacteriofago)
    Y se configuro los parametros avanzados con (3,3,3,4,4,<poder_infec_ini>,0.1,4)
    Y se coloco el spawn de bacterias en (2,2)
    Y se coloco el spawn de la otra entidad en (5,5)
    Y el usuario inicio el juego
    Cuando ha pasado 1 turno de juego
    Entonces el estado de juego deberia ser FINISHED
    Y el ganador deberia ser la otra entidad
    #Entonces deberian quedar <cant_v_act> bacteriofagos por salir del spawn
    #Y el tablero deberia quedar con <v_en_tablero> bacteriofagos

    Ejemplos:

      | cant_v | frec_v  |poder_infec_ini  |turnos  |cant_v_act |v_en_tablero|
      |  25    |    4    |       4         |  10    |    22     |    1       |
      |  25    |    2    |       4         |  70    |    0      |    0       |
      |  40    |    1    |       6         |  15    |    25     |    6       |
      |  80    |    2    |       10        |  70    |    45     |    5       |

  Esquema del escenario: Los antibioticos salen del spawn y se mantienen en el tablero si no hay bacterias
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (0,10,<cant_b>,<frec_b>,antibiotico)
    Y se configuro los parametros avanzados con (3,3,<poder_antibiotico>,4,4,4,0.1,4)
    Y se coloco el spawn de bacterias en (2,2)
    Y se coloco el spawn de la otra entidad en (5,5)
    Y el usuario inicio el juego
    Cuando ha pasado 1 turno de juego
    Entonces el estado de juego deberia ser FINISHED
    Y el ganador deberia ser la otra entidad
    #Entonces deberian quedar <cant_b_act> antibioticos por salir del spawn
    #Y el tablero deberia quedar con <b_en_tablero> antibioticos con poder <poder_antibiotico>

    Ejemplos:

      | cant_b | frec_b  |poder_antibiotico|turnos  |cant_b_act |b_en_tablero|
      |  25    |    4    |       3         |  10    |    22     |    3       |
      |  25    |    2    |       4         |  70    |    0      |    25      |
      |  40    |    1    |       5         |  15    |    25     |    15      |
      |  80    |    2    |       6         |  70    |    45     |    35      |

