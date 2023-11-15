from enum import Enum

class Game_State(Enum):
    NOT_STARTED = 1  # Todavia no empezo el juego
    CONFIG_GAME = 2  # CONFIGURA LOS PARAMETROS
    START_GAME = 3  # Inicio de juego