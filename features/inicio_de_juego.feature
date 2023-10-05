# language: es

Característica: Se inicia el juego

  Esquema del escenario: Se crea el tablero inicial
    Dado el usuario ingreso al modo de juego de <modo>
    Cuando se da inicio al juego
    Entonces se deberia crear un tablero de 30 x 50
    Y el modo de juego deberia ser <modo>

    Ejemplos:
      |modo         |
      |antibioticos |
      |bacteriofagos|

  Esquema del escenario: Se configuran los parametros iniciales
    Dado el usuario ingreso al modo de juego de <modo>
    Cuando el usuario configura los parametros iniciales de <ente> con ((<sbx>,<sby>),<cant>,<frec>)
    Y el usuario configura los parametros iniciales de <otro> con ((<sox>,<soy>),<cant>,<frec>)
    Entonces el tablero resultante tendra <cant>,<frec>, para <ente> (<sbx>,<sby>)
    Y el tablero resultante tendra <cant>,<frec>, para <otro> (<sox>,<soy>)

    Ejemplos:
      |modo         | sbx | sby | sox | soy | cant | frec |ente |otro |
      |antibioticos | 1   | 1   | 2   | 1   |  2   |  3   |  b  |  a  |
      |bacteriofagos| 1   | 5   | 2   | 5   |  4   |  1   |  b  |  v  |