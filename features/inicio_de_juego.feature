# language: es

Característica: Se inicia el juego

  Esquema del escenario: Se configuran los parametros iniciales
    Dado que el usuario abrio el juego
    Cuando se crea el juego con los siguientes parametros (<cant_bac>,<frec_bac>,<cant_o>,<frec_o>,<modo>)
    Entonces se deberia crear un tablero de 12x17
    Y la cantidad de bacterias de inicio es <cant_bac>
    Y la frecuencia de bacterias es <frec_bac>
    Y la cantidad de <modo> de inicio es <cant_o>
    Y la frecuencia de <modo> es <frec_o>
    Y el estado de juego deberia ser CONFIG
    Y el modo de juego deberia ser <modo>

    Ejemplos:

    |  cant_bac | frec_bac | cant_o | frec_o |   modo     |
    |    37     |     6    |   68   |   13   |antibiotico |
    |    79     |     4    |   15   |    5   |bacteriofago|
    |    100    |     12   |   26   |    3   |antibiotico |
    |    26     |     8    |   43   |    4   |bacteriofago|

  Esquema del escenario: Se posicionan los spawn
    Dado se creo el juego con los siguientes parametros (50,3,100,3,<modo>)
    Cuando el usuario elige la posicion del spawn de bacterias en <pos_bac>
    Y el usuario elige la posicion del spawn de la otra entidad en <pos_other>
    Entonces deberia haber un spawn de bacterias en <pos_bac>
    Y deberia haber un spawn de la otra entidad en <pos_other>
    Y el modo de juego deberia ser <modo>


    Ejemplos:
 
    |  pos_bac | pos_other | modo       | 
    |  (0,0)   |   (3,3)   |antibiotico |
    |  (5,15)  |   (5,16)  |bacteriofago|
    |  (0,16)  |   (4,14)  |antibiotico |
    |  (3,7)   |   (11,8)  |bacteriofago| 
    |  (11,4)  |   (0,0)   |antibiotico |
    |  (2,10)  |   (4,9)   |bacteriofago|
    |  (10,6)  |   (0,15)  |antibiotico |
    |  (9,15)  |   (0,0)   |bacteriofago|
    |  (3,16)  |   (11,16) |antibiotico |
    |  (4,8)   |   (5,16)  |bacteriofago|
    |  (10,6)  |   (3,0)   |antibiotico |
    |  (9,9)   |   (10,10) |bacteriofago|

  Esquema del escenario: Se da inicio al juego
    Dado se creo el juego con los siguientes parametros (50,3,100,3,<modo>)
    Y se coloco el spawn de bacterias en (2,2)
    Y se coloco el spawn de <modo> en (5,5)
    Cuando el usuario inicia el juego
    Entonces el estado de juego deberia ser STARTED
    Y el modo de juego deberia ser <modo>

    Ejemplos:

  |  modo          | 
  |  antibiotico   |
  |  bacteriofago  |