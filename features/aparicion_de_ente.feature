# language: es

Característica: Sale una entidad de un spawn

  Esquema del escenario: Aparece un ente al lado del spawn después del primer turno
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (<cantb>,<frecb>,<cant_otro>,<frec_o>,<modo>)
    Y se coloco el spawn de bacterias en (<x1>,<y1>)
    Y se coloco el spawn de la otra entidad en (<x2>,<y2>)
    Y el usuario inicio el juego
    Cuando ha pasado 1 turno de juego
    Entonces deberian quedar <cantb_act> bacterias por salir del spawn
    Y deberian quedar <cant_o_act> <modo> por salir del spawn
    Y deberia haber 1 bacteria en las celdas adyacentes a (<x1>,<y1>)
    Y deberia haber 1 <modo> en las celdas adyacentes a (<x2>,<y2>)

    Ejemplos:
      |modo        | x1 | y1 | x2 | y2 | cantb | frecb |cant_otro |frec_o|cantb_act |cant_o_act|
      |antibiotico | 1  | 1  | 4  | 4  |  25   |  3    |   14     |  2   |    24    |    13    |
      |antibiotico | 1  | 1  | 4  | 4  |  14   |  3    |   76     |  5   |    13    |    75    |
      |bacteriofago| 1  | 1  | 4  | 4  |  90   |  1    |   120    |  4   |    89    |    119   |
      |bacteriofago| 1  | 1  | 4  | 4  |  17   |  2    |   81     |  7   |    16    |    80    |

  Esquema del escenario: Aparecen entes de cada uno de los spawn después de varios turnos
    Dado que el usuario abrio el juego
    Y se creo el juego con los siguientes parametros (<cantb>,<frecb>,<cant_otro>,<frec_o>,<modo>)
    Y se coloco el spawn de bacterias en (<x1>,<y1>)
    Y se coloco el spawn de la otra entidad en (<x2>,<y2>)
    Y el usuario inicio el juego
    Cuando ha pasado <turnos> turno de juego
    Entonces deberian quedar <cantb_act> bacterias por salir del spawn
    Y deberian quedar <cant_o_act> <modo> por salir del spawn
    
    Ejemplos:
      |modo        | x1 | y1 | x2 | y2 | cantb | frecb |cant_otro |frec_o|turnos  |cantb_act |cant_o_act|
      |antibiotico | 1  | 1  | 2  | 2  |  25   |  3    |   14     |  2   |  9     |    22    |    9     |
      |antibiotico | 1  | 1  | 2  | 2  |  14   |  10   |   76     |  5   |  125   |    1     |    51    |
      |bacteriofago| 1  | 1  | 2  | 2  |  90   |  1    |   120    |  4   |  90    |    0     |    97    |
      |bacteriofago| 1  | 1  | 2  | 2  |  17   |  2    |   81     |  7   |  6     |    14    |    80    |