from django.db import models

class Genre(models.Model):
    nom = models.CharField(max_length=50)
    image = models.CharField(max_length=2000)

# Create your models here.
