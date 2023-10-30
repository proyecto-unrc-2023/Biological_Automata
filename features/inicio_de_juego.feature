# language: es

Característica: Se inicia el juego

  Esquema del escenario: Se configuran los parametros iniciales
    Dado que el usuario abrio el juego
    Cuando configura el juego con los siguientes parametros (<cant_bac>,<frec_bac>,<cant_o>,<frec_o>,<modo>)
    Entonces se deberia crear un tablero de 15x20
    Y la cantidad de bacterias de inicio es <cant_bac>
    Y la frecuencia de bacterias es <frec_bac>
    Y la cantidad de la otra entidad de inicio es <cant_o>
    Y la frecuencia de la otra entidad es <frec_o>
    Y el estado de juego deberia ser CONFIG
    Y el modo de juego deberia ser <modo>

    Ejemplos:

    |  cant_bac | frec_bac | cant_o | frec_o |   modo     |
    |    37     |     6    |   68   |   13   |antibiotico |
    |    79     |     4    |   15   |    5   |bacteriofago|
    |    100    |     12   |   26   |    3   |antibiotico |
    |    26     |     8    |   43   |    4   |bacteriofago|

  Esquema del escenario: Se posicionan los spawn
    Dado que el usuario abrio el juego
    Y los parametros iniciales del juego son (50,3,100,3,<modo>)
    Cuando el usuario elige la posicion del spawn de bacterias en <pos_bac>
    Y el usuario elige la posicion del spawn de la otra entidad en <pos_other>
    Entonces deberia haber un spawn de bacterias en <pos_bac>
    Y deberia haber un spawn de la otra entidad en <pos_other>
    Y el modo de juego deberia ser <modo>


    Ejemplos:
 
    |  pos_bac | pos_other | modo       | 
    |  (0,0)   |   (3,3)   |antibiotico |
    |  (5,19)  |   (5,16)  |bacteriofago|
    |  (0,17)  |   (4,14)  |antibiotico |
    |  (14,19) |   (11,18) |bacteriofago| 
    |  (13,4)  |   (0,0)   |antibiotico |
    |  (5,8)   |   (14,19) |bacteriofago|
    |  (10,6)  |   (0,19)  |antibiotico |
    |  (9,15)  |   (0,0)   |bacteriofago|
    |  (3,16)  |   (13,16) |antibiotico |
    |  (14,8)  |   (5,16)  |bacteriofago|
    |  (10,6)  |   (13,18) |antibiotico |
    |  (9,19)  |   (10,10) |bacteriofago|

  Esquema del escenario: Se da inicio al juego
    Dado que el usuario abrio el juego
    Y los parametros iniciales del juego son (50,3,100,3,<modo>)
    Y se coloco el spawn de bacterias en (2,2)
    Y se coloco el spawn de la otra entidad en (5,5)
    Cuando el usuario inicia el juego
    Entonces el estado de juego deberia ser STARTED
    Y el modo de juego deberia ser <modo>

    Ejemplos:

  |  modo          | 
  |  antibiotico   |
  |  bacteriofago  |
