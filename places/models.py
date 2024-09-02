from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField()
    date = models.DateField(auto_now_add=False)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    