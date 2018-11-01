from django.shortcuts import render
from load_csv.models import Province
# Create your views here.

def constraint_graph(request):
    q = Province.objects.all()[0].name
    objs = [[x.name, x.area] for x in q]
    graph = dict()
