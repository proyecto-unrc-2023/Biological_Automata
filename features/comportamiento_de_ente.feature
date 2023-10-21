# language: es

Característica: Comportamiento de las entidades

  Esquema del escenario: Una bacteria normal o fuerte se reproduce
    Dado que hay 1 bacteria <tipo> con 3 movimientos en <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 2 bacterias en <pos>

    Ejemplos:

      |pos  |tipo  |
      |(1,2)|normal|
      |(5,3)|normal|
      |(5,3)|normal|
      |(1,2)|fuerte|
      |(5,0)|fuerte|
      |(2,1)|fuerte|

 Esquema del escenario: Una bacteria debil no se reproduce
    Dado que hay 1 bacteria debil con 5 movimientos en <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 1 bacteria debil en <pos>
    Ejemplos:
      |pos  |
      |(1,2)|
      |(4,4)|
      |(2,5)|
      |(0,3)|
      |(3,1)|

  Esquema del escenario: Bacterias debiles se recuperan
    Dado que hay 1 bacteria debil con 6 movimientos en <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 1 bacteria fuerte en <pos>

    Ejemplos:
      |pos   |
      |(5,0) |
      |(1,2) |
      |(0,4) |
      |(2,4) |
      |(1,0) |
      |(3,3) |

  Esquema del escenario: Una bacteria infectada explota generando bacteriofagos
    Dado que hay 1 bacteria infectada en la celda <pos> con grado de infeccion 4
    Cuando se produce la confrontacion
    Entonces deberia haber 4 bacteriofago con poder de infeccion 4 en <pos> 
    Ejemplos:
      |pos    |end   |
      |(4,0)  |(4,1) |
      |(2,0)  |(2,1) |
      |(3,3)  |(3,4) |

Esquema del escenario: Un bacteriofago desaparece tras cierto tiempo
    Dado que hay 1 bacteriofago en la celda <pos> con poder de infeccion 0
    Cuando se produce la confrontacion
    Entonces el tablero no deberia tener bacteriofago en <pos>

    Ejemplos:
      |pos   |
      |(5,0) |
      |(1,2) |
      |(3,0) |
      |(2,4) |
      |(0,3) |
      |(1,1) |
      |(1,0) |

Esquema del escenario: Las bacterias salen del spawn y luego se reproducen
    Dado que el usuario abrio el juego
    Y los parametros iniciales del juego son (1,20,0,3)
    Y se coloco el spawn de bacterias en (2,2)
    Y se coloco el spawn de la otra entidad en (5,5)
    Y el modo de juego elegido es <modo>
    Y el usuario inicio el juego
    Cuando ha pasado <turnos> turno de juego
    Entonces deberian quedar 0 bacterias por salir del spawn
    Y el tablero deberia quedar con <b_en_tablero> bacterias

    Ejemplos:

    |  modo          | turnos | b_en_tablero |
    |  antibiotico   |    2   |      1       |
    |  bacteriofago  |    2   |      1       |
    |  antibiotico   |    5   |      2       |
    |  bacteriofago  |    5   |      2       |
    |  antibiotico   |    7   |      4       |
    |  bacteriofago  |    7   |      4       |    

Esquema del escenario: Los bacteriofagos salen del spawn y desaparecen si no encuentran bacterias
    Dado que el usuario abrio el juego
    Y los parametros iniciales del juego son (0,10,<cant_v>,<frec_v>)
    Y se coloco el spawn de bacterias en (2,2)
    Y se coloco el spawn de la otra entidad en (5,5)
    Y el modo de juego elegido es bacteriofago
    Y el usuario inicio el juego
    Cuando ha pasado <turnos> turno de juego
    Entonces deberian quedar <cant_v_act> bacteriofagos por salir del spawn
    Y el tablero deberia quedar con <v_en_tablero> bacteriofagos

    Ejemplos:

      | cant_v | frec_v  |turnos  |cant_v_act |v_en_tablero|
      |  25    |  8      |  10    |    24     |    1       |
      |  25    |  8      |  40    |    20     |    1       |
      |  30    |  1      |  15    |    15     |    4       |
      |  17    |  2      |  70    |    0      |    0       |