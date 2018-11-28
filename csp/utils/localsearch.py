from load_csv.models import Province as ProvinceModel
from csp.utils import Province
import random
import math

class LocalSearch:
	def __init__(self, csp, big_to_small=True):
		self.csp = csp
		self.big_to_small = big_to_small
	
	def check_solution(self, current):
		for a,b in self.csp.constraints:
			if current[a.name].color == current[b.name].color:
				return False
		return True

	def conflicted_variable(self, current):
		vars = []
		for a,b in self.csp.graph.generate_edges():
			if current[a.name].color == current[b.name].color:
				if (a not in vars):
					vars.append(current[a.name])
				if (b not in vars):
					vars.append(current[b.name])
		return vars

	def conflicts(self, variable, value, current):
		province = current[variable.name]
		province.set_color(value)
		current[variable.name] = province
		return self.calculate_conflicts(current)

	def color_heuristic(self, variable, value, current):
		current[variable.name].set_color(value)
		# current[variable.name] = province
		print(self.get_area_of_color(value, current))
		if self.get_area_of_color(value, current) > self.max_area:
			return False			

	def calculate_conflicts(self, current):
		count = 0
		for a,b in self.csp.constraints:
			if current[a.name].color == current[b.name].color:
				count += 1
		return count
	
	def assign(self):
		# print("ASSIGN")
		AREA = 8087393
		area_divided = AREA // 4
		self.max_area = area_divided
		color_area = []
		result = {}
		for i in self.csp.domains:
			color_area.append([i, area_divided])
		self.csp.variables.sort(key=lambda x:x.area, reverse=self.big_to_small)
		self.color_area = color_area
		assigned_provinces = set()
		while not len(assigned_provinces) == len(self.csp.variables):
			province = self.csp.variables[random.randint(0, len(self.csp.variables)-1)]
			if not assigned_provinces.__contains__(province):
				color_area.sort(key=lambda x: x[1], reverse=True)
				# idx = random.randint(0, len(color_area) - 1)
				color, area = color_area[0]
				province.set_color(color)
				color_area[0][1] -= province.area
				result[province.name] = province
				assigned_provinces.add(province)
		result = dict(sorted(result.items(), key=lambda x : x[1].area, reverse=True))
		print(result)
		return result

	'''CARI VALUE YANG BISA MEMINIMALISIR KONFLIK DAN MEMPERTAHANKAN KONSISTENSI LUAS'''
	def find_value(self, var, current):
		# print("FIND VALUE")
		
		confs = self.calculate_conflicts(current)
		curr_confs = 100000000000
		for value in self.csp.domains:
			curr_confs = self.conflicts(var, value, current)
			self.color_heuristic(var, value, current)
			if (curr_confs < confs):
					return value

	def get_area_of_color(self, color, current):
		count = 0
		for i in current:
			if current[i].color == color:
				count += current[i].area
		return count

	def min_conflicts(self, max_steps=100):
		current = self.assign()
		# print(current)
		for i in range(max_steps):
			print("iter:", i, ", conflicts: ", self.calculate_conflicts(current))
			if self.check_solution(current):
				return current
			conflicts = self.conflicted_variable(current)
			var = conflicts[random.randint(0, len(conflicts) - 1)]
			value = self.find_value(var, current)
			if value:
				current[var.name].set_color(value)
		return current