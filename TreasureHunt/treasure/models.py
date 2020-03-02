from django.db import models

# Create your models here.


class MapRoom:
    def __init__(self, room, neighbors):
        self.room_id = room.room_id
        self.title = room.title
        self.description = room.description
        self.coordinates = room.coordinates
        self.neighbors = neighbors
