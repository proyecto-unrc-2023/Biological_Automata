# language: es

Característica: El juego termina

  Esquema del escenario: El juego termina si el usuario detiene el juego
    Dado se creo el juego con los siguientes parametros (<cant_b>,20,<cant_otro>,3,<modo>)
    Y se coloco el spawn de bacterias en (0,0)
    Y se coloco el spawn de <modo> en (11,16)
    Y el usuario inicio el juego
    Y ha pasado <turnos> turno de juego
    Cuando el usuario detiene el juego
    Entonces el estado de juego deberia ser FINISHED
    Y el ganador deberia ser NO DETERMINADO

    Ejemplos:

    |    modo    |cant_b|cant_otro|turnos|
    |antibiotico |1     |1        |1     |
    |bacteriofago|1     |1        |1     |
    |antibiotico |24    |16       |10    |
    |bacteriofago|35    |23       |20    |
    |antibiotico |83    |72       |70    |
    |bacteriofago|96    |110      |100   |

  Esquema del escenario: Ganan las bacterias si no existe otro tipo de entidad en el juego
    Dado se creo el juego con los siguientes parametros (<cant>,20,0,3,<modo>)
    Y se coloco el spawn de bacterias en (0,0)
    Y se coloco el spawn de <modo> en (11,16)
    Y el usuario inicio el juego
    Cuando ha pasado 1 turno de juego
    Entonces el estado de juego deberia ser FINISHED
    Y el ganador deberia ser BACTERIA

    Ejemplos:

    |    modo    |cant|
    |antibiotico |1   |
    |bacteriofago|1   |
    |antibiotico |4   |
    |bacteriofago|5   |
    |antibiotico |13  |
    |bacteriofago|16  |

  Esquema del escenario: Ganan los bacteriofagos si no existen bacterias en el juego
    Dado se creo el juego con los siguientes parametros (0,10,<cant_v>,5,bacteriofago)
    Y se configuro los parametros avanzados con (3,3,3,4,4,<poder_infec_ini>,0.1,4)
    Y se coloco el spawn de bacterias en (2,2)
    Y se coloco el spawn de bacteriofago en (5,5)
    Y el usuario inicio el juego
    Cuando ha pasado 1 turno de juego
    Entonces el estado de juego deberia ser FINISHED
    Y el ganador deberia ser BACTERIOFAGO

    Ejemplos:

      | cant_v |poder_infec_ini|
      |  1     |       4       |
      |  25    |       6       |
      |  40    |       8       |
      |  80    |       10      |

  Esquema del escenario: Ganan los antibioticos si no existen bacterias en el juego
    Dado se creo el juego con los siguientes parametros (0,10,<cant_b>,5,antibiotico)
    Y se configuro los parametros avanzados con (3,3,<poder_antibiotico>,4,4,4,0.1,4)
    Y se coloco el spawn de bacterias en (2,2)
    Y se coloco el spawn de antibiotico en (5,5)
    Y el usuario inicio el juego
    Cuando ha pasado 1 turno de juego
    Entonces el estado de juego deberia ser FINISHED
    Y el ganador deberia ser ANTIBIOTICO

    Ejemplos:

      | cant_b |poder_antibiotico|
      |  25    |       3         |
      |  25    |       4         |
      |  40    |       5         |
      |  80    |       6         |
