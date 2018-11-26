from load_csv.models import Province as ProvinceModel
from csp.utils import Province

class LocalSearch:
	def __init__(self, csp):
		self.csp = csp
	
	def check_solution(self, current):
		for province in current:
			curr = self.csp.graph.graph[province]
			for neigh in curr:
				if neigh.color == curr.color:
					return False
		return True
	
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
		print(self.csp.graph.update_edge(province_list))
		return province_list

	def min_conflicts(self, max_steps=100000):
		current = self.assign()
		if self.check_solution:
			return current
		