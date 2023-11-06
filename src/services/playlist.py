import socket
import json
from models.song import Song


class PlaylistService:
    def add_song(song: Song):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 8888))
        request = f"add {json.dumps(song.__dict__)}"
        client_socket.send(request.encode())
        response = client_socket.recv(1024).decode()
        print(response)
        client_socket.close()

    def get_songs():
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 8888))
        request = "read"
        client_socket.send(request.encode())
        response = client_socket.recv(1024).decode()
        songs: list[str] = json.loads(response)
        client_socket.close()

        return songs
