from django.db import models

# Create your models here.
class Province(models.Model):
  name = models.CharField(max_length=20, unique=True)
  area = models.FloatField()

class ProvinceNeighbor(models.Model):
  province = models.ForeignKey(Province, on_delete=models.CASCADE)
  neighbor = models.ForeignKey(Province, related_name="neighbor")

  class Meta:
    unique_together = (province, neighbor)