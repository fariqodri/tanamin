from load_csv.models import Province as ProvinceModel
from csp.utils import Province

class LocalSearch:
	def __init__(self, csp):
		self.csp = csp
	
	def check_solution(self, current):
		d = {}
		for prov in current:
			d[prov] = prov
		for a,b in self.csp.graph.generate_edges():
			if d[a].color == d[b].color:
				return False
		return True

	def conflicted_variable(self, current):
		d = {}
		vars = []
		for prov in current:
			d[prov] = prov
		for a,b in self.csp.graph.generate_edges():
			if d[a].color == d[b].color:
				vars.append(a)
				vars.append(b)
		return vars

	def conflicts(self, variable, value, current):
		for i in range(len(current)):
			for province in current[i]:
				if province.get_name() == variable.get_name():
					province.set_color(value)
					return self.calculate_conflicts(current)

	def calculate_conflicts(self, current):
		count = 0
		for edge in current:
			if edge[0].get_color() == edge[1].get_color():
				count += 1
		return count
	
	def assign(self):
		AREA = 8087393
		area_divided = AREA // 4
		color_area = []
		province_list = self.csp.variables
		for i in self.csp.domains:
			color_area.append([i, area_divided])
		for province in province_list:
			color_area.sort(key=lambda x: x[1], reverse=True)
			color, area = color_area[0]
			province.set_color(color)
			color_area[0][1] -= province.area
		self.csp.variables = province_list
		return province_list

	def min_conflicts(self, max_steps=100000):
		current = self.assign()
		if self.check_solution(current):
			return current
		conflicts = self.conflicted_variable(current)
		