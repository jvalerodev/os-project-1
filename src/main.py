from models.song import Song
from models.playlist import Playlist
from utils.functions import Utils
from utils.consts import HEADERS

print("--- Reproductor de Música ---")

while True:
    Utils.print_menu()
    option = Utils.get_action(input("-Opción: "))

    if not option:
        Utils.clean_console()
        print("** Opción inválida **")

    elif option == "add":
        Utils.clean_console()
        print("** Proporciona los detalles de la canción **\n")

        song = Song()
        Utils.clean_console()

        Playlist.add_song(song)

    elif option == "read":
        Utils.clean_console()
        songs = Playlist.get_songs()

        if len(songs) == 0:
            print("** La lista de reproducción está vacía **\n")
            continue

        print("** Canciones de la lista de reproducción **\n")
        print(", ".join(HEADERS))

        for song in songs:
            print(", ".join(song))

    elif option == "exit":
        break