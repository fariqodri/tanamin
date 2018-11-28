class Csp:
	def __init__(self, graph, colors):
		self.variables = list(graph.keys())
		self.domains = colors
		self.constraints = graph.generate_edges()
		self.graph = graph
	
	def get_variables(self):
		return self.variables

	def get_domains(self):
		return self.domains

	def get_constraints(self):
		return self.constraints
