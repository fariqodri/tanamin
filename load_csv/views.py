from django.shortcuts import render
import csv, os
from functools import reduce
import math
from .models import Province
from tanamin.settings import BASE_DIR
from csp.models import ProvinceNeighbors

# Create your views here.
def load(request):
  Province.objects.all().delete()
  ProvinceNeighbors.objects.all().delete()
  with open(os.path.join(BASE_DIR, 'data.csv')) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader, None)

    provinces = [province for province in csv_reader]
    areas = [int(province[1]) for province in provinces]
    names = [province[0] for province in provinces]
    neighbors = [province[2] for province in provinces]
    
    province_with_areas = [[names[i], areas[i], neighbors[i]] for i in range(len(areas))]
    province_with_areas.sort(key=lambda x: x[1], reverse=True)

    for name, area, neighbors in province_with_areas:
      pro = Province(name=name, area=area)
      pro.save()
    for name, area, neighbors in province_with_areas:
      print(neighbors.split(", "))
      for ngbr_name in neighbors.split(", "):
        curr = Province.objects.get(name=name)
        if ngbr_name != "":
          print(ngbr_name)
          ngbr_obj = Province.objects.get(name=ngbr_name)
          conn_obj = ProvinceNeighbors(province=curr, neighbor=ngbr_obj)
        else:
          conn_obj = ProvinceNeighbors(province=curr, neighbor=None)
        conn_obj.save()

  return render(request, "table.html", {"data_provinsi": province_with_areas})