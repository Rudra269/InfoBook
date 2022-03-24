from django.db import models

class Livre(models.Model):
    titre =models.CharField(max_length=50)
    descrption = models.TextField()
    image = models.CharField(max_length=2000)
