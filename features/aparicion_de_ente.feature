# language: es

Característica: Sale una entidad de un spawn

  Esquema del escenario: Aparece un ente del spawn
    Dado que el usuario esta en el modo de juego de <modo>
    Y el usuario configura los parametros iniciales con ((<sx>,<sy>),<cant>,<frec>)
    Y el spawn esta en la posicion (<x1>,<y1>)
    Cuando el usuario da inicio al juego
    Entonces en la posicion (<x2>,<y2>) aparece 1 <entidad>
    
    Ejemplos:
      |modo         | x1 | y1 | x2 | y2 | sx | sy | cant | frec |entidad     |
      |antibioticos | 1  | 1  | 2  | 2  | 1  | 1  |  2   |  3   |bacteria    |
      |antibioticos | 1  | 1  | 2  | 2  | 1  | 1  |  2   |  3   |antibiotico |
      |bacteriofagos| 1  | 1  | 2  | 2  | 1  | 1  |  2   |  3   |bacteria    |
      |bacteriofagos| 1  | 1  | 2  | 2  | 1  | 1  |  2   |  3   |bacteriofago|

