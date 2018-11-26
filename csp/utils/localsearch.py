from load_csv.models import Province as ProvinceModel
from csp.utils import Province

class LocalSearch:
	def __init__(self, csp):
		self.csp = csp
	
	def check_solution(self, current):
		for edge in current:
			if edge[0].get_color() == edge[1].get_color():
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
			# for color, area in color_area:
			color, area = color_area[0]
			# print(province.name, color_area)
			province.set_color(color)
			color_area[0][1] -= province.area
					# break

		# luass = {'padi': 0, 'tebu': 0, 'teh': 0, 'jagung': 0}
		for province in province_list:
			# luass[province.color.plant] += province.area
			print(province.name, province.color)
		# print(luass)
		return province_list
		
	def min_conflicts(self, max_steps):
		current = self.assign()
		