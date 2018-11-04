from django.db import models
from load_csv.models import Province
# Create your models here.
class ProvinceNeighbors(models.Model):
  province = models.ForeignKey(Province, on_delete=models.CASCADE)
  neighbor = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="neighbor", null=True)

  class Meta:
    unique_together = ("province", "neighbor")