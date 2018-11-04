from collections import defaultdict
from .exceptions import DestinationNotExistError

class Color:
  '''
  Class that encapsulate color name, hex code, and type of plant it represents
  '''
  def __init__(self, name, hex, plant):
    self.name = name
    self.hex = hex
    self.plant = plant

  def __str__(self):
    return self.name

class Province:
  '''
  Class that encapsulate province name, area, and color it is represented
  '''
  def __init__(self, name, area, color: Color=None):
    self.name = name
    self.area = area
    self.color = color
  
  def get_color(self):
    return self.color
  
  def set_color(self, color: Color):
    self.color = color

  def __str__(self):
    return self.name

class ConstraintGraph:
  '''
  Constraint graph class
  '''
  def __init__(self, init: dict=None):
    if init:
      self.graph = init
    else:
      self.graph = defaultdict(list)
  
  def generate_edges(self):
    '''
    Show all edges
    '''
    edges = list()
    for node in self.graph:
      for neighbor in self.graph[node]:
        edges.append((node, neighbor))
    return edges
  
  def add_edge(self, source, destination):
    '''
    Add new edge, source 
    '''
    if destination in self.graph:
      self.graph[source].append(destination)
      return source, destination
    else:
      raise DestinationNotExistError("Destination does not exist in graph")
    
  
  def find_path(self, start, end, path=[]):
    '''
    Find path from start to end
    '''
    path = path + [start]
    if start == end:
      return path
    for node in self.graph[start]:
      if node not in path:
        newpath = self.find_path(node, end, path)
        if newpath:
          return newpath
        return None
    
  def find_all_paths(self, start, end, path =[]): 
    '''
    Find all possible paths from start to end
    '''
    path = path + [start] 
    if start == end: 
      return [path] 
    paths = [] 
    for node in self.graph[start]: 
      if node not in path: 
        newpaths = self.find_all_paths(node, end, path) 
      for newpath in newpaths: 
        paths.append(newpath) 
    return paths
  
  def find_shortest_path(self, start, end, path=[]):
    '''
    Find shortest path from start to end
    '''
    path = path + [start] 
    if start == end: 
        return path 
    shortest = None
    for node in self.graph[start]: 
        if node not in path: 
            newpath = self.find_shortest_path(node, end, path) 
            if newpath: 
                if not shortest or len(newpath) < len(shortest): 
                    shortest = newpath 
    return shortest 