from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=300)

    def __str__(self):
        return self.name