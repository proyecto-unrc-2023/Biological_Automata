# language: es

Característica: Se ubican los spawns de las entidades

  Esquema del escenario: Se ubica un spawn en el tablero
    Dado que el usuario ingreso al modo de juego de <modo>
    Cuando se crea un tablero de 6 x 6
    Y el usuario configura los parametros iniciales con ((<sx>,<sy>),<cant>,<frec>)
    Entonces en la celda (<p1>,<p2>) se encontrara el spawn de <entes>
    
    Ejemplos:
      |entes        |modo         | p1 | p2 | sx | sy | cant | frec |
      |bacterias    |antibioticos | 1  | 1  | 1  | 1  |  2   |  3   |
      |antibioticos |antibioticos | 1  | 1  | 1  | 1  |  2   |  3   |
      |bacterias    |bacteriofagos| 1  | 1  | 1  | 1  |  2   |  3   |
      |bacteriofagos|bacteriofagos| 1  | 1  | 1  | 1  |  2   |  3   |
   
