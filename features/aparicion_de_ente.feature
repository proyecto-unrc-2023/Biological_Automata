# language: es

Característica: Sale una entidad de un spawn

  Esquema del escenario: Aparece un ente del spawn
    Dado el usuario ingreso al modo de juego de <modo>
    Cuando el usuario configura los parametros iniciales de <ente> con ((<x1>,<y1>),<cant>,<frec>)
    Y el usuario da inicio al juego, con un <ente> en (<x2>,<y2>)
    Entonces en la posicion (<x2>,<y2>) aparece 1 <entidad>
    
    Ejemplos:
      |modo         | x1 | y1 | x2 | y2 | cant | frec |entidad     | ente |
      |antibioticos | 1  | 1  | 2  | 2  |  2   |  3   |bacteria    |  b   |
      |antibioticos | 1  | 1  | 2  | 2  |  2   |  3   |antibiotico |  a   |
      |bacteriofagos| 1  | 1  | 2  | 2  |  2   |  3   |bacteria    |  b   |
      |bacteriofagos| 1  | 1  | 2  | 2  |  2   |  3   |bacteriofago|  v   |

