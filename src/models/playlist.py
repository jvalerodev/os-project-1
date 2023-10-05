import os
import csv
import time
from .song import Song
from utils.consts import PLAYLIST_FILE, LOCK_FILE


# The `Playlist` class provides methods to add songs to a playlist, check for existing songs, and
# manage a write lock to prevent concurrent writes.
class Playlist:
    """
    The `add_song` function adds a song to a playlist, checking for existing songs and handling file
    writing and locking.

    @param song The `song` parameter is an instance of the `Song` class. It represents a song that
    needs to be added to the playlist.

    @return None
    """

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

    """
        The `get_songs` function reads a CSV file containing songs and returns a list of songs.
        
        @return a list of songs.
    """

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

    """
        The `check_existing_songs` function checks if a given title exists in a list of songs.
        
        @param title A string representing the title of a song that we want to check if it exists in the
        list of songs.
        @param songs A list of lists where each inner list represents a song. Each inner list contains the
        title of the song as the first element and additional information about the song as subsequent
        elements.
        
        @return a boolean value. It returns True if there is a song in the list of songs that has the same
        title as the given title parameter, and False otherwise.
    """

    @staticmethod
    def check_existing_songs(title: str, songs: list[list[str]]):
        return any(song[0] == title for song in songs)

    """
        The `is_locked` function checks if another user is writing to the playlist file by checking if a
        lock file exists.
        
        @return The method is returning a boolean value. If the lock file does not exist, it creates the
        lock file and returns False.
    """

    @staticmethod
    def is_locked():
        if not os.path.exists(LOCK_FILE):
            open(LOCK_FILE, mode="w").close()
            return False

        return True

    """
        The `release_write_lock` function removes a lock file if it exists.
    """

    @staticmethod
    def release_write_lock():
        if os.path.exists(LOCK_FILE):
            os.remove(LOCK_FILE)
