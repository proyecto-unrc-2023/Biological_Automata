# language: es

Característica: Sale una entidad de un spawn

  #Esquema del escenario: Aparece un ente del spawn
  #    Dado el usuario ingreso al modo de juego de <modo>
  #    Cuando el usuario configura los parametros iniciales de <ente> con ((<x1>,<y1>),<cant>,<frec>)
  #    Y el usuario da inicio al juego, con un <ente> en (<x2>,<y2>)
  #    Entonces en la posicion (<x2>,<y2>) aparece 1 <entidad>
  #    
  #    Ejemplos:
  #      |modo         | x1 | y1 | x2 | y2 | cant | frec |entidad     | ente |
  #      |antibioticos | 1  | 1  | 2  | 2  |  2   |  3   |bacteria    |  b   |
  #      |antibioticos | 1  | 1  | 2  | 2  |  2   |  3   |antibiotico |  a   |
  #      |bacteriofagos| 1  | 1  | 2  | 2  |  2   |  3   |bacteria    |  b   |
  #      |bacteriofagos| 1  | 1  | 2  | 2  |  2   |  3   |bacteriofago|  v   |

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
      |modo         | x1 | y1 | x2 | y2 | cant  | frec | ente |turnos  |cant_act  |
      |antibioticos | 1  | 1  | 2  | 2  |  25   |  3   |  b   |9       |22        |
      |antibioticos | 1  | 1  | 2  | 2  |  14   |  3   |  a   |125     |0         |
      |bacteriofagos| 1  | 1  | 2  | 2  |  90   |  1   |  b   |90      |0         |
      |bacteriofagos| 1  | 1  | 2  | 2  |  17   |  2   |  v   |6       |14        |