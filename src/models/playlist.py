import csv
from utils.consts import PLAYLIST_FILE


# The `Playlist` class provides methods to check for existing songs and
# manage a write lock to prevent concurrent writes.
class Playlist:
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
