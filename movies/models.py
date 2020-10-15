from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=500)


class Movie(models.Model):

    name = models.CharField(max_length=500)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    director = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre,blank=True)
