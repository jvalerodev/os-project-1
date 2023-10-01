import csv
from .song import Song
from utils.consts import PLAYLIST_FILE


class Playlist:
    @staticmethod
    def add_song(song: Song):
        songs = Playlist.get_songs()
        exists = Playlist.check_existing_songs(song.title, songs)

        if exists:
            print(
                f"** La canción '{song.title}' ya está en la lista de reproducción **"
            )
            return

        row = list(song.__dict__.values())

        try:
            with open(PLAYLIST_FILE, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(row)

            print("** Canción agregada a la lista correctamente **")
        except Exception as error:
            print(error)

    @staticmethod
    def get_songs():
        try:
            with open(PLAYLIST_FILE, mode="r") as file:
                reader = csv.reader(file)
                next(reader)

                songs = [row for row in reader]
                return songs
        except Exception as error:
            print(error)

    @staticmethod
    def check_existing_songs(title: str, songs: list[list[str]]):
        return any(song[0] == title for song in songs)
