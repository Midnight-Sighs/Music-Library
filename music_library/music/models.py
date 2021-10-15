from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_year = models.CharField(max_length=4)
    like_counter = models.IntegerField()
    genre = models.CharField(max_length=50)