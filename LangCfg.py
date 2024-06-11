from enum import Enum

class LangCfg(Enum):
    SPANISH = "Bienvenido al juego, presiona t para comenzar\npresiona c para ir a la configuración\njugador rojo mueve con i,k\njugador azul mueve con w,s\npresiona espacio para pausar"
    ENGLISH = "Welcome to the game, press t to start\npress c for configure\nred player moves with i,k\nblue player moves with w,s\npress spacebar to pause"
    FRENCH ="Bienvenu a ce jeux, presser t pour commencer\npresser c pour aller a la configuration\njoueur rouge bouges avec i,k\njoueur bleu bouges ave w,s\npresser space pour pause"
    español = ["Bienvenido al menu de configuracion", "idioma", ["español","ingles", "frances"] , "velocidad", "rebote", "guardar"]
    english =["Welcome to the settings menu", "language", ["spanish","english","french"],"speed", "bounce", "save"]
    français =["Bienvenu ou menu de configuration", "language", ["espagnol", "angalis","français"], "vitesse", "rebond", "sauver"]