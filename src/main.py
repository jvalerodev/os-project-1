from models.song import Song
from services.playlist import PlaylistService
from utils.functions import Utils
from utils.consts import HEADERS


print("--- Reproductor de Música ---")

# The code is creating a loop that will continue running until the user chooses to exit. Inside the
# loop, it displays a menu using the `Utils.print_menu()` function and prompts the user for an option.
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
        PlaylistService.add_song(song)

    elif option == "read":
        Utils.clean_console()
        songs = PlaylistService.get_songs()

        if len(songs) == 0:
            print("** La lista de reproducción está vacía **\n")
            continue

        print("** Canciones de la lista de reproducción **\n")
        print(", ".join(HEADERS))

        for song in songs:
            print(", ".join(song))

    elif option == "read_state":
        Utils.clean_console()
        songs = PlaylistService.get_songs()

        if len(songs) == 0:
            print("** La lista de reproducción está vacía **\n")
            continue

        print("** Estado de la lista de reproducción **\n")
        print(f"- Total de canciones: {len(songs)}")
        print("- Últimas dos canciones agregadas: \n")
        print(", ".join(HEADERS))

        for song in songs[-2:]:
            print(", ".join(song))

    elif option == "exit":
        break
