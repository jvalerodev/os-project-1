import os
import csv
import time
from .song import Song
from utils.consts import PLAYLIST_FILE, LOCK_FILE


class Playlist:
    @staticmethod
    def add_song(song: Song):
        while Playlist.is_locked():
            print("** Otra usuario está guardando una canción. Esperando... **")
            time.sleep(1)

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
                time.sleep(5)

            Playlist.release_write_lock()
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

    @staticmethod
    def is_locked():
        if not os.path.exists(LOCK_FILE):
            open(LOCK_FILE, mode="w").close()
            return False

        return True

    @staticmethod
    def release_write_lock():
        if os.path.exists(LOCK_FILE):
            os.remove(LOCK_FILE)
