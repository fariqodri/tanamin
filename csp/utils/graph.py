from csp.exceptions import DestinationNotExistError
from collections import defaultdict

class Graph:
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
	
	def add_edge(self, source, destination=None):
		'''
		Add new edge, source 
		'''
		if destination:
			self.graph[source].append(destination)
		else:
			self.graph[source] = []
		return source, destination
	
	def keys(self):
		return self.graph.keys()

	def __repr__(self):
		return str(dict(self.graph))
