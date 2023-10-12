# language: es

Característica: Sale una entidad de un spawn

  Esquema del escenario: Aparece un ente al lado del spawn después del primer turno
    Dado el usuario configura los parametros iniciales de b con ((<x1>,<y1>),<cantb>,<frecb>)
    Y el usuario configura los parametros iniciales de <otro> con ((<x2>,<y2>),<cant_otro>,<frec_o>)
    Y el usuario ingreso al modo de juego de <modo>
    Cuando ha pasado 1 turno de juego
    Entonces deberian quedar <cantb_act> b por salir del spawn
    Y deberian quedar <cant_o_act> <otro> por salir del spawn
    Y deberia haber 1 b en las celdas adyacentes a (<x1>,<y1>)
    Y deberia haber 1 <otro> en las celdas adyacentes a (<x2>,<y2>)

    Ejemplos:
      |modo         | x1 | y1 | x2 | y2 | cantb | frecb |cant_otro |frec_o| otro |cantb_act |cant_o_act|
      |antibioticos | 1  | 1  | 3  | 3  |  25   |  3    |   14     |  2   |   a  |    24    |    13    |
      |antibioticos | 1  | 1  | 3  | 3  |  14   |  3    |   76     |  5   |   a  |    13    |    75    |
      |bacteriofagos| 1  | 1  | 3  | 3  |  90   |  1    |   120    |  4   |   v  |    89    |    119   |
      |bacteriofagos| 1  | 1  | 3  | 3  |  17   |  2    |   81     |  7   |   v  |    16    |    80    |

  Esquema del escenario: Aparecen entes de cada uno de los spawn después de varios turnos
    Dado el usuario configura los parametros iniciales de b con ((<x1>,<y1>),<cantb>,<frecb>)
    Y el usuario configura los parametros iniciales de <otro> con ((<x2>,<y2>),<cant_otro>,<frec_o>)
    Y el usuario ingreso al modo de juego de <modo>
    Cuando ha pasado <turnos> turno de juego
    Entonces deberian quedar <cantb_act> b por salir del spawn
    Y deberian quedar <cant_o_act> <otro> por salir del spawn
    
    Ejemplos:
      |modo         | x1 | y1 | x2 | y2 | cantb | frecb |cant_otro |frec_o| otro |turnos  |cantb_act |cant_o_act|
      |antibioticos | 1  | 1  | 2  | 2  |  25   |  3    |   14     |  2   |   a  |  9     |    22    |    9     |
      |antibioticos | 1  | 1  | 2  | 2  |  14   |  3    |   76     |  5   |   a  |  125   |    0     |    51    |
      |bacteriofagos| 1  | 1  | 2  | 2  |  90   |  1    |   120    |  4   |   v  |  90    |    0     |    97    |
      |bacteriofagos| 1  | 1  | 2  | 2  |  17   |  2    |   81     |  7   |   v  |  6     |    14    |    80    |