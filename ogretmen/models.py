from django.db import models

# Create your models here.
class Muallim(models.Model):
  TC = models.CharField(max_length=11)
  AdiSoyadi = models.CharField(max_length=50)
  Branşı = models.CharField(max_length=30)
