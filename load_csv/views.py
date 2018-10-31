from django.shortcuts import render
import csv, os
from functools import reduce
import math
from .models import Province

# Create your views here.
def load(request):
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  Province.objects.all().delete()
  with open(os.path.join(BASE_DIR, 'data.csv')) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader, None)

    provinces = [province for province in csv_reader]
    areas = [int(province[-1]) for province in provinces]
    names = [province[0] for province in provinces]

    z_scored_areas = get_z_scores(areas)
    province_with_areas = [[names[i], z_scored_areas[i]] for i in range(len(areas))]
    
    for province in province_with_areas:
      Province(name=province[0], area=province[-1]).save()

  return render(request, "table.html", {"data_provinsi": province_with_areas})
    

def get_mean(numbers):
  total = reduce(lambda prev, curr: prev + curr, numbers)
  return total/len(numbers)

def get_stdev(numbers):
  mean = get_mean(numbers)
  upper = reduce(lambda prev, curr: prev + math.pow(curr - mean, 2), numbers, 0)
  return math.sqrt(upper/len(numbers))

def get_z_scores(numbers):
  mean = get_mean(numbers)
  stdev = get_stdev(numbers)
  z_scores = [(x - mean)/stdev for x in numbers]
  return z_scores