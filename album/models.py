from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=30)
    album_release_date = models.DateField()
    rating = models.IntegerField()
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name