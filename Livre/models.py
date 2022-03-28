from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=50)
    image = models.CharField(max_length=2000)
    description = models.CharField(max_length=50)
    auteur = models.CharField(max_length=50)
    format = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    genre = models.IntegerField()

# Create your models here.

# Create your models here.
