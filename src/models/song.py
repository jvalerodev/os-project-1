from datetime import datetime


class Song:
    def __init__(self):
        self.title = input("-Título: ")
        self.interpreter = input("-Intérprete: ")
        self.album = input("-Álbum: ")
        self.date_added = datetime.now()
        self.user = input("-Tu nombre de usuario: ")
        self.duration = input("-Duración: ")
