from django.db import models

# Create your models here.

class Talebe(models.Model):
    TC= models.CharField(max_length=11)
    AdiSoyadi = models.CharField(max_length=50)
    Aciklama= models.CharField(max_length=255)
    sinif =models.CharField(max_length=15, null=True)
   
