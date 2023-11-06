import socket
import json
from models.song import Song


class PlaylistService:
    """
    The function `add_song` connects to a server, sends a request to add a song in JSON format,
    receives a response, and then closes the connection.

    @param song The parameter "song" is of type Song. It is expected to be an instance of the Song
    class, which likely has attributes such as title, artist, duration, etc.
    """

    def add_song(song: Song):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 8888))
        request = f"add {json.dumps(song.__dict__)}"
        client_socket.send(request.encode())
        response = client_socket.recv(1024).decode()
        print(response)
        client_socket.close()

    """
        The function `get_songs` connects to a server, sends a request to read songs, receives a
        response containing a list of songs, and returns the list of songs.

        @return a list of songs.
    """

    def get_songs():
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 8888))
        request = "read"
        client_socket.send(request.encode())
        response = client_socket.recv(1024).decode()
        songs: list[str] = json.loads(response)
        client_socket.close()

        return songs
