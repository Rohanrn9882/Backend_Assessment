from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    genre = models. CharField(max_length = 50)
    uuid = models.IntegerField(primary_key = True)
