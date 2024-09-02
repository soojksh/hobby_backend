from django.db import models



class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300)
    image = models.ImageField()

    def __str__(self):
        return self.name