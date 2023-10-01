import os
from .consts import ACTIONS


class Utils:
    @staticmethod
    def clean_console():
        OS = os.name

        # Linux and macOS
        if OS == "posix":
            os.system("clear")

        # Windows
        elif OS == "nt":
            os.system("cls")

    @staticmethod
    def print_menu():
        print(
            """
Elige qué quieres hacer:
(1). Agregar nueva canción.
(2). Ver canciones de la playlist.
(3). Salir.
"""
        )

    @staticmethod
    def get_action(option: str):
        return ACTIONS.get(option)
