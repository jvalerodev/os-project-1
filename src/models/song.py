from datetime import datetime


# The class "Song" allows the user to input information about a song, such as title, interpreter,
# album, date added, user, and duration.
class Song:
    def __init__(self):
        self.title = input("-Título: ")
        self.interpreter = input("-Intérprete: ")
        self.album = input("-Álbum: ")
        self.date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.user = input("-Tu nombre de usuario: ")
        self.duration = input("-Duración: ")
