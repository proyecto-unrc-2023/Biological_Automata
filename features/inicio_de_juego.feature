# language: es

Característica: Se inicia el juego

  Esquema del escenario: Se configuran los parametros iniciales
    Dado que el usuario abrio el juego
    Cuando configura el juego con los siguientes parametros (<cant_bac>,<frec_bac>,<cant_o>,<frec_o>)
    Entonces se deberia crear un tablero de 30x50
    Y la cantidad de bacterias de inicio es <cant_bac>
    Y la frecuencia de bacterias es <frec_bac>
    Y la cantidad de la otra entidad de inicio es <cant_o>
    Y la frecuencia de la otra entidad es <frec_o>
    Y el estado de juego deberia ser CONFIG

    Ejemplos:

    |  cant_bac | frec_bac | cant_o | frec_o | 
    |    37     |     6    |   68   |   13   |
    |    79     |     4    |   15   |    5   |
    |    100    |     12   |   26   |    3   |
    |    26     |     8    |   43   |    4   |

  Esquema del escenario: Se posicionan los spawn
    Dado que el usuario abrio el juego
    Y los parametros iniciales del juego son (50,3,100,3)
    Cuando el usuario elige la posicion del spawn de bacterias en <pos_bac>
    Y el usuario elige la posicion del spawn de la otra entidad en <pos_other>
    Entonces deberia haber un spawn de bacterias en <pos_bac>
    Y deberia haber un spawn de la otra entidad en <pos_other>

    Ejemplos:

    |  pos_bac | pos_other | 
    |  (1,4)   |   (3,3)   |
    |  (5,8)   |   (5,16)  |
    |  (10,6)  |   (4,4)   |
    |  (16,16) |   (10,10) |


 Esquema del escenario: Se elige el modo de juego
  Dado que el usuario abrio el juego
  Y los parametros iniciales del juego son (50,3,100,3)
  Y se coloco el spawn de bacterias en (2,2)
  Y se coloco el spawn de la otra entidad en (5,5)
  Cuando el usuario elige el modo de juego <modo>
  Entonces el modo de juego deberia ser <modo>

  Ejemplos:

  |  modo          | 
  |  antibiotico   |
  |  bacteriofago  |

  Esquema del escenario: Se da inicio al juego
    Dado que el usuario abrio el juego
    Y los parametros iniciales del juego son (50,3,100,3)
    Y se coloco el spawn de bacterias en (2,2)
    Y se coloco el spawn de la otra entidad en (5,5)
    Y el modo de juego elegido es <modo>
    Cuando el usuario inicia el juego
    Entonces el estado de juego deberia ser STARTED

    Ejemplos:

  |  modo          | 
  |  antibiotico   |
  |  bacteriofago  |
