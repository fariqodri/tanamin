from django.db import models

# Create your models here.
class Province(models.Model):
  name = models.CharField(max_length=20, unique=True)
  area = models.FloatField()