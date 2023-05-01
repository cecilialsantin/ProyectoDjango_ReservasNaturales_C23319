from django.db import models

# Create your models here.
class Campsite(models.Model):
    
    categoty= models.CharField(max_length=100, null=False, unique=True, verbose_name='Categoria')
  