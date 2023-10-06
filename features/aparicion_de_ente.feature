# language: es

Característica: Sale una entidad de un spawn

  Esquema del escenario: Aparece un ente del spawn
    Dado el usuario ingreso al modo de juego de <modo>
    Y el usuario configura los parametros iniciales de <ente> con ((<x1>,<y1>),<cant>,<frec>)
    Cuando ha pasado 1 turno para la generacion de entidades
    Entonces deberian quedar <cant_act> <ente> por salir del spawn
    
    Ejemplos:
      |modo         | x1 | y1 | x2 | y2 | cant | frec | ente |cant_act |
      |antibioticos | 1  | 1  | 2  | 2  |  8   |  3   |  b   |7        |
      |antibioticos | 1  | 1  | 2  | 2  |  15  |  10  |  a   |14       |
      |bacteriofagos| 1  | 1  | 2  | 2  |  7   |  6   |  b   |6        |
      |bacteriofagos| 1  | 1  | 2  | 2  |  10  |  5   |  v   |9        |

  Esquema del escenario: Aparecen varios entes después de varios turnos
    Dado el usuario ingreso al modo de juego de <modo>
    Y el usuario configura los parametros iniciales de <ente> con ((<x1>,<y1>),<cant>,<frec>)
    Cuando ha pasado <turnos> turno para la generacion de entidades
    Entonces deberian quedar <cant_act> <ente> por salir del spawn
    
    Ejemplos:
      |modo         | x1 | y1 | cant  | frec | ente |turnos  |cant_act  |
      |antibioticos | 1  | 1  |  25   |  3   |  b   |9       |22        |
      |antibioticos | 1  | 1  |  14   |  3   |  a   |125     |0         |
      |bacteriofagos| 1  | 1  |  90   |  1   |  b   |90      |0         |
      |bacteriofagos| 1  | 1  |  17   |  2   |  v   |6       |14        |


  Esquema del escenario: Aparecen entes de cada uno de los spawn después de varios turnos
    Dado el usuario ingreso al modo de juego de <modo>
    Y el usuario configura los parametros iniciales de b con ((<x1>,<y1>),<cantb>,<frecb>)
    Y el usuario configura los parametros iniciales de <otro> con ((<x2>,<y2>),<cant_otro>,<frec_o>)
    Cuando ha pasado <turnos> turno de juego
    Entonces deberian quedar <cantb_act> b por salir del spawn
    Y deberian quedar <cant_o_act> <otro> por salir del spawn
    
    Ejemplos:
      |modo         | x1 | y1 | x2 | y2 | cantb | frecb |cant_otro |frec_o| otro |turnos  |cantb_act |cant_o_act|
      |antibioticos | 1  | 1  | 2  | 2  |  25   |  3    |   14     |  2   |   a  |  9     |    22    |    9     |
      |antibioticos | 1  | 1  | 2  | 2  |  14   |  3    |   76     |  5   |   a  |  125   |    0     |    51    |
      |bacteriofagos| 1  | 1  | 2  | 2  |  90   |  1    |   120    |  4   |   v  |  90    |    0     |    97    |
      |bacteriofagos| 1  | 1  | 2  | 2  |  17   |  2    |   81     |  7   |   v  |  6     |    14    |    80    |