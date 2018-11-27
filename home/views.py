from django.shortcuts import render, reverse, redirect
from load_csv.models import Province as ProvinceModel
from csp.models import ProvinceNeighbors
from csp.utils import Color, Province, Graph, Csp, LocalSearch

# Create your views here.
def index(request):
  return render(request, 'index.html')

def submit_tanaman(request):
  if request.method == 'POST':
    input = request.POST['tanamans']
    jumlah = input.split("_")[0]
    tanamans = input.split("_")[1:]
    colors = []
    graph = Graph()
    for i in range(int(jumlah)):
      colors.append(Color(i + 1, tanamans[i]))
    # for province in ProvinceModel.objects.all().iterator():
    #   provinces.append(Province(province.name, province.area))
    for obj in ProvinceNeighbors.objects.all().iterator():
      prov = Province(name=obj.province.name, area=obj.province.area)
      if obj.neighbor:
        graph.add_edge(prov, Province(name=obj.neighbor.name, area=obj.neighbor.area))
      else:
        graph.add_edge(prov)
    # print(graph.keys())
    csp = Csp(graph, colors)
    local_search = LocalSearch(csp)
    for i in local_search.min_conflicts():
      print(i.name, i.color)

  return redirect("home:index")