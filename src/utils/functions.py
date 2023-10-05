import os
from .consts import ACTIONS


# The `Utils` class provides static methods for cleaning the console, printing a menu, and getting an
# action based on an option.
class Utils:
    """
    The function `clean_console` clears the console screen in Python, using different commands depending
    on the operating system.
    """

    @staticmethod
    def clean_console():
        OS = os.name

        # Linux and macOS
        if OS == "posix":
            os.system("clear")

        # Windows
        elif OS == "nt":
            os.system("cls")

    """
        The function `print_menu()` prints a menu with options for adding a new song, viewing the songs in
        the playlist, checking the playlist's status, or exiting the program.
    """

    @staticmethod
    def print_menu():
        print(
            """
Elige qué quieres hacer:
(1). Agregar nueva canción.
(2). Ver canciones de la playlist.
(3). Ver estado de la playlist.
(4). Salir.
"""
        )

    """
        The `get_action` function returns the action associated with a given option.
        
        @param option A string representing the option for which we want to get the corresponding action.
        
        @return The value associated with the given option in the ACTIONS dictionary.
    """

    @staticmethod
    def get_action(option: str):
        return ACTIONS.get(option)
