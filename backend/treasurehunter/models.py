from django.db import models

# Create your models here.


class Room(models.Model):
    room_id = models.IntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    coordinates = models.CharField(blank=True, max_length=200)
