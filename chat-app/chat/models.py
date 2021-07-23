from django.db import models
from datetime import datetime


class Room(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.TextField()
    date = models.DateTimeField(default=datetime.now(), blank=True)
    user = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
