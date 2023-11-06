import socket
from socket import socket as Socket
import threading
import json
import csv
import time
from models.playlist import Playlist
from models.song import Song
from utils.consts import PLAYLIST_FILE


class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lock = threading.Lock()

    """
        The `client_handler` function receives requests from a client socket, processes them, and sends back
        appropriate responses.

        @param client_socket The `client_socket` parameter is a Socket object that represents the connection
        between the server and the client. It is used to send and receive data between the two.

        @return None
    """

    def client_handler(self, client_socket: Socket):
        while True:
            request = client_socket.recv(1024).decode()

            if not request:
                break

            if request.startswith("add"):
                song: dict[Song] = json.loads(request.split(" ", 1)[1])

                with self.lock:
                    current_songs = Playlist.get_songs()
                    exists = Playlist.check_existing_songs(song["title"], current_songs)

                    if exists:
                        client_socket.send(
                            f"** La canción '{song['title']}' ya está en la lista de reproducción **".encode()
                        )
                        return

                    row = list(song.values())

                    with open(PLAYLIST_FILE, mode="a", newline="") as file:
                        print("Agregando canción...")
                        time.sleep(5)
                        writer = csv.writer(file)
                        writer.writerow(row)

                    print(f"'{song['title']}' agregada a la lista correctamente.")
                    client_socket.send(
                        "** Canción agregada a la lista correctamente **".encode()
                    )

            elif request == "read":
                songs = Playlist.get_songs()
                client_socket.send(json.dumps(songs).encode())

        client_socket.close()


server = Server()
server.socket.bind(("localhost", 8888))
server.socket.listen(5)

while True:
    client_socket, addr = server.socket.accept()
    client_thread = threading.Thread(
        target=server.client_handler, args=(client_socket,)
    )
    client_thread.start()
